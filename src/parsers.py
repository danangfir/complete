from bs4 import BeautifulSoup
import requests
from .config import BASE_URL

def parser_html(html):
    print("Parsing HTML content...")
    if not html:
        print("No HTML Content To Parse")
        return None
    
    # membuat request
    r = requests.get(BASE_URL)
    soup = BeautifulSoup(r.content, 'html.parser')
    
    
    # Jika Berjalan kita command
    #  soup = BeautifulSoup(html.content, 'html.parser')
    
    # Ekstrak judul halaman






























