from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.apple.com/shop/refurbished/ipad/ipad').text
# print(html_text)
soup = BeautifulSoup(html_text, 'lxml')
ipads = soup.find_all('h3')
print(ipads)
# print(soup.prettify())
