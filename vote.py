from playwright.sync_api import sync_playwright
import time

URL = "https://topg.org/minecraft-servers/server-654317"

with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=False,   # IMPORTANT FOR DEBUGGING
        slow_mo=500
    )

    page = browser.new_page()

    print("Opening page...")
    page.goto(URL, wait_until="domcontentloaded")

    time.sleep(5)

    print("\n=== INPUTS FOUND ===")

    inputs = page.locator("input")
    count = inputs.count()

    for i in range(count):
        item = inputs.nth(i)

        print({
            "index": i,
            "name": item.get_attribute("name"),
            "id": item.get_attribute("id"),
            "type": item.get_attribute("type"),
            "placeholder": item.get_attribute("placeholder")
        })

    print("\n=== BUTTONS FOUND ===")

    buttons = page.locator("button")

    for i in range(buttons.count()):
        btn = buttons.nth(i)

        try:
            print({
                "index": i,
                "text": btn.inner_text(),
                "id": btn.get_attribute("id"),
                "type": btn.get_attribute("type")
            })
        except:
            pass

    print("\nBrowser left open for inspection.")
    input("Press ENTER to close...")

    browser.close()
