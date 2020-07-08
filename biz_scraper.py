from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://boards.4channel.org/biz/').text

soup = BeautifulSoup(source,'lxml')

print(soup.prettify())
