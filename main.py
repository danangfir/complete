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

    print("Scraping page...")
    html = scrape_page()
    if not html:
        print("Failed to scrape the page or no content returned.")
        exit()

    print("Parsing HTML content...")
    data = parser_html(html)
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
