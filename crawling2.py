import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.recipe3

headers ={"User-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36"}

i=range(1,11)
recipe=[]
for a in i:

    try:
        data = requests.get('https://www.10000recipe.com/bbs/list.html?bid=3&cid=2&page=' + str(a), headers=headers)
        soup = BeautifulSoup(data.text, 'html.parser')
        num = soup.find('div', {'class': 'info_list'})

        k=num.find_all('h4',{'class':'media-heading'})
        for kk in k:
            (recipe.append(kk.find('a').text))





    except:
        pass

print(recipe)
k = range(0, len(recipe))

for i in k:
    doc = {
        'recipe': recipe[i]
    }
    db.recipe3.insert_one(doc)