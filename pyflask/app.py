from flask import Flask, render_template, request, jsonify, url_for
import urllib.request
import os
import sys
from urllib.parse import quote
import json
app = Flask(__name__)

@app.route('/')
def home():
  return render_template('pop - 복사본.html')
    
@app.route('/call', method = ['GET'])
def call(char) :
        char = request.args_encodingsargs.get('char')
        encText = quote(request.args.get('char'))
        display = 10
        url = "https://openapi.naver.com/v1/search/shop?query=" + encText + "&display=" + str(display) + "&start=1" + "&sort=sim"
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id","oXfhI4we88tBhBs1hxY_")
        request.add_header("X-Naver-Client-Secret","mruETz2SMm")
        response = urllib.request.urlopen(request)
        rescode=response.getcode()
    #    json_really_data = []
        if(rescode == 200):
            response_body = response.read()
            middle_data = json.loads(response_body)
            json_data = middle_data['items']
        else:
            print("Error code:"+rescode)
        ## 넘겨받은 값을 원래 페이지로 리다이렉트
        return json_data
    
if __name__ == '__main__':
    app.run(debug=True, threaded=True)