from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.apple.com/shop/refurbished/ipad/ipad').text
print(html_text)
