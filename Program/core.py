import urllib.request
from tkinter import *
import parser

class ResearchWindow():
	def __init__(self):
		self.root = Tk()
		self.textDisplay = Text(self.root)
		self.textDisplay.grid(row=1, column=0)
		self.textDisplay.config(state='normal')
		Label(self.root, text="Control").grid(row=1, column=2, sticky=N, pady=0)
		self.addentry = Entry(self.root)
		self.addentry.grid(row=1, column=2, sticky=N, pady=20)
		self.addentrybutton = Button(self.root, text="Add", command=AddSite)
		self.addentrybutton.grid(row=1, column=3, sticky=NE, pady=20, padx=0)
		self.print("Ready")
		self.root.mainloop()
	def print(self, text, newline = True):
		self.textDisplay.insert(END, text)
	def AddSite(self):
		add = self.textDisplay.get()
		self.textDisplay.set("")
		
if __name__ == "__main__":
	reswindow = ResearchWindow()
