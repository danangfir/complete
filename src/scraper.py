from playwright.sync_api import sync_playwright
from config import BASE_URL, HEADLESS, TIMEOUT, CHROMEDRIVER_PATH

def scrape_page(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=HEADLESS, executable_path=CHROMEDRIVER_PATH)
        
        
        