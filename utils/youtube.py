from pytubefix import YouTube
from tkinter import messagebox
from utils.video_yt import get_video_info
from widgets.labels import ContentLabel
from widgets.progressbars import CustomProgressbar



#Custom YouTube object
class VideoYT():
	def __init__(self, url):
		self.url = url		
		self.get_info()		


	def get_info(self):
		self.video = YouTube(self.url, on_progress_callback=self.update_progress_bar)				
		self.info = get_video_info(self.video)


	def download_file(self, file_path, file_quality, file_type,frame):
		self.file_path = file_path
		self.file_quality = file_quality
		self.file_type = file_type
		self.download_status_panel(frame)
		if file_type == 1:
			self.down_video()
		elif file_type ==2:
			self.down_audio()
		elif file_type == 3:
			self.down_onlyvideo()


	def download_status_panel(self, frame):
		ContentLabel(frame,text='Descargando...').grid(column=0,row=0)	
		self.progress_bar = CustomProgressbar(frame,style='Horizontal.TProgressbar')	
		self.progress_bar.grid(column=1,row=0,columnspan=2)
		self.progress_label = ContentLabel(frame,text='0%')
		self.progress_label.grid(column=3,row=0)


	def down_video(self):
		video = self.video.streams.filter(progressive=True, resolution=self.file_quality).last()		
		self.filesize = video.filesize
		video.download(filename=self.file_path,skip_existing=False)
		messagebox.showinfo(title='Video guardado', message='El video ha sido guardado exitosamente en: '+ self.file_path)


	def down_audio(self):
		audio = self.video.streams.filter(mime_type='audio/mp4', abr=self.file_quality).last()		
		self.filesize = audio.filesize
		audio.download(filename=self.file_path,skip_existing=False)
		messagebox.showinfo(title='Audio guardado', message='El audio ha sido guardado exitosamente en: '+self.file_path)


	def down_onlyvideo(self):
		video = self.video.streams.filter(mime_type='video/webm',resolution=self.file_quality).last()		
		self.filesize = video.filesize
		video.download(filename=self.file_path,skip_existing=False)
		messagebox.showinfo(title='Video guardado', message='El video ha sido guardado exitosamente en: '+ self.file_path)


	def update_progress_bar(self, chunk, file_handle, bytes_remaining):		
		current = ((self.filesize - bytes_remaining)/self.filesize)*100
		self.progress_bar['value'] = current
		self.progress_label['text'] = f'{round(current,2)} %'