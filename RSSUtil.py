#!/usr/bin/env python
# -*- coding: utf-8 -*-

import feedparser
from feedformatter import Feed as FeedFormatter
import time
import os
import jinja2
import MovieUtil

FEED_URL = "http://oabt.org/rss.php?cid=6"

PEANUT_TITLE = "Peanut Movie RSS"
PEANUT_URL = os.environ['HTTP_HOST'] + "/rss.xml"
PEANUT_AUTHOR = "Chrisplus"
PEANUT_DESCRIPTION = ""

PEANUT_UNKNOW = "Sorry, Peanut cannot find this movie"

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def fetchRSS(ref, newDate):

	print PEANUT_URL

	btFeeder = feedparser.parse(FEED_URL)

	if btFeeder.entries is None or len(btFeeder.entries) == 0:
		pass

	newFeed = []
	for entry in btFeeder.entries:
		# Check if the feeds are needed
		if compareDate(entry.published_parsed, newDate):
			newFeed.append(entry)
		else:
			break

	if newFeed is not None and len(newFeed) > 0:
		return wrapRSS(newFeed), newFeed[0].published_parsed
	else:
		return None, newDate

def wrapRSS(entries):
	newFeed = initFeed()

	for entry in entries:
		item = {}
		item["title"] = entry.title
		item["link"] = entry.link
		item["pubDate"] = time.localtime()
		item["guid"] = str(hash(entry.title))
		item["description"] = render(entry.title)
		newFeed.items.append(item)

	return newFeed.format_rss2_string()

def compareDate(t1, t2):
	return time.mktime(t1) - time.mktime(t2) > 0

def initFeed():
	newFeed = FeedFormatter()
	newFeed.feed['title'] = PEANUT_TITLE
	newFeed.feed["link"] = PEANUT_URL
	newFeed.feed["author"] = PEANUT_AUTHOR
	newFeed.feed["description"] = PEANUT_DESCRIPTION
	return newFeed

def render(title):
	realTitle,year, zhTitle = MovieUtil.splitLinkName(title)

	movieInfo = MovieUtil.fetchFromIMDB(realTitle, year)

	if len(movieInfo) > 1:
		movieID, date, genre, director, actors, rating, votes, plot = MovieUtil.fetchFromIMDB(realTitle, year)
		doubanLink, summary, doubanRate = MovieUtil.fetchFromDouban(movieID)
	else:
		movieID, date, genre, director, actors, rating, votes, plot,doubanLink, summary, doubanRate = [PEANUT_UNKNOW] * 11

	template_values = {
		'movietitle' : zhTitle + "\t" + realTitle + "\t" + year,
		'genre' : genre,
		'date' : date,
		'director' : director,
		'actors' : actors,
		'imdbRating' : rating,
		'doubanRating' : doubanRate,
		'imdbLink' : movieID,
		'doubanLink' : doubanLink,
		'summary' : summary}

	template = JINJA_ENVIRONMENT.get_template('description.html')
	return template.render(template_values)



if __name__ == "__main__":
	NEW_DATE = time.strptime("15 AUG 14", "%d %b %y") 
	fetchRSS(NEW_DATE)