import urllib.request
from tkinter import *
import threading
import htmlparser
import time

pages = []
class LookupWorker(threading.Thread):
	def __init__(self, window):
		threading.Thread.__init__(self)
		self.window = window
		self.work = []
	def run(self):
		self.window.print("Started lookup thread")
		while True:
			for url in self.work:
				self.window.print("Looking up " + url)
				code = htmlparser.GetCode(url)
				pages.append(urllib.Webpage(url, code))
			for i in range(len(self.work)):
				self.work.pop(i)
			time.sleep(1)
	def AddWork(self,works):
		self.work.append(works)
		if type(works) == str:
			self.window.print("Added " + works)
		else:
			for item in works:
				self.window.print("Added " + item)
class ResearchWindow():
	def __init__(self):
		buffy = 0
		self.lookup = []
		self.root = Tk()
		self.textDisplay = Text(self.root)
		self.textDisplay.grid(row=1, column=0)
		self.textDisplay.config(state='disabled')
		Label(self.root, text="Control").grid(row=1, column=2, sticky=N, pady=buffy)
		buffy += 20
		self.addentry = Entry(self.root)
		self.addentry.grid(row=1, column=2, sticky=N, pady=buffy)
		self.addentrybutton = Button(self.root, text="Add", command=self.AddSite)
		self.addentrybutton.grid(row=1, column=3, sticky=NE, pady=buffy, padx=0)
		
		self.lookupbot = LookupWorker(self)
		self.lookupbot.start()

		self.print("Ready\n")
		self.root.mainloop()
	def print(self, text, newline = True):
		self.textDisplay.config(state='normal')
		if newline:
			text += "\n"
		self.textDisplay.insert(END, text)
		self.textDisplay.config(state='disabled')
	def AddSite(self):
		add = self.addentry.get()
		self.addentry.delete(0, END)
		self.lookupbot.AddWork(add)
if __name__ == "__main__":
	reswindow = ResearchWindow()
