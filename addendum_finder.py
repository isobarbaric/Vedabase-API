
from bs4 import BeautifulSoup
import cfscrape

class PreambleFinder:

    # figure out formatting later, moving on for now?
    def __init__(self):
        pass

    def find(self):
        scraper = cfscrape.create_scraper()  
        base_url = 'https://vedabase.io/en/library/bg/'

        preamble_path = ['setting-the-scene/', 'dedication/', 'preface/', 'introduction/']
        preamble = dict()

        for url in preamble_path:
            current_page = scraper.get(base_url + url).content 
            soup = BeautifulSoup(current_page, 'html.parser')
            page_title = soup.find('div', {'class': lambda x: x and 'r r-title r-chapter' in x}).text.strip() 

            page_content = ''
            for text_content in soup.findAll("div", {"id": "content"}):
                page_content += text_content.text + '\n'

            preamble[url[:-1]] = [page_title, page_content]

        return preamble

class EpilogueFinder:

    def __init__(self):
        pass

    def find(self):
        scraper = cfscrape.create_scraper()  
        url = 'https://vedabase.io/en/library/bg/note-2nd-edition'

        current_page = scraper.get(url).content 
        soup = BeautifulSoup(current_page, 'html.parser')
        page_title = soup.find('div', {'class': lambda x: x and 'r r-title r-chapter' in x}).text.strip() 

        page_content = ''
        for text_content in soup.findAll("div", {"id": "content"}):
            page_content += text_content.text + '\n'

        epilogue = dict()
        epilogue['note-2nd-edition'] = page_content

        return epilogue