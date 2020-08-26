import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.recipe3

headers ={"User-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36"}

i=range(1,11)
page=[]
recipe=[]
for a in i:

    try:
        data = requests.get('https://www.10000recipe.com/bbs/list.html?bid=3&cid=2&page=' + str(a), headers=headers)
        soup = BeautifulSoup(data.text, 'html.parser')
        num = soup.find('div', {'class': 'info_list'})
        k=num.find_all('div',{'class':'media'})


        for kk in k:
            page.append(kk.find('a')['href'])
            # (recipe.append(kk.find('a').text))





    except:
        pass
name=[]
category=[]
# print(page)

for p in page:
    data2 = requests.get('https://www.10000recipe.com'+p,headers=headers)
    soup = BeautifulSoup(data2.text, 'html.parser')
    try:
        name1 =soup.select('#contents_area')
        cate =soup.find("dl",{"class":"recipe_cont"}).find_all("td")[2]

        category.append(cate.text)

        for craw in name1:
            a_tag =craw.select_one('#contents_area > div>h2')



        name.append(a_tag.text)



    except:
        pass

k= range(0,len(page))
for i in k:
    doc = {
        'name': name[i],
        'category':category[i]
    }
    db.recipe3.insert_one(doc)