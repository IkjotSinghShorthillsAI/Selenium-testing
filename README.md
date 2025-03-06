# Selenium Test Script - Demo Login

## Overview
This script uses Selenium WebDriver to automate the login process for the OrangeHRM demo site. It initializes a Chrome WebDriver, navigates to the login page, enters credentials, submits the form, and then closes the browser.

## Prerequisites
Ensure you have the following installed before running the script:
- Python (3.x recommended)
- Google Chrome browser
- Chrome WebDriver (Ensure the driver version matches your Chrome version)
- Selenium library

## Installation
1. Install Selenium using pip:
   ```sh
   pip install selenium
   ```
2. Download the Chrome WebDriver from:
   [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)
3. Place the WebDriver executable in a directory accessible via system PATH or specify its path in the script.

## Usage
1. Save the script as `main.py`.
2. Run the script using:
   ```sh
   python main.py
   ```

## Script Functionality
- Opens the OrangeHRM login page.
- Enters the username (`Admin`).
- Enters the password (`admin123`).
- Submits the login form.
- Waits for the response.
- Closes the browser session.


