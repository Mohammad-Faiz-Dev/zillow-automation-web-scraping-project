from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Replace with your scraped listings

listings = [
    ("747 Geary Street, 747 Geary St, Oakland, CA 94609", "$2,895", "https://www.zillow.com/b/747-geary-street-oakland-ca-CYzGVt/"),
    ("Parkmerced | 3711 19th Ave, San Francisco, CA", "$2,810", "https://www.zillow.com/apartments/san-francisco-ca/parkmerced/5XjKHx/"),
    ("845 Sutter, 845 Sutter St APT 509, San Francisco, CA", "$2,450", "https://www.zillow.com/apartments/san-francisco-ca/845-sutter/5XkKMm/"),
    ("100 Van Ness, 100 Van Ness Ave #410, San Francisco, CA 94102", "$2,940", "https://www.zillow.com/apartments/san-francisco-ca/100-van-ness/5hJ5Sv/"),
    ("828 Franklin, 828 Franklin St #606, San Francisco, CA 94102", "$2,395", "https://www.zillow.com/apartments/san-francisco-ca/828-franklin/5XkH2V/"),
    ("923 Folsom, 923 Folsom St APT 506, San Francisco, CA 94107", "$2,816", "https://www.zillow.com/apartments/san-francisco-ca/923-folsom/5Yy6Np/"),
    ("Hanover Soma West, 1140 Harrison St #138, San Francisco, CA 94103", "$2,974", "https://www.zillow.com/apartments/san-francisco-ca/hanover-soma-west/9NJsx9/"),
    ("Slate Residences, 911 Bryant St #102, San Francisco, CA 94103", "$2,704", "https://www.zillow.com/apartments/san-francisco-ca/slate-residences/9NJxjf/"),
    ("NorthPoint Apartments, 2211 Stockton St, San Francisco, CA 94133", "$2,810", "https://www.zillow.com/apartments/san-francisco-ca/northpoint-apartments/5XjLPJ/"),
    ("The Landing | 1395 22nd St, San Francisco, CA", "$2,798", "https://www.zillow.com/apartments/san-francisco-ca/the-landing/9NK3gC/"),
    ("1350 Washington Street | 1350 Washington St, San Francisco, CA", "$2,195", "https://www.zillow.com/apartments/san-francisco-ca/1350-washington-street/9NKDS7/"),
    ("2775 Market St, 2775 Market St APT 102, San Francisco, CA 94114", "$2,995", "https://www.zillow.com/apartments/san-francisco-ca/2775-market-st/5XsQ4D/"),
    ("Mt. Sutro, 480 Warren Dr #312, San Francisco, CA 94131", "$2,895", "https://www.zillow.com/apartments/san-francisco-ca/mt.-sutro/5XjVRC/"),
    ("Konrad on the Park, 971 Eddy St #212, San Francisco, CA 94109", "$2,805", "https://www.zillow.com/apartments/san-francisco-ca/konrad-on-the-park/9NKJXS/"),
    ("1188 Mission at Trinity Place | 1188 Mission St, San Francisco, CA", "$1914", "https://www.zillow.com/apartments/san-francisco-ca/1188-mission-at-trinity-place/5XjN4q/"),
    ("Nob Hill Place, 1155 Jones St APT 208, San Francisco, CA 94109", "$2,950", "https://www.zillow.com/apartments/san-francisco-ca/nob-hill-place/5XkKgw/"),
    ("Avalon Sunset Towers, 8 Locksley Ave, San Francisco, CA 94131", "$2,917", "https://www.zillow.com/b/avalon-sunset-towers-san-francisco-ca-5XjLKv/"),
    ("125-135 Gardenside, 125 Gardenside Dr, San Francisco, CA 94114", "$2,595", "https://www.zillow.com/apartments/san-francisco-ca/125.dash.135-gardenside/BjFbbM/"),
    ("Freedom West, 820 McAllister St, San Francisco, CA 94102", "$2,000", "https://www.zillow.com/apartments/san-francisco-ca/freedom-west/5mmHmr/"),
    ("Franklin St, 24 Franklin St #805, San Francisco, CA 94102", "$2,824", "https://www.zillow.com/apartments/san-francisco-ca/franklin-st/9NJqFL/"),
    ("Loft 168, 168 Bluxome St, San Francisco, CA 94107", "$2,800", "https://www.zillow.com/b/loft-168-san-francisco-ca-9NK42M/"),
    ("Mosser Towers Apartments, 455 Eddy St APT E1102, San Francisco, CA 94102", "$2,450", "https://www.zillow.com/apartments/san-francisco-ca/mosser-towers-apartments/9NJr4f/"),
    ("1029 Geary St., 1029 Geary St, San Francisco, CA 94109", "$2,095", "https://www.zillow.com/apartments/san-francisco-ca/1029-geary-st./5YCgZq/"),
    ("33 8th at Trinity Place | 33 8th St, San Francisco, CA", "$2,298", "https://www.zillow.com/apartments/san-francisco-ca/33-8th-at-trinity-place/9NJw4S/"),
    ("SoMa Square | 1 Saint Francis Pl, San Francisco, CA", "$2,809", "https://www.zillow.com/apartments/san-francisco-ca/soma-square/5Xj2Yr/"),
    ("480 Potrero Ave, 480 Potrero Ave #610, San Francisco, CA 94110", "$2,495", "https://www.zillow.com/apartments/san-francisco-ca/480-potrero-ave/5mY4JQ/"),
    ("The Mission | 240 Dolores St, San Francisco, CA", "$2,494", "https://www.zillow.com/apartments/san-francisco-ca/the-mission/5XjQJR/"),
    ("L Seven | 1222 Harrison St, San Francisco, CA", "$2,775", "https://www.zillow.com/apartments/san-francisco-ca/l-seven/9NJtD7/"),
    ("Palace Court Apartments | 555 Ofarrell St, San Francisco, CA", "$1,745", "https://www.zillow.com/apartments/san-francisco-ca/palace-court-apartments/5XjKSv/"),
    ("2000 Post | 2000 Post St, San Francisco, CA", "$2,764", "https://www.zillow.com/apartments/san-francisco-ca/2000-post/5XjRNn/"),
    ("HQ | 1532 Harrison St, San Francisco, CA", "$2,799", "https://www.zillow.com/apartments/san-francisco-ca/hq/9NJthZ/"),
    ("AVA 55 Ninth | 55 9th St, San Francisco, CA", "$2,525", "https://www.zillow.com/apartments/san-francisco-ca/ava-55-ninth/5XkH8X/"),
    ("The Bay | 2133 Stockton St, San Francisco, CA", "$2,199", "https://www.zillow.com/apartments/san-francisco-ca/the-bay/5Xhzkj/"),
    ("Lofts at Seven | 277 Golden Gate Ave, San Francisco, CA", "$1,995", "https://www.zillow.com/apartments/san-francisco-ca/lofts-at-seven/5XmsgS/"),
    ("347 Eddy St. | 347 Eddy St, San Francisco, CA", "$1,895", "https://www.zillow.com/apartments/san-francisco-ca/347-eddy-st./5XxfK3/"),
    ("Solaire | 299 Fremont St, San Francisco, CA", "$2,898", "https://www.zillow.com/b/solaire-san-francisco-ca-65g7KK/"),
    ("Marina Cove Apartments, 1550 Bay St APT B225, San Francisco, CA 94123", "$2,999", "https://www.zillow.com/apartments/san-francisco-ca/marina-cove-apartments/5XjRBB/"),
    ("Avalon Dogpatch, 800 Indiana St, San Francisco, CA 94107", "$2,830", "https://www.zillow.com/apartments/san-francisco-ca/avalon-dogpatch/5Yy5Rr/"),
    ("The Gateway, 430 Davis Ct #3-0306, San Francisco, CA 94111", "$2,895", "https://www.zillow.com/apartments/san-francisco-ca/the-gateway/5Xkxvk/"),
    ("50 Laguna, 50 Laguna St APT 604, San Francisco, CA 94102", "$2,775", "https://www.zillow.com/apartments/san-francisco-ca/50-laguna/5XjSDX/"),
    ("The Fillmore Center, 1475 Fillmore St #S30305, San Francisco, CA 94115", "$2,998", "https://www.zillow.com/apartments/san-francisco-ca/the-fillmore-center/5XjVzy/"),
    ("1333 Gough Apartments at Cathedral Hall, 1333 Gough St APT 1G, San Francisco, CA 94109", "$2,895", "https://www.zillow.com/apartments/san-francisco-ca/1333-gough-apartments-at-cathedral-hall/5XjRmn/"),
    ("1177 Market at Trinity Place | 1177 Market St, San Francisco, CA", "$2,773", "https://www.zillow.com/apartments/san-francisco-ca/1177-market-at-trinity-place/BNjvdD/"),
    ("300 Buchanan, 300 Buchanan St #202, San Francisco, CA 94102", "$2,975", "https://www.zillow.com/apartments/san-francisco-ca/300-buchanan/5XjW2N/"),
]

# Your Google Form URL
FORM_URL = "https://forms.gle/FfXqpmJY643P46qv8"

# Set up Selenium
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(), options=options)

for address, price, link in listings:
    driver.get(FORM_URL)
    time.sleep(2)  # Wait for form to load

    # Fill in Address
    driver.find_element(By.XPATH,
                        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/textarea').send_keys(address)
    # Fill in Price
    driver.find_element(By.XPATH,
                        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(price)
    # Fill in Link
    driver.find_element(By.XPATH,
                        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea').send_keys(link)
    # Submit the form
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div').click()
    time.sleep(2)  # Wait for submission to process

print("✅ All listings submitted!")
driver.quit()