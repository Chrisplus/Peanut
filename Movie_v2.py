#!/usr/bin/env python
# -*- coding: utf-8 -*-


DOUBAN_API = "https://api.douban.com"
DOUBAN_SEARCH = "/v2/movie/search?%s"
DOUBAN_DETAIL = "/v2/movie/subject/"

import urllib, urllib2
import json
from PeanutMovie import PeanutMovie

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
	return parseDouban_v2(content, year)

def parseDouban_v2(content, year):
	try:
		jsonData = json.loads(content)
	except ValueError:
		return None

	total = jsonData["total"]

	if total <= 0:
		return None
	
	# Find the right one
	correlated = None
	for can in jsonData["subjects"]:
		if can["year"] == year:
			correlated = can
			break

	cont = urllib2.urlopen(DOUBAN_API + DOUBAN_DETAIL + correlated["id"]).read()
	try:
		jd = json.loads(cont)
	except ValueError:
		return None

	peanut = PeanutMovie()

	peanut.setzhTitle(jd["title"])
	peanut.setenTitle(jd["original_title"])
	peanut.setYear(jd["year"])
	peanut.setRating(jd["rating"]["average"])

	peanut.setgenre(jd["genres"])
	peanut.setLink(jd["alt"])
	peanut.setPost(jd["images"]["large"])

	direcor = jd["directors"][0]
	peanut.setDirector(direcor)
	peanut.setActors(jd["casts"])
	peanut.setCountry(jd["countries"])
	peanut.setSummary(jd["summary"])
	peanut.setratingcount(jd["ratings_count"])

	return peanut


def searchHelper(rawTitle):
	res = splitLinkName(rawTitle)

	if res is None:
		return None

	zhTitle,title,year = res
	peanut = searchFromDouban(zhTitle, title, year)

	return peanut

	# print peanut.entitle
	# print peanut.rating
	# print peanut.director.link

	# for actor in peanut.casts:
	# 	print actor.avatar

	# xml = RSSUtil.wrapRSS(peanuts)
	# return xml



# if __name__ == "__main__":

# 	# testName = u "Night.at.the.Museum.2006.丛林二.双语字幕.国英音轨.HR-HDTV.AC3.1024X552.x264.mkv【Auto】"
# 	testName = "Night.at.the.Museum.2006.博物馆奇妙夜.双语字幕.国英音轨.HR-HDTV.AC3.1024X552.x264.mkv【Auto】"
# 	# testName = None
# 	res = searchHelper(testName)
# 	# print zhTitle, title, year






			
			