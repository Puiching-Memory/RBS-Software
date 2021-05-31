#!/usr/bin/python
# encoding:utf-8
 
import urllib2, json, urllib
 
 
data = {}
data["appkey"] = "your_appkey_here"
data["month"] = 1
data["day"] = 2
 
url_values = urllib.urlencode(data)
url = "https://api + jisuapi + com/todayhistory/query" + "?" + url_values
request = urllib2.Request(url)
result = urllib2.urlopen(request)
jsonarr = json.loads(result.read())
 
if jsonarr["status"] != u"0":
    print jsonarr["msg"]
    exit()
result = jsonarr["result"]
for val in result:
    print val["year"] + "年 " +  val["month"] + "月 " +  val["day"] + "日 " +  val["title"] + " " +  val["content"]