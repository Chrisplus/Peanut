#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib, urllib2
import json

IMDB_API = "http://www.omdbapi.com/?%s"
Douban_API = "http://api.douban.com/v2/movie/imdb/"



def splitLinkName(magName):
	# the mag link example
	# RV.2006.房车之旅.双语字幕.HR-HDTV.AC3.1024X576.x264.mkv【Auto】
	# Night.at.the.Museum.Battle.of.the.Smithsonian.2009.博物馆奇妙夜2.双语字幕.国英音轨.HR-HDTV.AC3.1024X576.x264.mkv【Auto】
	if magName is None:
		pass

	nameArray = magName.split('.')

	if nameArray is None or len(nameArray) <= 1:
		pass

	titleSet = ""
	year = ""
	for attr in nameArray:
		if attr.isdigit():
			year = attr
			break
		else:
			titleSet = titleSet + attr + " "
	title = titleSet.strip(" ")

	return title,year


def fetchFromIMDB(movieName, movieYear):
	# The IMDB third-party API example
	# http://www.omdbapi.com/?t=RV&y=2006
	# t is title
	# y is year
	if movieName is None or not movieName or movieYear is None or not movieYear:
		pass

	param = {}
	param.update({'t' : movieName})
	param.update({'y' : movieYear})

	requestUrl = IMDB_API % urllib.urlencode(param)
	content = urllib2.urlopen(requestUrl).read()
	return parseIMDB(content)

def fetchFromDouban(imdbNo):
	# The tmp API example
	# http://api.douban.com/v2/movie/imdb/tt0449089 
	# tt0449089 is IMDB No.
	requestUrl = Douban_API + imdbNo
	content = urllib2.urlopen(requestUrl).read()
	return parseDouban(content)

def parseIMDB(content):
	try:
		jsonData = json.loads(content)
	except ValueError:
		return -1

	rep = jsonData['Response']
	date = ""
	director = ""
	genre = ""
	plot = ""
	actors = ""
	rating = ""
	votes = ""
	movieID = ""
	if rep == "True":
		date = jsonData['Released']
		director = jsonData['Director']
		genre = jsonData['Genre']
		actors = jsonData['Actors']
		rating = jsonData['imdbRating']
		votes = jsonData['imdbVotes']
		movieID = jsonData['imdbID']
		plot = jsonData['Plot']

		return movieID, date, genre, director, actors, rating, votes, plot
	else:
		return -1

def parseDouban(content):
	try:
		jsonData = json.loads(content)
	except ValueError:
		return -1
	try:
		code = jsonData['code']
	except KeyError:
		doubanLink = jsonData['alt']
		summary = jsonData['summary']
		doubanRate = jsonData['rating']['average']
		return doubanLink, summary, doubanRate





if __name__ == "__main__":
	testName = u"Night.at.the.Museum.2006.博物馆奇妙夜.双语字幕.国英音轨.HR-HDTV.AC3.1024X552.x264.mkv【Auto】"
	title,year = splitLinkName(testName)
	movieID, date, genre, director, actors, rating, votes, plot = fetchFromIMDB(title, year)
	print movieID, date, genre, director, actors, rating, votes
	print fetchFromDouban(movieID)

