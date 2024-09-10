from tkinter import Frame
from frames.panels.main import Main

#A simple Frame to varied use.
def create_body( root ):
	body = Frame(root)
	body.pack(side='right', fill="both",expand=True)
	main_panel = Main(body)
	#Return Frame object to be used as needed.
	return body, main_panel