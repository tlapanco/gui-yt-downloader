from tkinter import Frame
from utils.system import open_in_browser
from widgets.buttons import MenuButton, LinkButton
from constants.app import BACKGROUND, GITHUB_URL

#Background color for header.
BG = '#222'
#Size in pixels for header.
HEIGHT = 50

def open_github_profile():
	open_in_browser(GITHUB_URL)

#Function to create a header according to a given frame (root).
def create_header(root):
	header = Frame(root, bg=BG, height=HEIGHT)
	header.pack_propagate(False)
	header.pack(side='top',fill='x')	
	header_content = {}
	LinkButton(header, bg= BG, text='@tlapanco', command=open_github_profile).pack(side='right', padx=[0,20])
	#Return a button object to use as needed.
	header_content["mButton"] = MenuButton(header)
	header_content["mButton"].pack(fill='y',side='left')
	return header_content