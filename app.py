from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.recipe3                      # 'recipe3'라는 이름의 db를 만듭니다.
db2 = client.recipe


@app.route('/')
def home():
  return render_template('index.html')


@app.route('/orders', methods=['GET'])
def view_orders():

   list1 = list(db2.recipe.find({}, {'_id': 0}))
   list2 = list(db.recipe3.find({}, {'_id': 0}))
   return jsonify({'result': 'success', 'recipe3': list2, 'recipe': list1})


if __name__ == '__main__':
  app.run('0.0.0.0', port=5000, debug=True)
  #test_post()
  print("끝!")
