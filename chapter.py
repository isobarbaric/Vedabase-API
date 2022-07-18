
from bs4 import BeautifulSoup
import cfscrape

# options: cfscrape, cloudscraper

class Chapter:

    def __init__(self, number, title, texts):
        self.number = number
        self.title = title
        self.texts = texts

    def __repr__(self):
        info = 'Chapter Number: ' + self.number + ', Chapter Title: ' + self.title + ', Chapter Length: ' + str(len(self.texts)) + ' texts, \n'
        for text in self.texts:
            info += text.title + ', '
        return info[:-1]

class Text:

    def __init__(self, title, devanagri, romanization, synonyms, translation, purport):
        self.title = title
        self.devanagri = devanagri
        self.romanization = romanization
        self.synonyms = synonyms
        self.translation = translation
        self.purport = purport

    def __repr__(self):
        return self.title

scraper = cfscrape.create_scraper()  
base_url = 'https://vedabase.io/en/library/bg/'

content = []

for current_number in range(1, 19):
    current_path = "https://vedabase.io/en/library/bg/" + str(current_number)
    current_chapter = scraper.get(current_path).content 
    soup = BeautifulSoup(current_chapter, 'html.parser')

    chapter_number = soup.find('div', {'class': 'r r-title-small r-chapter'}).text.strip() 
    chapter_title = soup.find('div', {'class': 'r r-lang-en r-chapter-title r-title'}).text.strip() 
    
    texts = soup.findAll('dl', {'class': lambda x: x and 'r r-verse' in x})
    verse_numbers = []
    
    for i in range(len(texts)):
        word = texts[i].text
        word = word[word.find('TEXT')+5:word.find(':')]
        if word[0] == ' ':
            word = word[1:]
        verse_numbers.append(word)

    chapter_texts = []

    for verse in verse_numbers:
        current_text = scraper.get(current_path + '/' + verse + '/').content
        local_soup = BeautifulSoup(current_text, 'html.parser')
        title = local_soup.find('div', {'class': 'r r-title r-verse'}).text.strip()
        devanagri = local_soup.find('div', {'class': 'wrapper-devanagari'}).text.strip()
        romanization = local_soup.find('div', {'class': 'wrapper-verse-text'}).text.strip()
        synonyms = local_soup.find('div', {'class': 'wrapper-synonyms'}).text.strip()
        translation = local_soup.find('div', {'class': 'wrapper-translation'}).text.strip()
        
        purport = '' 
        if local_soup.find('div', {'class': 'wrapper-puport'}) is not None:
            purport = local_soup.find('div', {'class': 'wrapper-puport'}).text.strip()

        chapter_texts.append(Text(title, devanagri, romanization, synonyms, translation, purport))

    content.append(Chapter(chapter_number, chapter_title, chapter_texts))

for chapter in content:
    print(chapter)

# chapter number, title, each text

# hardcode chapter lengths for now, come back later with a smarter way

# variable names are super confusing
