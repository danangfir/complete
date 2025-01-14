from playwright.sync_api import sync_playwright
from .config import BASE_URL, HEADLESS, CHROMEDRIVER_PATH

def scrape_page(url=BASE_URL):
    with sync_playwright() as p:
        try:
            print(f"Launching browser to scrape: {url}")
            browser = p.chromium.launch(headless=HEADLESS, executable_path=CHROMEDRIVER_PATH)
            page = browser.new_page()
            response = page.goto(url)
            
            if response and response.ok:
                print(f"Successfully loaded page: {url} (Status: {response.status})")
            else:
                print(f"Failed to load page. Status: {response.status if response else 'No response'}")
                browser.close()
                return None

            content = page.content()
            print("Scraped content successfully")
            browser.close()
            return content
        except Exception as e:
            print(f"Error during scraping: {e}")
            return None
    