from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://boards.4channel.org/biz/').text

soup = BeautifulSoup(source,'lxml')

board = soup.find('div',class_='board')

thread = board.find('div',class_='thread')

subject = thread.find('span',class_='subject').text

message = thread.find('blockquote',class_="postMessage").text

print(subject)
print()
print(message)

# print(thread.prettify())
