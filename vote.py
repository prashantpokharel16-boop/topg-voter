import time
import random
import os
from playwright.sync_api import sync_playwright

MINECRAFT_USERNAME = "SAROJGMG"
VOTE_URL = "https://topg.org/minecraft-servers/server-654317"

def run_vote():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        )
        page = context.new_page()

        print("Opening vote page...")
        page.goto(VOTE_URL, wait_until="networkidle")
        time.sleep(random.uniform(3, 6))

        print(f"Filling username: {MINECRAFT_USERNAME}")
        page.fill('input[name="voter_name"]', MINECRAFT_USERNAME)
        time.sleep(random.uniform(1, 3))

        print("Clicking Submit...")
        page.click('input[type="submit"], button[type="submit"]')
        time.sleep(6)

        # Save screenshot with absolute path
        screenshot_path = os.path.join(os.getcwd(), "vote_result.png")
        page.screenshot(path=screenshot_path)
        print(f"Screenshot saved to: {screenshot_path}")

        # Print page content so we can see result in logs
        print("Page title:", page.title())
        print("Page URL:", page.url)
        print("Page content snippet:", page.content()[:500])

        browser.close()

if __name__ == "__main__":
    run_vote()    run_vote()
