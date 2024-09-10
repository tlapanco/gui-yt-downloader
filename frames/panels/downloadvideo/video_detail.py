from tkinter import Frame
from widgets.labels import ImageLabel, ContentLabel

#Detail frame configurations
BG = 'black'

class DetailFrame():
	def __init__(self, root, info):
		self.root = root
		self.info = info				
		self.create_frame()


	def create_frame(self):
		self.frame = Frame(self.root, bg=BG)
		self.frame.pack(side='top', pady=[30, 15])		
		self.create_content()


	def create_content(self):
		#Thumbnail from Video
		self.thumbnail = ImageLabel(self.frame,image=self.info['thumbnail'])
		self.thumbnail.grid(column=0,row=0,columnspan=2,pady=5,rowspan=4)
		#Video information 
		video_details =[
			('title_label','Título del vídeo:', self.info["short_title"]),
			('autor_label','Autor: ', self.info['author']),
			('length_label','Duración: ', self.info['length']),
			('pdate_label','Fecha de publicación: ', self.info['publish_date'])
		]
		#row and column indexes to use in grid frame
		#Starting in the first row
		row = 0
		#Starting in the third column because of video image
		column = 2
		#Creating every label for video information
		for l_name, l_content, l_detail in video_details:
			ContentLabel(self.frame, text=l_content).grid(column=column, row=row, padx=10)
			ContentLabel(self.frame, text=l_detail).grid(column=column+1, row=row, pady=5)
			row += 1