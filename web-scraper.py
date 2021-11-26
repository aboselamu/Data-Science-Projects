# import pandas as pd
from bs4 import BeautifulSoup
import requests
url = 'http://.html'
data = requests.get(url)
my_data = []

html = BeautifulSoup(data.text, 'html.parser')
articles = html.select('a.post-card')

for article in articles:

    title = article.select('.card-title')[0].get_text()
    excerpt = article.select('.card-text')[0].get_text()
    pub_date = article.select('.card-footer small')[0].get_text()

    my_data.append({"title": title, "excerpt": excerpt, "pub_date": pub_date})
# data
print(data)
