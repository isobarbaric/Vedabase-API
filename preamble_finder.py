
from bs4 import BeautifulSoup
import cfscrape

# options: cfscrape, cloudscraper

class PreambleFinder:

    # figure out formatting later, moving on for now?
    def __init__(self):
        pass

    def find(self):
        scraper = cfscrape.create_scraper()  
        base_url = 'https://vedabase.io/en/library/bg/'

        # preamble class?
        preamble_path = ['setting-the-scene/', 'dedication/', 'preface/', 'introduction/']
        preamble = []

        for url in preamble_path:
            current_page = scraper.get("https://vedabase.io/en/library/bg/" + url).content 
            soup = BeautifulSoup(current_page, 'html.parser')
            page_title = soup.find('div', {'class': lambda x: x and 'r r-title r-chapter' in x}).text.strip() 

            page_content = ''
            for text_content in soup.findAll("div", {"id": "content"}):
                page_content += text_content.text + '\n'

            preamble.append([page_title, page_content])

        return preamble

# 'r r-lang-en r-chapter-title r-title'
