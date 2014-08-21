#!/usr/bin/env python
# -*- coding: utf-8 -*-

class PeanutMovie:

	def __init__(self):
		self.zhtitle = ""
		self.entitle = ""
		self.year = ""
		self.rating = ""
		self.genre = ""
		self.link = ""
		self.post = ""
		director = None
		actors = []

	def setzhTitle(self, zhtitle):
		self.zhtitle = zhtitle
		return self

	def setenTitle(self, enTitle):
		self.entitle = entitle
		return self

	def setYear(self, year):
		self.year = year
		return self

	def setRating(self, rating):
		self.rating = rating
		return self

	def setgenre(self, genre):
		if genre is None:
			self.genre = "Unknown"
		else:
			self.genre = ",".join(genre)
		return self

	def setLink(self, link):
		self.link = link
		return self

	def setPost(self, post):
		self.post = post
		return self

	def setDirecotr(self, name, enName, avatar, link):
		self.director = Actor(name, enName, avatar, link)
		return self

	def setActors(self, names, enNames, avatars, links):
		if names is None or enNames is None or avatars is None or links is None:
			# ADD the anonymous avatar and link
			self.actors.append(Actor("Unknown", "Unknown" ,"Unknown", "Unknown"))
		else:
			i = 0
			while i < len(names)
				self.actors.append(Actor(names[i], enNames[i], avatars[i], links[i]))
				i = i + 1
		return self

	def build(self):
		# ADD check procedure
		return self
		
class Actor():
	def __init__(self, name, enName, avatar, link):
		self.name = name
		self.enName = enName
		self.avatar = avatar
		self.link = link
