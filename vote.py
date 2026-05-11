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

        # Print ALL input fields found on page so we can see exact selectors
        inputs = page.query_selector_all('input')
        print(f"Found {len(inputs)} input fields:")
        for i, inp in enumerate(inputs):
            print(f"  Input {i}: name={inp.get_attribute('name')} type={inp.get_attribute('type')} id={inp.get_attribute('id')} placeholder={inp.get_attribute('placeholder')}")

        # Print ALL buttons found
        buttons = page.query_selector_all('button, input[type="submit"]')
        print(f"Found {len(buttons)} buttons:")
        for i, btn in enumerate(buttons):
            print(f"  Button {i}: text={btn.inner_text()} type={btn.get_attribute('type')} id={btn.get_attribute('id')}")

        browser.close()

if __name__ == "__main__":
    run_vote()        try:
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
