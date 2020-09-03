import urllib.request
import os
import sys
from urllib.parse import quote
import json
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home() :
    return render_template('recipe.html')

@app.route('/chan')
def chan_render() :
    return render_template('search.html')

@app.route('/chan1', methods=['GET'])

def chan_get():

    keyword = request.args.get("keyword")

    encText = quote(keyword)
    display = 3
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

    return jsonify({"result" : 'success', 'info' : json_data})

if __name__ == '__main__':

  app.run('0.0.0.0', port=5000, debug = True)



