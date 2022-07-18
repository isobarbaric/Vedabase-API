
from bs4 import BeautifulSoup

a = '<dl class="r r-verse" id="bb181"><dt><a href="/en/library/bg/1/1/">TEXT 21-22:</a></dt><dd>Dhṛtarāṣṭra said: O Sañjaya, after my sons and the sons of Pāṇḍu assembled in the place of pilgrimage at Kurukṣetra, desiring to fight, what did they do?</dd></dl>'

soup = BeautifulSoup(a, 'html.parser')

word = soup.find('a').text
print(word[word.find('TEXT')+5:-1])
