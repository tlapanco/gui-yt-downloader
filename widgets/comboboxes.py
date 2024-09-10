from tkinter.ttk import Combobox, Style


class CustomCombobox ( Combobox ):
	def __init__(self, *args,**kwargs):
		super().__init__(*args,**kwargs)
		self.style_button()


	def style_button(self):
		styles = Style()		
		styles.configure('TCombobox',background='black')
		self.config(state='disabled')



