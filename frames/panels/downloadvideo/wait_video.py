from constants.images_paths import IMG_YT_LEN
from utils.images import read_image
from widgets.labels import ImageLabel, TitleLabel

#Wait video panel texts
SEARCH_VIDEO_MESS= "Buscando vídeo..."

class WaitGetVideo():
	def __init__(self, root):
		self.root = root		
		self.create_content()


	def create_content(self):
		self.image = read_image(IMG_YT_LEN)
		self.image_label = ImageLabel(self.root, image=self.image)
		self.image_label.pack(pady=[50,0])
		TitleLabel(self.root, text=SEARCH_VIDEO_MESS).pack(pady=[0, 50])
