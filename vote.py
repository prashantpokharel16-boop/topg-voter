import time
import random
from playwright.sync_api import sync_playwright

def run_vote():
    with sync_playwright() as p:
        # We use a more "stealthy" launch
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        )
        page = context.new_page()

        print("Navigating to TopG...")
        page.goto("https://topg.org/minecraft-servers/server-654317", wait_until="domcontentloaded")
        
        # Random delay to mimic a human reading the page
        time.sleep(random.uniform(5, 10))

        try:
            # Check if username field is visible
            username_field = page.locator('#voter_name')
            if username_field.is_visible():
                print("Entering username: SAROJGMG")
                username_field.fill("SAROJGMG")
                time.sleep(random.uniform(1, 3))
                
                print("Clicking the Vote button...")
                page.click('#vote_button')
                
                # IMPORTANT: TopG often has a small delay or a redirect after voting
                time.sleep(10)
                
                # Check for success message on the page
                if "thanks for voting" in page.content().lower() or "voted successfully" in page.content().lower():
                    print("SUCCESS: Vote confirmed by website!")
                else:
                    print("WARNING: Clicked, but success message not found. TopG might be blocking the IP.")
            else:
                print("ERROR: Username field not found. Page might be blocked by Cloudflare.")
                page.screenshot(path="blocked.png")

        except Exception as e:
            print(f"Error occurred: {e}")
            page.screenshot(path="error.png")

        browser.close()

if __name__ == "__main__":
    run_vote()    run_vote()
