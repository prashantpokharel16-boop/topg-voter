import time
from playwright.sync_api import sync_playwright

def run_vote():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        )
        page = context.new_page()

        print("Navigating to TopG...")
        page.goto("https://topg.org/minecraft-servers/server-654317", wait_until="networkidle")
        time.sleep(5)

        try:
            print("Entering username: SAROJGMR")
            # Fill the username field
            page.fill('#voter_name', "SAROJGMR")
            time.sleep(2)

            print("Clicking the Vote button...")
            # Click the green vote button
            page.click('#vote_button')
            
            # Wait to confirm the vote was sent
            time.sleep(10)
            print("Successfully submitted!")
            
        except Exception as e:
            print(f"Error: {e}")
            page.screenshot(path="error.png")

        browser.close()

if __name__ == "__main__":
    run_vote()
