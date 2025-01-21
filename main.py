from src.config import BASE_URL
from src.parsers import parser_html
from src.storage import save_to_json
from src.scraper import scrape_page

if __name__ == "__main__":
    asci = """
    ███████╗████████╗ █████╗ ██████╗ ████████╗██╗███╗   ██╗ ██████╗     
    ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝██║████╗  ██║██╔════╝     
    ███████╗   ██║   ███████║██████╔╝   ██║   ██║██╔██╗ ██║██║  ███╗    
    ╚════██║   ██║   ██╔══██║██╔══██╗   ██║   ██║██║╚██╗██║██║   ██║    
    ███████║   ██║   ██║  ██║██║  ██║   ██║   ██║██║ ╚████║╚██████╔╝    
    ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝     
    """
    print(asci)

    print("Scraping all pages...")
    html_pages = scrape_page()  
    if not html_pages:
        print("Failed to scrape the pages or no content returned.")
        exit()

    print("Parsing HTML content from all pages...")
    data = parser_html(html_pages)  
    if not data:
        print("Failed to parse HTML or no data extracted.")
        exit()

    print("Saving data to JSON...")
    save_to_json(data)

    ascii = """
    ██████╗  ██████╗ ███╗   ██╗███████╗
    ██╔══██╗██╔═══██╗████╗  ██║██╔════╝
    ██║  ██║██║   ██║██╔██╗ ██║█████╗  
    ██║  ██║██║   ██║██║╚██╗██║██╔══╝  
    ██████╔╝╚██████╔╝██║ ╚████║███████╗
    ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚══════╝
    """
    print(ascii)
