from flask import Flask, render_template, request, jsonify

# 몽고디비에서 ObjectId 객체를 사용하기 위해서 아래 임포트
from bson import ObjectId

app = Flask(__name__)

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.recipe
db2  =client.recipe3

#희아--> 메인 페이지
@app.route('/')  # 페이지 연결: 루트페이지
def home():
    """
    index.html 페이지 연결.
    """
    return render_template('index.html')


@app.route('/yuna')  # 페이지 연결: 윤아페이지
def yun_render():
    """
    index.html 페이지 연결.
    """
    return render_template('recipe.html')


""" def yun_json(): 

    db의 list -> json

    result = list(db.recipe.find({}))
    return jsonify({'result':'success', 'result':result}) """

""" DB에서 _id값에 맞는 레시피 정보 가져오기 """


@app.route('/yuna1', methods=['GET'])
def yuna_get():
    # 클라이언트가 url에 뿌린 _id의 value 갖고오기.
    id = request.args.get("_id")
    id = ObjectId(id)

    # 클라이언트 요청과 일치하는 document 찾기 {키:밸류} --> id는 제외하고 넘겨줌.. Object 문제,, 대체 왜?? 그냥 모르자 필요 없으니까
    # .find도 안됨.. find_one만됨... 왜?? 사실 하나만 필요해서 알 필요 없음
    recipe_info = db.recipe.find_one({"_id": id}, {"_id": 0})

    return jsonify({"result": 'success', 'info': recipe_info})


""" 찬진이 검색 결과(재료)로 연결하기 """

@app.route('/hee',methods=['GET'])  # 페이지 연결: 루트페이지
def hee_get():
    """
    index.html 페이지 연결.
    """
    list1 = list(db2.recipe3.find({}, {'_id': 0}))
    list2 =list(db.recipe.find({}, {'_id': 0}))

    print(list1)

    return jsonify({'result': 'success', 'list': list1,'list2':list2})


@app.route("/chan", methods=["GET"])
def chan_get():
    # 일단 요청 결과만 리턴하자.. 구체적 내용은 추후에 작업
    ingredi = request.args.get("ingredi")
    return ingredi


if __name__ == '__main__':

  app.run('0.0.0.0', port=5000, debug = True)

