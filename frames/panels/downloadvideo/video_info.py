from widgets.labels import TitleLabel
from utils.frames import clear_frame, config_frame_columns
from utils.youtube import VideoYT
from frames.panels.downloadvideo.video_detail import DetailFrame
from frames.panels.downloadvideo.download_options import DownloadFrame



class VideoInfo():
	def __init__(self, root, video_url, search_panel):
		self.root = root
		self.video_url = video_url
		self.search_panel = search_panel
		self.get_video()


	def get_video(self):
		self.video_obj = VideoYT(self.video_url)
		self.create_content()


	def create_content(self):
		clear_frame(self.root)
		config_frame_columns(self.root, 4)
		self.frame_info = DetailFrame(self.root, self.video_obj.info)
		self.frame_download = DownloadFrame(self.root, self.video_obj, self.search_panel)