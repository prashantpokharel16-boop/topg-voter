from playwright.sync_api import sync_playwright
import time

USERNAME = "Creamofmeatball"
URL = "https://topg.org/minecraft-servers/server-684395"

with sync_playwright() as p:

    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    print("Opening page...")

    page.goto(URL, wait_until="domcontentloaded")

    time.sleep(5)

    print("Opening vote popup...")

    page.click("#openModal")

    time.sleep(3)

    print("Filling username...")

    page.fill("#game_user", USERNAME)

    time.sleep(2)

    print("Submitting vote...")

    page.click("#submit")

    time.sleep(10)

    page.screenshot(path="vote_result.png")

    print("Done!")

    browser.close()
