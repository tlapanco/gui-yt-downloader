from tkinter import Label
from constants.app import FONT


class ContentLabel(Label):
	def __init__(self, *args,**kwargs):
		super().__init__(*args,**kwargs)
		self.style_label()


	def style_label(self):
		self.config(bg='black',fg='white',font=[FONT, 10])


class ErrorLabel(Label):
	def __init__(self, *args,**kwargs):
		super().__init__(*args,**kwargs)
		self.style_label()


	def style_label(self):
		self.config(foreground='red',bg='black', font=[FONT,15])
		

class TitleLabel(Label):
	def __init__(self, *args,**kwargs):
		super().__init__(*args,**kwargs)
		self.style_label()


	def style_label(self):
		self.config(
			bg="black",
			foreground="white",
			font=(FONT,20))
		

class ImageLabel(Label):
	def __init__(self, *args,**kwargs):
		super().__init__(*args,**kwargs)
		self.style_label()


	def style_label(self):
		self.config(bg='black')

	