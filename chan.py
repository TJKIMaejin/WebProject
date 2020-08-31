import urllib.request
import os
import sys
from urllib.parse import quote
import json

# 네이버 api call
def call(keyword):
#    checkstr = keyword
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
    return json_data

list=[]
list = call("양파")
print(list)


#list = []
#    list = json_data
#    food_data = []
#    for i in range (0,display) :
#        if ( list[i]['category4'] == checkstr ) :
#            food_data.append(list[i])
