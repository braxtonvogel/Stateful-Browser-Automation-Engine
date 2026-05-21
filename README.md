# Stateful Browser Automation Engine

A lightweight Python automation framework built with Playwright for managing persistent, authenticated browser sessions and automating web workflows.

---

## Overview

This project demonstrates how to build a **stateful browser automation system** that can:

- Maintain persistent login sessions across runs
- Automate browser navigation workflows
- Reuse authenticated contexts without re-login
- Interact with dynamic web applications using Playwright

It is designed as a reusable foundation for building more advanced automation systems.

---

## Key Features

- Persistent authentication using saved browser state
- Automated navigation of web pages
- Fast session reuse without repeated login
- Stateful browser context management
- Built on Playwright (Chromium automation)

---

## Use Case Example

This engine can be adapted for:

- Automating dashboard workflows
- Accessing authenticated web systems
- Navigating member-only pages
- Repetitive browser tasks requiring login state
- Data collection from session-based websites (where permitted)

---

## Screenshots

### Automated Navigation in Action

![Automation Running](Screenshots/in_action.png)

### Final Product 

![Login Setup](Screenshots/finished.png)

---

## Tech Stack

- Python 3.10+
- Playwright
- Chromium browser automation

---

## Project Structure

```text
Stateful-Browser-Automation-Engine/
│
├── main.py
├── requirements.txt
├── README.md
├── screenshots/
│   ├── finished.png
│   └── in_action.png
└── .gitignore
