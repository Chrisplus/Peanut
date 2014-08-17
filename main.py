#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import RSSUtil
import time
import logging


class MainHandler(webapp2.RequestHandler):

	def __init__(self, request, response):
		# Init system date
		#self.NEW_DATE = time.localtime()
		self.initialize(request, response)
		self.NEW_DATE = time.strptime("17 AUG 14", "%d %b %y")
		self.rss = None

	def get(self):
		self.rss, self.NEW_DATE = RSSUtil.fetchRSS(self.request.url, self.NEW_DATE)
		self.response.headers['Content-Type'] = 'text/xml'
		self.response.write(self.rss)
		logging.info("Response Successfully\t" + "Set New Date to " + time.strftime("%a, %d %b %Y %H:%M:%S +0000", self.NEW_DATE))


application = webapp2.WSGIApplication([
    ('/rss.xml', MainHandler)
], debug=False)
