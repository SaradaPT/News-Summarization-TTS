import requests
from bs4 import BeautifulSoup

company_name = "Tesla"  # Example input
search_url = f"https://news.google.com/search?q={company_name}&hl=en-IN&gl=IN&ceid=IN:en" 

headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(search_url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

print("🔍 Debugging Google News Structure...\n")

for item in soup.find_all('div', class_='xrnccd')[:5]:  # ✅ Print first 5 articles
    title_tag = item.find('h3')
    summary_tag = item.find('span', class_='xBbh9')

    print("Title:", title_tag.text if title_tag else "No Title Found")
    print("Summary:", summary_tag.text if summary_tag else "No Summary Found")
    print("---")
