class Webpage:
	def __init__(self, url, code = None, tokens = None):
		self.url = url
		self.code = code
		self.tokens = tokens

def GetCode(url):
	url = "https://google.com"
	page = urllib.request.urlopen(url).read()
	return Webpage(url, code)
