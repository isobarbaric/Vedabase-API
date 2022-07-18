
from bs4 import BeautifulSoup
import cfscrape
import os 
import json
import shutil

class Chapter:

    def __init__(self, number, title, texts):
        self.number = number
        self.title = title
        self.texts = texts

    def __repr__(self):
        info = 'Chapter Number: ' + self.number + ', Chapter Title: ' + self.title + ', Chapter Length: ' + str(len(self.texts)) + ' texts, \n'
        for text in self.texts:
            info += text.title + ', ' + text.devanagri + ', ' + text.romanization + ', ' + text.synonyms + ', ' + text.translation + ', ' + text.purport
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

class ChapterFinder:

    def __init__(self):
        pass

    def find(self):
        scraper = cfscrape.create_scraper()  
        base_url = 'https://vedabase.io/en/library/bg/'

        if ('json' in os.listdir()):
            shutil.rmtree('json')
        os.mkdir('json')
        os.mkdir('json/gita')

        for idx in range(1, 19):
            current_path = base_url + str(idx)
            current_chapter = scraper.get(current_path).content 
            soup = BeautifulSoup(current_chapter, 'html.parser')

            current_number = soup.find('div', {'class': 'r r-title-small r-chapter'}).text.strip() 
            current_title = soup.find('div', {'class': 'r r-lang-en r-chapter-title r-title'}).text.strip() 
            
            current_texts = soup.findAll('dl', {'class': lambda x: x and 'r r-verse' in x})
            current_verses = []
            
            for i in range(len(current_texts)):
                word = current_texts[i].text
                word = word[word.find('TEXT')+5:word.find(':')]
                if word[0] == ' ':
                    word = word[1:]
                current_verses.append(word)

            current_texts = []

            for verse in current_verses:
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

                current_texts.append(Text(title, devanagri, romanization, synonyms, translation, purport))

            chapter_created = Chapter(current_number, current_title, current_texts)

            with open('json/gita/' + 'chapter_' + str(idx) + '.json', 'w') as storage:
                rn = {} 
                rn['number'] = chapter_created[-1].number
                rn['title'] = chapter_created[-1].title
                rn['verses'] = {}
                for text in chapter_created[-1].texts:
                    revised_title = text.title[text.title.rfind('.')+1:]
                    rn['verses'][revised_title] = {}
                    rn['verses'][revised_title]['title'] = text.title
                    rn['verses'][revised_title]['devanagri'] = text.devanagri
                    rn['verses'][revised_title]['romanization'] = text.romanization
                    rn['verses'][revised_title]['synonyms'] = text.synonyms
                    rn['verses'][revised_title]['translation'] = text.translation
                    rn['verses'][revised_title]['purport'] = text.purport
                json_string = json.dumps(rn, indent=4)
                storage.write(json_string)

# variable names are super confusing
