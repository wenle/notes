#!/usr/bin/env python

import urllib
import urllib2
import os
import os.path

def downloadPage(path, fileName, url, params):
    data = urllib.urlencode(params)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    filePath = os.path.join(path, fileName)
    with open(filePath, "w") as f:
        f.write(response.read())

def downloadFirstPage():
    url = "http://beijinglawyers.chinalawinfo.com/case/Result.asp?SFlag=11"
    values = {"Para1Type" : "1", "HidPara5IDs" : "11,13", "otherPara6":"0401", "Range" : "1", "doSearch.x" : "41", "doSearch.y" : "10"}
    downloadPage("/Users/baowl/Documents/cases", "1.html", url, values);
	
downloadFirstPage();
	


#url = "http://beijinglawyers.chinalawinfo.com/case/Result.asp?SFlag=11"
#values = {"Para1Type" : "1", "HidPara5IDs" : "11,13", "otherPara6":"0401", "Range" : "1", "doSearch.x" : "41", "doSearch.y" : "10"}
#url = "http://beijinglawyers.chinalawinfo.com/case/Result.asp?SFlag=13&Para1Type=1&DispLeft=0&DispWord=&CheckFlag=0&KeyWord="
#values = {"page" : "10", "PageSelect" : "9", "preWhere" : "48%28%7C7B%522B%3D%25%23%30%30%32%25%23%25%2C%25%23%30%30%33%25%23%25%2C%25%23%30%30%34%25%23%25%29%20%41%4E%44%20%28%28%6570%636E%6765%6E90%3D%25%23%62%30%32%37%23%25%29%20%4F%52%20%28%6570%636E%6765%6E90%3D%25%23%62%30%32%38%23%25%29%29"}
#data = urllib.urlencode(values)
#print data
#req = urllib2.Request(url, data)
#response = urllib2.urlopen(req)
#the_page = response.read()
#print the_page
