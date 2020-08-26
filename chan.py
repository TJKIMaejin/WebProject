import urllib.request
import os
import sys
from urllib.parse import quote
from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
 
# 네이버 api call
def call(keyword, start):
    encText = quote(keyword)
    url = "https://openapi.naver.com/v1/search/shop?query=" + encText + "&display=10" + "&start=" + str(start) + "&sort=sim"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id","oXfhI4we88tBhBs1hxY_")
    request.add_header("X-Naver-Client-Secret","mruETz2SMm")
    response = urllib.request.urlopen(request)
    rescode=response.getcode()
    list1=[]
    if(rescode == 200):
        response_body = response.read()
        list1.append(response_body.decode('utf-8'))
        print(response_body.decode('utf-8'))
    else:
        print("Error code:"+rescode)
    return rescode
    return list1

def get10results(keyword):
    list = []
    for num in range(0,10):
        list = list + call(keyword, 1)['items'] # list 안에 키값이 ’item’인 애들만 넣기
    return list

import json
 
list = []
result = get10results("양파")

list = list + result