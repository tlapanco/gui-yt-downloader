from constants.app import CODE_URL
from constants.images_paths import IMG_MAIN_PANEL
from utils.frames import clear_frame
from utils.images import read_image
from utils.system import open_in_browser
from widgets.labels import TitleLabel, ContentLabel, ImageLabel
from widgets.buttons import LinkButton

#Main panel configurations
BG = '#bbb'
FG ='black'

#Main panel texts
TITLE = 'YouTube Downloader V1.0'
FOOTER_TEXT = 'Ver código fuente en:'

class Main():
  def __init__(self, root):
    self.root = root
    self.root.config(bg=BG)
    self.create_content()
  

  def create_content(self):
    clear_frame(self.root)
    self.img = read_image(IMG_MAIN_PANEL)
    self.img_label = ImageLabel(self.root, image=self.img)
    self.img_label.config(bg=BG)
    self.img_label.pack()
    title = TitleLabel(self.root, text=TITLE)
    title.config(bg=BG)
    title.pack()    
    LinkButton(self.root, text='Github', command=self.open_code_source, bg=BG).pack(side='bottom', pady=[0,20])
    footer_text = ContentLabel(self.root, text=FOOTER_TEXT)
    footer_text.config(bg=BG, foreground=FG)
    footer_text.pack(side='bottom')

  def open_code_source(self):
    open_in_browser( CODE_URL)