#!/usr/bin/env python
# -*- coding: utf-8 -*-

Unknown = "Unknown"

class PeanutMovie:

	def __init__(self):
		self.zhtitle = ""
		self.entitle = ""
		self.year = ""
		self.rating = ""
		self.genre = ""
		self.link = ""
		self.post = ""
		self.casts = []
		self.coutry = ""
		self.summary = ""
		self.director = None
		self.ratingcount = ""
		self.castnames = ""
	def setratingcount(self, ct):
		self.ratingcount = ct

	def setSummary(self, summ):
		self.summary = summ

	def setzhTitle(self, zhtitle):
		self.zhtitle = zhtitle


	def setenTitle(self, enTitle):
		self.entitle = enTitle


	def setYear(self, year):
		self.year = year


	def setRating(self, rating):
		self.rating = rating



	def setgenre(self, genre):
		if genre is None:
			self.genre = "Unknown"
		else:
			self.genre = ",".join(genre)
		# return self

	def setCountry(self, country):
		if country is None:
			self.country = "Unknown"
		else:
			self.country = ",".join(country)
		# return self

	def setLink(self, link):
		self.link = link
		# return self

	def setPost(self, post):
		self.post = post
		# return self

	def setDirector(self, director):
		if director is None:
			self.director = Actor({"name" : Unknown, "avatars" : None,  "alt": Unknown})
		else:
			self.director = Actor(director)
		# return self

	def setActors(self, actors):
		# if names is None or enNames is None or avatars is None or links is None:
		# 	# ADD the anonymous avatar and link
		# 	self.actors.append(Actor("Unknown", "Unknown" ,"Unknown", "Unknown"))
		# else:
		# 	i = 0
		# 	while i < len(names)
		# 		self.actors.append(Actor(names[i], enNames[i], avatars[i], links[i]))
		# 		i = i + 1
		# return self
		if actors is None or len(actors) == 0:
			# ADD the anonymous avatar and link
			self.casts.append(Actor({"name" : Unknown, "avatars" : None, "alt": Unknown}))
		else:
			for actor in actors:
				self.casts.append(Actor(actor))
				self.castnames = self.castnames + "  " + actor["name"]

	def build(self):
		# ADD check procedure
		return self

class Actor():
	def __init__(self, actor):
		self.name = actor["name"]

		if actor["avatars"] is None:
			self.avatar = "./images/man.png"
		else: 
			self.avatar = actor["avatars"]["medium"]
		
		self.link = actor["alt"]
