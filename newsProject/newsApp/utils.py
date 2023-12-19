import requests
from bs4 import BeautifulSoup


def fetch_article_details(url):
    try:
        # Send a request to the URL and get the HTML content
        response = requests.get(url)
        response.raise_for_status()

        # Parse HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract title, image, and description (modify as per your HTML structure)
        title = soup.title.text if soup.title else None
        image = soup.find('meta', property='og:image')['content'] if soup.find('meta', property='og:image') else None
        description = soup.find('meta', property='og:description')['content'] if soup.find('meta',
                                                                                           property='og:description') else None

        return title, image, description
    except Exception as e:
        # Handle exceptions (e.g., URL not reachable, parsing errors)
        print(f"Error fetching details for URL: {url}. Error: {e}")
        return None, None, None
