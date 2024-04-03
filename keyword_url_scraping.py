import requests
from bs4 import BeautifulSoup

def search_websites(website_urls, keywords):
    matching_urls = []

    for url in website_urls:
        try:
            # Send HTTP GET request to the URL
            response = requests.get(url)
            response.raise_for_status()  # Raise error for unsuccessful requests

            # Parse HTML content
            soup = BeautifulSoup(response.content, "html.parser")

            # Check if any of the keywords are present in the HTML content
            for keyword in keywords:
                if keyword.lower() in soup.get_text().lower():
                    matching_urls.append(url)
                    break  # Stop searching if any keyword is found
        except Exception as e:
            print('Error while searching', url, ':', e)

    return matching_urls

def main():
    website_urls = ['https://www.bbc.com/news', 'https://www.nytimes.com/', 'https://edition.cnn.com/']

    # Get keywords input from the user
    keywords_input = input("Enter keywords separated by commas or spaces: ")
    keywords = [keyword.strip() for keyword in keywords_input.split(',')]

    matching_urls = search_websites(website_urls, keywords)

    if matching_urls:
        print('Matching URLs:')
        for url in matching_urls:
            print(url)
    else:
        print('No matching URLs found.')

main()
