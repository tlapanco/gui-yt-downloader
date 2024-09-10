from tkinter import Entry

class URLEntry(Entry):
	def __init__(self, *args,**kwargs):
		super().__init__(*args,**kwargs)
		self.style_entry()


	def style_entry(self):
		self.config(bg='black',
			highlightcolor='white',
			highlightthickness=2,
			bd=0,
			foreground='white',
			selectbackground='white',
			selectforeground='black',
			insertbackground='white',
			justify='center',
			relief='flat',
			highlightbackground='white')