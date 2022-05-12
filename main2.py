import time
from bs4 import BeautifulSoup
from selenium import webdriver

from requests_html import HTMLSession

base_url = 'https://www.premierleague.com/fixtures'
spec_url = 'https://www.premierleague.com/fixtures?co=1&cl='
url = 'https://servinn-8acdd.web.app'

#driver = webdriver.Chrome('/Applications/chromedriver')
#servinnweb = driver.get(url)
#time.sleep(5)

#page = driver.find_element(By.TAG_NAME, 'div')

#driver.quit()


s = HTMLSession()
ss = s.get(base_url)

ss.html.render(keep_page=True)


print(ss.html.page)
