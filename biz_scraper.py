from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://boards.4channel.org/biz/').text

soup = BeautifulSoup(source,'lxml')

csv_file = open('biz_scrape.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['subject','message','link'])

board = soup.find('div',class_='board')


for thread in board.find_all('div',class_='thread'):

    subject = thread.find('span',class_='subject').text

    message = thread.find('blockquote',class_="postMessage").text

    post_info = thread.find('div',class_='postInfo desktop')

    link_list = [a['href'] for a in post_info.find_all('a', href=True)][2]

    link = f'https://boards.4channel.org/biz/{link_list}'

    csv_writer.writerow([subject,message,link])
    
csv_file.close()

    # print(link)
    # print(subject)
    # print()
    # print(message)
