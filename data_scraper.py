import requests
from bs4 import BeautifulSoup

URL = "https://appbrewery.github.io/Zillow-Clone/"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9"
}

def get_listings():
    response = requests.get(URL, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    all_links = [a['href'] for a in soup.select(".StyledPropertyCardDataWrapper a") if a.get("href")]
    all_prices = [price.get_text().split("+")[0].split("/")[0].strip()
                  for price in soup.select(".PropertyCardWrapper span")]
    all_addresses = [addr.get_text().strip()
                     for addr in soup.select(".StyledPropertyCardDataWrapper address")]

    listings = list(zip(all_addresses, all_prices, all_links))

    print("listings = [")
    for address, price, link in listings:
        print(f'    ("{address}", "{price}", "{link}"),')
    print("]")

if __name__ == "__main__":
    get_listings()  # Only prints out the formatted listings list