# Zillow Automation Web Scraping Project 🏠🤖

This project automates the process of:

1. Scraping rental listings from a Zillow demo site.
2. Printing the listings in a copy-paste-ready Python list format.
3. Auto-filling a Google Form with those listings.
4. Automatically storing the submitted form data in a connected Google Sheet.

---

## 📁 Project Structure

zillow-automation/
│
├── data_scraper.py # Scrapes data and prints listings = [...] to terminal
├── form_filler.py # Uses listings to auto-fill a Google Form
├── README.md # Project documentation

yaml
Copy
Edit

---

## 🔧 How It Works

### 1. `data_scraper.py` — Web Scraper

- Scrapes listings from the Zillow Clone site:  
  [https://appbrewery.github.io/Zillow-Clone/](https://appbrewery.github.io/Zillow-Clone/)

- Uses `requests` and `BeautifulSoup` to collect:
  - 🏠 Address
  - 💵 Price
  - 🔗 Listing URL

- Outputs a ready-to-use Python list in this format:

 Usage:
bash
Copy
Edit
python data_scraper.py
Then copy the printed listings = [...] block and paste it into form_filler.py.

2. form_filler.py — Google Form Filler
Automates filling in a Google Form using the listings list.

Uses Selenium to open the form, enter data into:

Address field
Price field
Link field

(if you're manually testing it you will have to run data_scraper.py then scrape the website of zillow, Afterwards you'll have the scraped Adresses, Prices and Link from the zillow site in the format of a list called 'listings, just copy that from the terminal and paste it in form_filler's 'listings' and to fill the form, run the program, 'form
-filler.py'.)

Submits each entry individually.

Each submission is automatically recorded in a Google Sheet that’s linked to your form.

✅ Setup Your Google Form:
Create a Google Form with:

Address (Short answer)

Price (Short answer)

Link (Short answer)

Click Responses > Link to Sheets to send submissions to a spreadsheet.

✅ Usage:
Make sure you’ve pasted the listings into form_filler.py, then run:

bash
Copy
Edit
python form_filler.py
🔗 Connection Flow
sql
Copy
Edit
data_scraper.py
     ↓
 Terminal prints listings = [...]
     ↓
 Paste into form_filler.py
     ↓
 form_filler.py auto-submits to Google Form
     ↓
 Google Sheet receives data in real-time
📌 Notes
The scraper only works with the static Zillow demo site.

You must manually paste the output listings into form_filler.py.

Ensure Selenium and ChromeDriver are installed and working.

Add a delay (e.g. time.sleep(2)) between submissions if needed.

📦 Dependencies
Install dependencies with:

bash
Copy
Edit
pip install requests beautifulsoup4 selenium
Also make sure to download the correct ChromeDriver for your version of Chrome and put it in your system path.
