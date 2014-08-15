#!/usr/bin/env python
# -*- coding: utf-8 -*-

import feedparser
import time

FEED_URL = "http://oabt.org/rss.php?cid=6"


def fetchRSS(newDate):

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
		wrapRSS(newFeed)
		NEW_DATE = newFeed[0].published_parsed 

	print len(newFeed)
def wrapRSS(entry):
	pass

def compareDate(t1, t2):
	return time.mktime(t1) - time.mktime(t2) > 0

class RSSEntry:
	
	def __init__(self):
		self.title = ""
		self.link = ""
		self.date = ""
	def setTitle(self, title):
		self.title = title

	def setLink(self, link):
		self.link = link

	def setDate(self, date):
		self.date = date

if __name__ == "__main__":
	
	fetchRSS(NEW_DATE)