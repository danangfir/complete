from playwright.sync_api import sync_playwright
from .config import BASE_URL, HEADLESS, TIMEOUT

def scrape_page():
    with sync_playwright() as p:
        print("Launching browser...")
        browser = p.chromium.launch(headless=HEADLESS)
        print("Browser launched successfully.")

        page = browser.new_page()
        page.set_default_timeout(TIMEOUT * 1000)

        all_html = [] 
        page_number = 1

        while True:
            current_url = f"{BASE_URL}/page-{page_number}.html"
            print(f"Navigating to: {current_url}")

            try:
                response = page.goto(current_url)
                if not response or response.status == 404: 
                    print(f"Reached the last page or invalid page: {current_url}")
                    break

                all_html.append(page.content()) 
                page_number += 1 

            except Exception as e:
                print(f"Error navigating to page: {e}")
                break

        browser.close()
        return all_html
