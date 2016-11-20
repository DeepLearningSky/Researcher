import urllib
class Webpage:
	def __init__(self, url, code = None, tokens = None):
		self.url = url
		self.code = code
		self.tokens = tokens

def GetCode(url):
	page = urllib.request.urlopen(url).read()
	return page
