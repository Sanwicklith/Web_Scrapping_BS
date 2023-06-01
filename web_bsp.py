import requests
from bs4 import BeautifulSoup

source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')

# print(soup.prettify())
article = soup.find('article')
# print(article.prettify())
# title = article.h2.a.text
# print(f'Title: {title}')
#
# post_date = article.p.time.text
# print(f'Posted: {post_date}')
#
# author = article.span.a.span.text
# print(f'Author: {author}')
#
# summary = article.div.p.text
# print(f'Video Summary: {summary}')


for link in article.find_all('span', class_='embed-youtube'):
    video_link = link.iframe['src']

    print(video_link)


