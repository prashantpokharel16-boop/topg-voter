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
        time.sleep(random.uniform(3, 6))

        # Fill username field
        print(f"Filling username: {MINECRAFT_USERNAME}")
        page.fill('input[name="voter_name"]', MINECRAFT_USERNAME)
        time.sleep(random.uniform(1, 3))

        # Click the Submit button
        print("Clicking Submit...")
        page.click('input[type="submit"], button[type="submit"]')
        time.sleep(6)

        # Save screenshot to check result
        page.screenshot(path="vote_result.png")
        print("Done! Check vote_result.png to see if it succeeded.")

        browser.close()

if __name__ == "__main__":
    run_vote()                    print("SUCCESS: Vote confirmed by website!")
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
