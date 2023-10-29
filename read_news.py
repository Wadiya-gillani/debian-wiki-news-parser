import requests
from bs4 import BeautifulSoup

# URL of the Debian Wiki News page
wiki_url = 'https://wiki.debian.org/'

# Function to fetch and parse the content
def fetch_and_parse_wiki_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad requests
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

# Function to extract and write content in Markdown format
def write_to_markdown(soup):
    if soup:
        try:
            with open('debian_news.md', 'w', encoding='utf-8') as file:
                # Find all paragraphs within the content
                paragraphs = soup.find_all('p')
                for paragraph in paragraphs:
                    # Write the text of each paragraph to the Markdown file
                    file.write(paragraph.get_text(strip=True) + '\n\n')
            print("Content has been extracted and saved to 'debian_news.md'.")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Error: Unable to fetch and parse the Debian Wiki page.")

# Main function
def main():
    soup = fetch_and_parse_wiki_page(wiki_url)
    write_to_markdown(soup)

if __name__ == "__main__":
    main()
