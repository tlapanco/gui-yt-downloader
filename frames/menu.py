from constants.images_paths import IMG_PROFILE
from tkinter import Frame
from widgets.buttons import OptionMenuButton, FooterMenuButton
from constants.app import BACKGROUND
from widgets.labels import ImageLabel
from utils.images import read_image
from frames.panels.main import Main
from frames.panels.downloadvideo.search_video import SearchVideo


#Menu configurations.
BG = '#111'
WIDTH = 180
PROFILE = IMG_PROFILE

# Frame that will contain all avaiable options
class Menu(Frame):
	def __init__(self, *args,**kwargs):
		super().__init__(*args,**kwargs)
		# Array that contains the menu options information.
		self.options = [
			("Descargar\n de YouTube", self.open_search_panel)
		]
		self.create_options()


	def create_options(self):
		self.config(bg=BG, width=WIDTH)
		#Main menu image
		self.img_profile = read_image(PROFILE, (150,150))
		self.img = ImageLabel(self,image=self.img_profile)
		self.img.config(bg=BG)
		self.img.pack()
		#Creating buttons for every option from self.options
		for name, command in self.options:
			OptionMenuButton(self, text=name, command=command).pack(fill="both", pady=[5,0], padx=0)
		#Footer menu options
		FooterMenuButton(self,text='Inicio', bg=BG, command=self.open_main_panel).pack(side='bottom', fill='x', pady=[0,20])
		self.pack_propagate(False)

	def open_search_panel(self):		
		self.search_panel = SearchVideo(self.body)


	def open_main_panel(self):
		
		self.main_panel = Main(self.body)


	def set_body(self, body):
		self.body = body