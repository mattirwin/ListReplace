import sublime, sublime_plugin

class listReplaceCommand(sublime_plugin.WindowCommand):
	def reverse_enum(self, L):
		for index in reversed(xrange(len(L))):
			yield index, L[index]

	def run(self):
		ws = self.window.views()
		if (len(ws) < 2):
			print "Requires at least 2 views/tabs"
			return
		# print ws
		
		self.window.show_input_panel("Term to search:", "", self.on_done, None, None)
		pass
		
	def getNRows(self, cview):
		endChar = cview.size()
		numRows = cview.rowcol(endChar)[0] + 1
		return numRows

	def getRows(self, cview):
		endChar = cview.size()
		numRows = cview.rowcol(endChar)[0] + 1
		outList = []

		for x in range(0, numRows):
			ctp = cview.text_point(x,0)
			lineContent = cview.substr(cview.line(ctp))
			outList.append(lineContent)

		return outList

	def getNMatches(self, cview, tomatch):
		foundList = cview.find_all(tomatch)
		numMatches = len(foundList)
		return numMatches

	def makeReplacements(self, sview, tomatch, rowContent):
		foundList = sview.find_all(tomatch)

		for idx, fLoc in self.reverse_enum(foundList):
			print idx, fLoc, rowContent[idx]

			try:
				sEdit = sview.begin_edit()
				sview.replace(sEdit, fLoc, rowContent[idx])
				sview.end_edit()
			except:
				print "makeReplacements error"
				pass

	def on_done(self, searchText):
		try:
			#sublime.status_message("User said: " + user_input)
			print "post input..."
			searchView = self.window.views()[0]
			replaceView = self.window.views()[1]

			print "now for numRows..."
			searchNum = self.getNMatches(searchView, searchText)
			repNum = self.getNRows(replaceView)
			print searchNum
			print repNum

			if searchNum != repNum:
				print "Number of search terms and replacement terms do not match"
			else:
				print "Search and Match are ready!!!"

				rowContent = self.getRows(replaceView)

				self.makeReplacements(searchView, searchText, rowContent)

				# try:
				# 	sEdit = searchView.begin_edit()
				# 	searchView.replace(sEdit, searchView.line(0), "going nuts")
				# 	searchView.end_edit()
				# except:
				# 	print "no luck"
				# 	pass

		except ValueError:
			print "error"
			pass
