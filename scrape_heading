import requests
from bs4 import BeautifulSoup

def scrape_headlines(url):
    try:
        # Send HTTP GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise error for unsuccessful requests
        
        # Parse HTML content
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Extract headlines
        headlines = []
        # Look for h1, h2, h3, and h4 tags for headlines
        for tag in ['h1', 'h2', 'h3', 'h4']:
            headlines.extend([headline.text.strip() for headline in soup.find_all(tag)])
        
        return headlines
    except Exception as e:
        print('Error:', e)
        return []

# Main function
def main():
    website_urls = ['https://www.bbc.com/news', 'https://www.nytimes.com/', 'https://edition.cnn.com/']
    
    for url in website_urls:
        headlines = scrape_headlines(url)
        
        if headlines:
            print('Headlines from', url, ':', headlines)
        else:
            print('No headlines scraped from', url)

main()
