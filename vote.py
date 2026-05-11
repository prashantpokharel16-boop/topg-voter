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
        page.goto(VOTE_URL, wait_until="domcontentloaded")
        time.sleep(8)

        # Step 1 — Click the "Vote for server" button to open the modal
        print("Opening vote modal...")
        try:
            page.click('a:has-text("Vote for server")', timeout=10000)
            print("Clicked Vote for server link")
        except:
            try:
                page.click('button:has-text("Vote")', timeout=10000)
                print("Clicked Vote button")
            except:
                print("❌ Could not open vote modal")

        time.sleep(4)

        # Step 2 — Now fill the username field inside the modal
        print(f"Filling username: {MINECRAFT_USERNAME}")
        try:
            page.fill('input[name="voter_name"]', MINECRAFT_USERNAME, timeout=15000)
            print("Username filled!")
        except:
            print("❌ Could not find username field")

        time.sleep(2)

        # Step 3 — Click Submit
        print("Submitting vote...")
        try:
            page.click('button[type="submit"], input[type="submit"]', timeout=10000)
            print("Submit clicked!")
        except:
            print("❌ Could not click submit")

        time.sleep(6)

        # Check result
        content = page.content()
        if "thank" in content.lower() or "success" in content.lower() or "voted" in content.lower():
            print("✅ VOTE SUCCESS!")
        elif "already" in content.lower():
            print("⏰ Already voted - cooldown not finished yet")
        elif "captcha" in content.lower() or "hcaptcha" in content.lower():
            print("🚫 BLOCKED BY CAPTCHA")
        else:
            print("❓ UNKNOWN RESULT - check screenshot")

        # Save screenshot
        screenshot_path = os.path.join(os.getcwd(), "vote_result.png")
        page.screenshot(path=screenshot_path)
        print(f"Screenshot saved to: {screenshot_path}")
        print("Page title:", page.title())
        print("Page URL:", page.url)
        print("Page content snippet:", page.content()[:800])

        browser.close()

if __name__ == "__main__":
    run_vote()
