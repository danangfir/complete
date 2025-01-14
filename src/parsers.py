from bs4 import BeautifulSoup

def parser_html(html):
    print("Parsing HTML content...")
    if not html:
        print("No HTML Content To Parse")
        return None
    
    # Jika Berjalan kita command
    soup = BeautifulSoup(html, "html.parser")
    title = soup.string if soup.title else "No Title Found"
    
    print(f"Extracted title: {title}")
    return ("title", title)
    
    