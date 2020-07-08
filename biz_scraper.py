from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://boards.4channel.org/biz/').text

soup = BeautifulSoup(source,'lxml')

board = soup.find('div',class_='board')


for thread in board.find_all('div',class_='thread'):

    subject = thread.find('span',class_='subject').text

    message = thread.find('blockquote',class_="postMessage").text

    post_info = thread.find('div',class_='postInfo desktop')

    link_list = [a['href'] for a in post_info.find_all('a', href=True)][2]

    print(link_list)


    # print(subject)
    # print()
    # print(message)
