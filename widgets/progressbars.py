from tkinter.ttk import Progressbar, Style

class CustomProgressbar(Progressbar):
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.asignar_estilos()


	def asignar_estilos(self):
		estilos = Style()	
		
		estilos.configure('Horizontal.TProgressbar',
											troughcolor='black',
											background='white',
											darkcolor='white',
											lightcolor='white',
											bordercolor='white'
			)
		

	def actualizar_barra(self, tamaño,actual):
		self['value'] = actual / tamaño * 100
