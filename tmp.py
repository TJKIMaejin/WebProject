from flask import Flask, render_template, request ,jsonify
import threading
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.recipe
@app.route('/') # 페이지 연결: 루트페이지
def home():
    """
    index.html 페이지 연결.
    """               
    return render_template('recipe.html')

@app.route('/api',methods=['GET']) # 페이지 연결: 루트페이지
def yun():

    list1 = list(db.recipe.find({},{'_id':0}))

    return jsonify({'result':'success', 'recipe':list1})

if __name__ == '__main__':
  app.run('0.0.0.0', port=5000, debug = True)
  #test_post()
  print("끝!")