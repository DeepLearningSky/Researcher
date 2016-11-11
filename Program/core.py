from tkinter import *
import os

def notImplimented():
	pass

def newProject(dir, name, topic, tags):
	if not os.path.isdir(dir):
		print("ERROR! " + dir + " not a valid directory")
		return
	else:
		os.mkdir(dir + "/" + name)
		dir = dir + "/" + name
		os.mkdir(dir + "/Data")

		pgtfile = open(dir + "/" + name + ".rsproj", 'w')
		pgtfile.write("~name " + name)
		pgtfile.write("~topic " + topic)
		for tag in tags:
			pgtfile.write("~tag: " + tag)
		pgtfile.close()

class ProjectScreen():
	def __init__(self):
		self.components = {}
		self.root = Tk()
		self.root.geometry('{}x{}'.format("200", "50"))
		self.AddComponent("newprojectbutton", Button(self.root, text="New Project", command=notImplimented))
		self.components["newprojectbutton"].pack()
		self.AddComponent("openprojectbutton", Button(self.root, text="Open Project", command=notImplimented))
		self.components["openprojectbutton"].pack()
		self.root.mainloop()

	def AddComponent(self, name, component):
		self.components[name] = component
	def RemoveComponent(self, name):
		self.components[name] = None

if __name__ == "__main__":
	pgt = ProjectScreen()