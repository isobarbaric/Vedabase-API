
from bs4 import BeautifulSoup
import cfscrape

# options: cfscrape, cloudscraper

class Chapter:

    def __init__(self, number, title, texts):
        self.number = number
        self.title = title
        self.texts = texts

    def __repr__(self):
        return 'Chapter Number: ' + self.number + ', Chapter Title: ' + self.title + ', Chapter Length: ' + str(len(self.texts)) + ' texts'

class Text:

    def __init__(self, title, devanagri, romanization, synonyms, translation, purport):
        self.title = title
        self.devanagri = devanagri
        self.romanization = romanization
        self.synonyms = synonyms
        self.translation = translation
        self.purport = purport

scraper = cfscrape.create_scraper()  
base_url = 'https://vedabase.io/en/library/bg/'

content = []

for chapter_number in range(1, 19):
    current_path = "https://vedabase.io/en/library/bg/" + str(chapter_number)
    current_chapter = scraper.get(current_path).content 
    soup = BeautifulSoup(current_chapter, 'html.parser')

    chapter_number = soup.find('div', {'class': 'r r-title-small r-chapter'}).text.strip() 
    chapter_title = soup.find('div', {'class': 'r r-lang-en r-chapter-title r-title'}).text.strip() 

    chapter_texts = []
    # for text_content in soup.findAll("div", {"id": "content"}):
    #     page_content += text_content.text + '\n'

    content.append(Chapter(chapter_number, chapter_title, chapter_texts))

for chapter in content:
    print(chapter)

# chapter number, title, each text

# hardcode chapter lengths for now, come back later with a smarter way
