from constants.images_paths import IMG_DOWNLOAD
from threading import Thread
from utils.frames import clear_frame
from utils.images import read_image
from utils.video_yt import validate_yt_URL
from widgets.labels import ImageLabel, TitleLabel
from widgets.entries import URLEntry
from widgets.buttons import SearchButton
from tkinter import messagebox
from frames.panels.error import ErrorPanel
from frames.panels.downloadvideo.video_info import VideoInfo
from frames.panels.downloadvideo.wait_video import WaitGetVideo


#Search panel configurations
BG = 'black'

#Search panel texts
TITLE = "Inserta el URL de tu vídeo aquí..."
ERROR_TITLE = "Error."
NOT_YT_URL_MESSAGE = "El texto ingresado, no es una URL válida. Revisa la URL e intentalo de nuevo."
ERROR_PANEL_TEXT = "Algo salió mal..."


class SearchVideo():
	def __init__(self, body):
		self.body = body
		self.create_content()

	def create_content(self):
		clear_frame(self.body)
		self.body.config(bg=BG)
		self.image = read_image(IMG_DOWNLOAD)
		ImageLabel(self.body,image=self.image).pack(expand=True)
		TitleLabel(self.body,text=TITLE).pack(expand=True)
		self.url_entry = URLEntry(self.body)
		self.url_entry.pack(fill='x',expand=True, padx=40,ipady=2)
		self.url_entry.focus()
		SearchButton(self.body, bg=BG, command=self.search_video).pack(expand=True)


	def search_video(self):
		#get entry content and transforms it to a string
		self.video_url = str(self.url_entry.get())
		#validate url
		if validate_yt_URL(self.video_url):
			self.get_yt_video(self.video_url) #get video from YouTube
		else:
			#show an error message 			
			messagebox.showerror(title=ERROR_TITLE, message=NOT_YT_URL_MESSAGE)
			self.url_entry.focus()
			self.url_entry.select_range(0,len(self.video_url))


	def get_yt_video(self, video_url):		
		clear_frame(self.body)
		#Show a wait panel while getting YouTube video.
		self.wait_panel = WaitGetVideo(self.body)
		Thread(target=self.open_video_panel).start()


	def open_video_panel(self):
		#Create a panel with video info
		try:			
			self.panel_info = VideoInfo(self.body, self.video_url, self.create_content)
		except Exception as e:
			ErrorPanel(self.body, ERROR_PANEL_TEXT, str(e), self.create_content)