import requests
from bs4 import BeautifulSoup

# Passing in our html using a file

with open('test.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')
# print(soup.prettify())
for article in soup.find_all('div', class_='article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.p.text
    print(summary)

    print()

