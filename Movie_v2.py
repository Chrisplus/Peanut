#!/usr/bin/env python
# -*- coding: utf-8 -*-


DOUBAN_API = "https://api.douban.com"
DOUBAN_SEARCH = "/v2/movie/search?%s"

import urllib, urllib2
import json

def splitLinkName(magName):
	# the mag link example
	# RV.2006.房车之旅.双语字幕.HR-HDTV.AC3.1024X576.x264.mkv【Auto】
	# Night.at.the.Museum.Battle.of.the.Smithsonian.2009.博物馆奇妙夜2.双语字幕.国英音轨.HR-HDTV.AC3.1024X576.x264.mkv【Auto】
	if magName is None:
		return None

	nameArray = magName.split('.')

	if nameArray is None or len(nameArray) <= 1:
		None

	titleSet = ""
	year = ""
	splitspot = 0
	zhTitle = ""
	for attr in nameArray:
		if attr.isdigit():
			year = attr
			zhTitle = nameArray[splitspot + 1]
			break
		else:
			titleSet = titleSet + attr + " "
		splitspot = splitspot + 1

	title = titleSet.strip(" ")
	zhTitle = zhTitle.strip(" ")
	return zhTitle,title,year 

def searchFromDouban(zhTitle, title, year):
	if zhTitle is None or title is None or year is None:
		return None
	
	param = {}
	param.update({'q' : zhTitle})

	requestUrl = (DOUBAN_API + DOUBAN_SEARCH) % urllib.urlencode(param)
	content = urllib2.urlopen(requestUrl).read()
	return parseDouban_v2(content)

def parseDouban_v2(content):
	try:
		jsonData = json.loads(content)
	except ValueError:
		return None

	total = jsonData["total"]

	return total, total, total


def searchHelper(rawTitle):
	res = splitLinkName(rawTitle)

	if res is None:
		print None
	else:
		zhTitle, title, year = res
		print zhTitle, title, year
	# return searchFromDouban(zhTitle,title,year)

if __name__ == "__main__":

	# testName = u "Night.at.the.Museum.2006.丛林二.双语字幕.国英音轨.HR-HDTV.AC3.1024X552.x264.mkv【Auto】"
	testName = "Night.at.the.Museum.2006.博物馆奇妙夜.双语字幕.国英音轨.HR-HDTV.AC3.1024X552.x264.mkv【Auto】"
	# testName = None
	searchHelper(testName)
	# print zhTitle, title, year




