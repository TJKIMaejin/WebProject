from flask import Flask, render_template, request
import threading
app = Flask(__name__)

@app.route('/') # 페이지 연결: 루트페이지


def home():
    """
    index.html 페이지 연결.
    """
    return render_template('index.html')

@app.route('/test', methods=['POST'])
def test_post():
    """ 
    recipe.html 페이지에서 타이틀(title) 값 요청.
    """
    title_receive = request.form['title']
    print(title_receive)
    return jsonify({'result':'success', 'msg': '이 요청은 POST!'})


@app.route('/test', methods=['GET'])
def test_get():
    title_receive = request.args.get('title')
    print(title_receive)
    return jsonify({'result':'success', 'msg': '이 요청은 GET!'})


if __name__ == '__main__':
  app.run('0.0.0.0', port=5000, debug = True)
  #test_post()
  print("끝!")
