from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
from flask import Flask, render_template, request, jsonify

from bson import ObjectId

import urllib.request
import os
import sys
from urllib.parse import quote
import json

app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.recipe3                      # 'recipe3'라는 이름의 db를 만듭니다.
db2 = client.recipe

def objectIdDecoder(list):
  results=[]
  for document in list:
    document['_id'] = str(document['_id'])
    results.append(document)
  return results

@app.route('/')
def home():
  return render_template('index.html')




@app.route('/yuna')  # 페이지 연결: 윤아페이지
def yun_render():
    """
    index.html 페이지 연결.
    """
    return render_template('recipe.html')




@app.route('/orders', methods=['GET'])
def view_orders():
  # yun: 전체 db 반환
   list1 = objectIdDecoder(list(db2.recipe.find({}))) # yun: 재료, 이미지, 과정, ...
   list2 = objectIdDecoder(list(db.recipe3.find({}))) # yun: 재료 설명 --> 이거 안쓰니까 안받아도 될거같은데?
   return jsonify({'result': 'success', 'recipe3': list2, 'recipe': list1}) # yun: recipe은 재료, 이미지, 과정등을 담고있음 "recipe": {image, recipe_main, ...}, {} 이런 형식



@app.route('/yuna1', methods=['GET'])
def yuna_get():
    # 클라이언트가 url에 뿌린 _id의 value 갖고오기.
    id = request.args.get("_id")
    id = ObjectId(id)

    # 클라이언트 요청과 일치하는 document 찾기 {키:밸류} --> id는 제외하고 넘겨줌.. Object 문제,, 대체 왜?? 그냥 모르자 필요 없으니까
    # .find도 안됨.. find_one만됨... 왜?? 사실 하나만 필요해서 알 필요 없음
    recipe_info = db2.recipe.find_one({"_id": id}, {"_id": 0})

    return jsonify({"result": 'success', 'info': recipe_info})

@app.route('/chan')
def chan_render() :
    return render_template('search.html')

@app.route("/chan1", methods=["GET"])
def chan_get():
    # 일단 요청 결과만 리턴하자.. 구체적 내용은 추후에 작업
    indgred = request.args.get("ingredi")
    keyword = str(indgred)
    encText = quote(keyword)
    display = 3
    url = "https://openapi.naver.com/v1/search/shop?query=" + encText + "&display=" + str(display) + "&start=1" + "&sort=sim"
    request1 = urllib.request.Request(url)
    request1.add_header("X-Naver-Client-Id","oXfhI4we88tBhBs1hxY_")
    request1.add_header("X-Naver-Client-Secret","mruETz2SMm")
    response = urllib.request.urlopen(request1)
    rescode=response.getcode()
#    json_really_data = []
    if(rescode == 200):
        response_body = response.read()
        middle_data = json.loads(response_body)
        json_data = middle_data['items']
    else:
        print("Error code:"+rescode)

    return jsonify({"result" : 'success', 'info' : json_data})



if __name__ == '__main__':
  app.run('0.0.0.0', port=5000, debug=True)
  #test_post()
  print("끝!")