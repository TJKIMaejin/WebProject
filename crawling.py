import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.recipe

# URL을 읽어서 HTML를 받아오고,

headers ={"User-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36"}

i=range(1,2)
# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
#contents_area_full > ul > ul

page = []
for a in i:

    try:
        data = requests.get('https://www.10000recipe.com/recipe/list.html?order=reco&page=' + str(a), headers=headers)
        soup = BeautifulSoup(data.text, 'html.parser')
        num = soup.find('ul', {'class': 'common_sp_list_ul ea4'})
        k=num.find_all('div',{'class':'common_sp_thumb'})
        for kk in k:
            page.append(kk.find('a')['href'])

    except:
        pass

        # if img_tag is not None:
        #     print(img_tag)
# print(page)
main_img= []
main_step=[]
main_title=[]
main_recipe=[]
main_recipe2=[]

for p in page:
    data2 = requests.get('https://www.10000recipe.com'+p,headers=headers)
    soup = BeautifulSoup(data2.text, 'html.parser')

    try:
        title = soup.select('#contents_area > div.view2_summary')
        img = soup.select_one('#contents_area > div.view2_pic > div.centeredcrop > img')
        recipe = soup.select('#divConfirmedMaterialArea > ul:nth-of-type(1) > a')
        recipe2 = soup.select('#divConfirmedMaterialArea > ul:nth-of-type(2) > a')
        step = soup.find("div", {"class": "view_step"})
        s = step.find_all("div", {"class": "media-body"})
        i = 0
        last = ""
        last_recipe1 = ""
        last_recipe2 = ""
        for a in s:
            i += 1
            last += str(i) + a.text + "&"
        last = last[:-1]



        for craw in title:
          a_tag = craw.select_one('h3')

    # a의 text를 찍어본다.
        for craw in recipe:
            a_tag = craw.find('li')
            last_recipe1 += a_tag.text.split("\n")[0] + "&"
            # print(last_recipe1)
        last_recipe1 = last_recipe1[:-1].strip()



        for craw in recipe2:
        # movie 안에 a 가 있으면,
            a_tag = craw.find('li')
            last_recipe2 += a_tag.text.split("\n")[0] + "&"
        last_recipe2 = last_recipe2[:-1]

        main_recipe2.append(last_recipe2)
        main_img.append(img['src'])
        main_step.append(last)
        main_recipe.append(last_recipe1.strip())
        main_title.append(a_tag.text)


    except:
        pass
k = range(0, len(page))


for i in k:
    doc = {
        'step': main_step[i], 'title': main_title[i], 'recipe1': main_recipe[i], 'recipe2': main_recipe2[i], 'img': main_img[i]
    }
    db.recipe.insert_one(doc)



# print(main_img)
# print(main_step)
# print(main_title)
# print(main_recipe)
# print(main_recipe2)
#






