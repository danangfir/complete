from bs4 import BeautifulSoup
from .storage import save_to_json

def parser_html(html_pages):
    print("Parsing HTML content...")
    if not html_pages:
        print("No HTML Content To Parse")
        return None

    data = []

    for html in html_pages:
        soup = BeautifulSoup(html, 'html.parser')
        books = soup.find_all('article', class_='product_pod')

        for book in books:
            # Ambil nama buku
            name = book.h3.a['title']

            # Ambil Rating
            rating_class = book.find('p', class_='star-rating')
            rating = rating_class.get('class', [])[1] if rating_class else "No Rating"

            # Ambil Harga
            price = book.find('p', class_='price_color').text.strip()

            # Tambahkan list ke data
            data.append({
                "name": name,
                "rating": rating,
                "price": price
            })

    # Simpan data ke JSON
    save_to_json(data)
    return data
