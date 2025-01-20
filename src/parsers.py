from bs4 import BeautifulSoup
import requests
from .config import BASE_URL

def parser_html(html):
    print("Parsing HTML content...")
    if not html:
        print("No HTML Content To Parse")
        return None
    
    # membuat request
    # r = requests.get(BASE_URL)
    # soup = BeautifulSoup(r.content, 'html.parser')
    
    
    # Jika Berjalan kita command
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # MEncari semua Nama Novel
    books = soup.find_all('article', class_='product_pod')
    
    # kita gunakan Loop buat mengekstrak semua nama novel
    for book in books:
        title = book.h3.a['title']
        print(title)






























