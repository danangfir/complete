from playwright.sync_api import sync_playwright
from .config import BASE_URL, HEADLESS, TIMEOUT

def scrape_page(url=BASE_URL):
    with sync_playwright() as p:
        print("Launching browser...")
        browser = p.chromium.launch(headless=HEADLESS)
        print("Browser launched successfully.")

        page = browser.new_page()
        page.set_default_timeout(TIMEOUT * 1000)

        print(f"Navigating to: {url}")
        response = page.goto(url)

        if response and response.ok:
            print(f"Page loaded successfully: {url} (Status: {response.status})")
        else:
            print(f"Failed to load page. Status: {response.status if response else 'No response'}")

        content = page.content()
        browser.close()
        return content
