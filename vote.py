from playwright.sync_api import sync_playwright
import time

USERNAME = "SAROJGMG"
URL = "https://topg.org/minecraft-servers/server-654317"

with sync_playwright() as p:

    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    print("Opening page...")

    page.goto(URL, wait_until="domcontentloaded")

    time.sleep(5)

    print("Filling username...")

    page.fill("#game_user", USERNAME)

    time.sleep(2)

    print("Clicking submit...")

    page.click("#submit")

    time.sleep(10)

    page.screenshot(path="vote_result.png")

    print("Done!")

    browser.close()
