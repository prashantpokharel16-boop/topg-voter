import time
import random
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

        time.sleep(random.uniform(2, 5))

        print(f"Entering username: {MINECRAFT_USERNAME}")
        page.fill('input[name="voter_name"]', MINECRAFT_USERNAME)

        time.sleep(random.uniform(1, 3))

        print("Submitting vote...")
        page.click('button[type="submit"]')

        time.sleep(5)

        page.screenshot(path="vote_result.png")
        print("Done. Screenshot saved.")

        browser.close()

if __name__ == "__main__":
    run_vote()
