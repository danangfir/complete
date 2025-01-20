from bs4 import BeautifulSoup
import requests
from .config import BASE_URL
from .storage import save_to_json

def parser_html(html):
    print("Parsing HTML content...")
    if not html:
        print("No HTML Content To Parse")
        return None
    
    
    # Jika Berjalan kita command
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # list untuk menyimpan data
    data = []
    
    # looping agar bisa dapat datanya
    books = soup.find_all('article', class_='product_pod')
    for book in books:
        # ambil nama buku
        name = book.h3.a['title']
        # Ambil Rating (convert ke anka)
        rating_class = book.find('p', class_='star-rating')
        if rating_class:
            rating = rating_class.get('class', [])[1] if len (rating_class.get('class', [])) > 1 else "No Rating"
        else:
            rating = "No Rating"
            
        # Ambil Harga
        price = book.find('p', class_='price_color').text
        
        # Tambahkan list ke data
        data.append({
            "name": name,
            "rating": rating,
            "price": price
        })
    
    # simpan data ke json
    save_to_json(data)
