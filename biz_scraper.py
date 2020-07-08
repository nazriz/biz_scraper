from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://boards.4channel.org/biz/').text

soup = BeautifulSoup(source,'lxml')

board = soup.find('div',class_='board')

thread = board.find('div',class_='thread')

print(thread.prettify())
