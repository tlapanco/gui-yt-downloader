from tkinter import Frame, IntVar, messagebox
from threading import Thread
from widgets.entries import URLEntry
from widgets.labels import ContentLabel
from widgets.comboboxes import CustomCombobox
from widgets.buttons import DownloadButton, BackButton, ExamineButton
from widgets.radiobuttons import CustomRadioButton
from utils.frames import clear_frame
from utils.system import get_current_path, set_path


#Download frame configurations
BG = 'black'

#Download frame texts
TITLE_NOT_AVAIABLE = 'No disponible.'
TEXT_NOT_AVAIABLE = 'Archivo no disponible, elige otro tipo de archivo o intentalo más tarde.'


class DownloadFrame():
	def __init__(self, root, video, search_panel):
		self.root = root
		self.info = video.info
		self.video = video
		self.search_panel = search_panel
		self.create_frame()


	def create_frame(self):
		self.frame = Frame(self.root, bg=BG)
		self.frame.pack(side='top')
		self.downloads_panel =Frame(self.root, bg=BG)
		self.downloads_panel.pack(pady=[20,0])
		self.show_qualities()


	def show_qualities(self):
		#Row index for grid frame
		row = 0
		ContentLabel(self.frame,text="Calidades: ").grid(column=0,row=row, pady=5, columnspan=2)
		self.combobox = CustomCombobox(self.frame)
		self.combobox.grid(column=2, row=row,columnspan=2, pady=5)
		self.show_radiobuttons(row+1)


	def show_radiobuttons(self, row):
		self.option = IntVar()
		CustomRadioButton(self.frame, variable=self.option, value=1, command=self.update_frame, text='Video').grid(column=1,row=row+1,pady=5)
		CustomRadioButton(self.frame, variable=self.option, value=2, command=self.update_frame, text='Audio').grid(column=2,row=row+1,pady=5)
		CustomRadioButton(self.frame, variable=self.option, value=3, command=self.update_frame, text='Video (solo)').grid(column=3,row=row+1,pady=5)
		self.show_path_details(row+1)


	def show_path_details(self, row):
		#Getting and setting initial file path
		self.video_path = get_current_path()
		self.path = URLEntry(self.frame, width=80)
		self.path.insert(0,self.video_path)
		self.path.grid(row=row+1, columnspan=4, pady=5 )
		self.show_buttons(row+1)		
		

	def show_buttons(self, row):
		self.exa_btn = ExamineButton(self.frame, state='disabled', command=self.set_video_path)
		self.exa_btn.grid(column=0,row=row+1,columnspan=4,pady=10)
		BackButton(self.frame, command=self.search_panel).grid(column=0, row=row+2)
		self.dow_btn =DownloadButton(self.frame, state='disabled', command=self.on_dow_clicked)
		self.dow_btn.grid(column=3, row=row+2)


	def set_video_path(self):		
		self.info["title"], self.video_path = set_path(self.video_path, self.option.get(), self.info["title"], self.path)


	def on_dow_clicked(self):
		if self.combobox.get() != 'No disponible':			
			Thread(target=self.download).start()
		else:
			messagebox.showinfo(title=TITLE_NOT_AVAIABLE, message=TEXT_NOT_AVAIABLE)


	def download(self):
		if self.downloads_panel.winfo_children():
			clear_frame(self.downloads_panel)
		self.video.download_file(self.path.get(), self.combobox.get(), self.option.get() , self.downloads_panel)

	#Function to change the filename and state of buttons when clicked on radiobuttons
	def update_frame(self):
		self.path.delete(0,'end')
		if self.option.get() == 1:
			self.combobox["values"] = self.info["q_video"]
			self.path.insert(0, self.video_path + self.info["title"] +'.mp4')
		elif self.option.get() == 2: 
			self.combobox["values"] = self.info["q_audio"]			
			self.path.insert(0, self.video_path + self.info["title"] +'.mp3')
		elif self.option.get() == 3: 
			self.combobox["values"] = self.info["q_solo_video"]			
			self.path.insert(0, self.video_path + self.info["title"] +'.webm')
		self.combobox.current(0)
		self.combobox['state'] = 'readonly'
		self.dow_btn['state']='normal'		
		self.exa_btn['state'] = 'normal'