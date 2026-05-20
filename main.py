from playwright.sync_api import sync_playwright
import requests
import os
import time

GROUP_ID = "YOURGROUPID"

GROUP_URL = f"https://www.facebook.com/groups/YOUR_GROUP/media"

DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

def is_valid_image(url):
    return url and ("scontent" in url or "fbcdn" in url)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    context = browser.new_context(storage_state="fb_session.json")
    page = context.new_page()

    page.goto(GROUP_URL)
    time.sleep(8)

    print("Opened group photos page")

    seen_images = set()
    last_count = 0
    stagnant_rounds = 0

    # Scroll until no new images appear anymore
    for i in range(200):  # safety limit
        page.mouse.wheel(0, 8000)
        time.sleep(3)

        images = page.locator("img").all()

        for img in images:
            src = img.get_attribute("src")
            if is_valid_image(src):
                seen_images.add(src)

        current_count = len(seen_images)

        print(f"Scroll {i+1} | Found: {current_count}")

        # Stop if nothing new is loading
        if current_count == last_count:
            stagnant_rounds += 1
        else:
            stagnant_rounds = 0

        last_count = current_count

        # If Facebook stops loading new content
        if stagnant_rounds >= 5:
            print("No new images loading anymore. Stopping scroll.")
            break

    print(f"\nTotal unique images found: {len(seen_images)}\n")

    # Download images
    for idx, url in enumerate(seen_images):
        try:
            img_data = requests.get(url, timeout=10).content

            filename = os.path.join(DOWNLOAD_FOLDER, f"image_{idx}.jpg")

            with open(filename, "wb") as f:
                f.write(img_data)

            print(f"Downloaded {filename}")

        except Exception as e:
            print("Error downloading:", e)

    print("\nDONE.")