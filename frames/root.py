from tkinter import Tk
from frames.header import create_header
from frames.body import create_body
from frames.menu import Menu

# Main window to manage all app actions.
class MainWindow(Tk):
	
	def __init__(self):		
		super().__init__()
		self.create_frames()
		self.configure_buttons()


	def create_frames(self):
		self.header = create_header(self)		
		self.body, self.main_panel = create_body(self)
		self.menu = Menu(self)
		self.menu.set_body(self.body)
		


	def configure_buttons(self):
		# Adding method to show and hide menu to the menu button.
		self.header["mButton"].config(command=self.show_hide_menu)



	def show_hide_menu(self):
		#Conditional to verify if menu is shown or not.
		if self.menu.winfo_ismapped(): self.menu.pack_forget() #Hide menu
		else: self.menu.pack(side='left',fill='y', padx=0) #Show menu