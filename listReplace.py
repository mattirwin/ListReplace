"""
ListReplace
v 0.1.0
Licensed under MIT
Copyright (c) 2014 Matt Irwin <info@irwinone.com>
"""

import sublime, sublime_plugin

class listReplaceCommand(sublime_plugin.WindowCommand):
	searchTerm = None
	repTerm = None
	searchView = None
	repView = None
	selList = []

	def reverse_enum(self, L):
		for index in reversed(xrange(len(L))):
			yield index, L[index]

	def run(self):
		self.searchTerm = None
		self.repTerm = None
		self.searchView = None
		self.repView = None
		self.selList = []

		ws = self.window.views()
		
		if (len(ws) < 2):
			sublime.error_message("Requires at least 2 views/tabs")
			return
		
		for idx, cv in enumerate(ws):
			if cv.file_name() != None :
				self.selList.append(cv.file_name().split("/")[-1] + "," + str(idx))
			else:
				self.selList.append(cv.substr(cv.line(0)).replace(",", "") + "," + str(idx))

		# these nested callbacks are really gross but as a python newb I'm not sure how to fix this...
		sublime.message_dialog("Choose the target view in the following dropdown")
		self.window.show_quick_panel([elem.split(",")[0] for elem in self.selList], self.setSearchView)

	def setSearchView(self, viewIdx):
		if viewIdx == -1 :
			return
		transIdx = int(self.selList[viewIdx].split(',')[-1])
		self.searchView = self.window.views()[transIdx]
		del self.selList[viewIdx]
		sublime.message_dialog("Choose the source view in the following dropdown")
		self.window.show_quick_panel([elem.split(",")[0] for elem in self.selList], self.setRepView)

	def setRepView(self, viewIdx):
		if viewIdx == -1 :
			return
		transIdx = int(self.selList[viewIdx].split(',')[-1])
		self.repView = self.window.views()[transIdx]
		del self.selList[viewIdx]
		self.window.show_input_panel("Enter a search term (regex):", "", self.setSearchTerm, None, None)

	def setSearchTerm(self, iTerm):
		self.searchTerm = iTerm
		self.window.show_input_panel("Enter a replacement term (regex):", "", self.setRepTerm, None, None)

	def setRepTerm(self, iTerm):
		self.repTerm = iTerm
		self.final_run()

	def getNMatches(self, cview, tomatch):
		foundList = cview.find_all(tomatch)
		numMatches = len(foundList)
		return numMatches

	def getMatches(self, cview, tomatch):
		foundList = cview.find_all(tomatch)
		outList = [cview.substr(x) for x in foundList]
		return outList

	def makeReplacements(self, sview, tomatch, rowContent):
		foundList = sview.find_all(tomatch)
		for idx, fLoc in self.reverse_enum(foundList):
			try:
				sEdit = sview.begin_edit()
				sview.replace(sEdit, fLoc, rowContent[idx])
				sview.end_edit()
			except:
				#sublime.error_message("listReplace - Error during makeReplacements")
				print "listReplace - Error during makeReplacements"

	def final_run(self):
		searchNum = self.getNMatches(self.searchView, self.searchTerm)
		repNum = self.getNMatches(self.repView, self.repTerm)
		if searchNum != repNum:
			sublime.error_message("Number of search terms and replacement terms do not match")
		else:
			sublime.status_message("Search and Match are ready!!!")
			replacements = self.getMatches(self.repView, self.repTerm)
			self.makeReplacements(self.searchView, self.searchTerm, replacements)

