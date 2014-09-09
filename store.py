#!/usr/bin/env python
# -*- coding: utf-8 -*-

from google.appengine.ext import ndb
import datetime

RSS_NAME = "lasted_rss"

class RSSEntry(ndb.Model):
	date = ndb.DateTimeProperty(auto_now_add=True)
	ct = ndb.StringProperty()
	parent = ndb.KeyProperty()

	@classmethod
	def query(cls, ancestor_key):
		return cls.query(ancestor=ancestor_key).order(-cls.date)

def store(rss):
	entry = RSSEntry(parent=ndb.Key("id", RSS_NAME),
                        ct = rss)
	entry.put()

def query():
	ancestor_key = ndb.Key("id", RSS_NAME)
	rssEntries = RSSEntry.query(ancestor_key).fetch(1)
	if len(rssEntries) == 1:
		return rssEntries[0].ct