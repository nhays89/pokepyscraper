import requests
from bs4 import BeautifulSoup

def check_stock(product_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    
    try:
        print(product_url);
        response = requests.get(product_url, headers=headers)
        response.raise_for_status()  # Ensure the request was successful
        print(response.text);
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Update the selector based on PokemonCenter's HTML structure
        buttons = soup.find_all('button')
        print(buttons)
        for btn in buttons:
            print(btn)
        addtoCartBtn = "none yet"
        if addtoCartBtn and "add to cart" in addtoCartBtn:
            print("Product is in stock!")
        else:
            print("Product is still out of stock.")
            
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching product page: {e}")

# Replace with the product URL you want to monitor
product_url = "https://www.pokemoncenter.com/product/10-10125-102/pokemon-tcg-scarlet-and-violet-journey-together-enhanced-booster-display-box-36-packs-and-1-promo-card"
product_url_test = "https://www.pokemoncenter.com/product/176-80818/pokemon-tcg-sword-and-shield-battle-styles-booster-display-box-36-packs"
check_stock(product_url_test)
