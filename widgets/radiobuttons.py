from tkinter.ttk import Radiobutton, Style


class CustomRadioButton ( Radiobutton ):
	def __init__(self, *args,**kwargs):
		super().__init__(*args,**kwargs)
		self.style_button()


	def style_button(self):
		styles = Style()
		styles.configure('TRadiobutton',background='black',foreground='white')

