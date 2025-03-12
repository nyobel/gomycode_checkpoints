# import libraries
import requests
from bs4 import BeautifulSoup

# Fetch and parse HTML content from url
def get_html(url):
    page = requests.get(url)

    if page.status_code == 200:
        #parsing
        soup = BeautifulSoup(page.content, 'html.parser')
        return soup
    else:
        print('Error fetching page:', page.status_code)
        return None
    

# Extract article title from BeautifulSoup
def get_title(soup):
    title_tag = soup.find('h1', id = 'firstHeading')
    return title_tag.text.strip() if title_tag else 'Title not found'


# Extract article title text for each paragraph with their respective headings
# Map headings to their respective paragraphs in the dictionary
def get_article_text(soup):
    """
    Extracts article text by grouping paragraphs under their respective headings.
    For headings, this function first attempts to find a <span> with class "mw-headline".
    If not found, it falls back to using the text directly from the <h2> tag.
    
    Returns a dictionary where keys are section headings and values are lists of paragraph texts.
    """
    content = {}
    content_div = soup.find('div', id='mw-content-text')
    if not content_div:
        return content

    current_heading = "Introduction"
    content[current_heading] = []

    # Loop through all <h2> and <p> elements within the content division.
    # Using recursive=True to capture all such elements in order.
    for element in content_div.find_all(['h2', 'p']):
        if element.name == 'h2':
            # Try to find the heading text within a span first.
            span = element.find('span', class_='mw-headline')
            if span:
                current_heading = span.text.strip()
            else:
                current_heading = element.text.strip()
            content[current_heading] = []
        elif element.name == 'p':
            paragraph = element.get_text().strip()
            if paragraph:
                content[current_heading].append(paragraph)
    return content



# Collect links that redirect to other wikipedia pages
def get_internal_links(soup):
    links = []
    for a in soup.find_all('a', href=True):
        href = a['href']
        if href.startswith("/wiki/") and ":" not in href:
            full_url = "https://en.wikipedia.org" + href
            links.append(full_url)
    return links
    

# Combining all steps
def scrape_wikipedia(url):
    soup = get_html(url)
    if soup is None:
        return None
    
    title = get_title(soup)
    article_text = get_article_text(soup)
    internal_links = get_internal_links(soup)

    return{
        "title": title,
        "article_text": article_text,
        "internal_links": internal_links
    }


# Main function
if __name__ == "__main__":
    # Define url for testing
    url = "https://en.wikipedia.org/wiki/Limbic_system"
    result = scrape_wikipedia(url)

    if result:
        print("Title:", result["title"])
        print("\nArticle Sections and Paragraphs:")
        for section, paragraphs in result["article_text"].items():
            print(f"\n{section}:")
            for para in paragraphs:
                print("  -", para)
        print("\nFirst 10 Internal Links:")
        for link in result["internal_links"][:10]:
            print(link)