from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
from flask import Flask, render_template, request, jsonify

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


@app.route('/orders', methods=['GET'])
def view_orders():
  # yun: 전체 db 반환
   list1 = objectIdDecoder(list(db2.recipe.find({}))) # yun: 재료, 이미지, 과정, ...
   list2 = objectIdDecoder(list(db.recipe3.find({}))) # yun: 재료 설명 --> 이거 안쓰니까 안받아도 될거같은데?
   return jsonify({'result': 'success', 'recipe3': list2, 'recipe': list1}) # yun: recipe은 재료, 이미지, 과정등을 담고있음 "recipe": {image, recipe_main, ...}, {} 이런 형식


if __name__ == '__main__':
  app.run('0.0.0.0', port=5000, debug=True)
  #test_post()
  print("끝!")
