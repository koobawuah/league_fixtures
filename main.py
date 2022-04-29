from bs4 import BeautifulSoup
import requests 

base_url = 'https://www.premierleague.com/fixtures'
spec_url = 'https://www.premierleague.com/fixtures?co=1&cl='

epl_fix_page = requests.get(base_url)
content = BeautifulSoup(epl_fix_page, 'lxml')
fixtures = content.find_all('ul', class_='matchList')

print(content)
