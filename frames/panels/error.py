from widgets.labels import TitleLabel, ErrorLabel
from widgets.buttons import BackButton
from utils.frames import clear_frame


#Simple panel to show errors 
class ErrorPanel():
	def __init__(self, root, error_title, error_message, return_panel):
		self.root = root # Where this panel wil be showed
		self.error_title = error_title # Title for this panel
		self.error_message = error_message # Message for the error 
		self.return_panel = return_panel # Method to get back to the previous panel
		clear_frame(self.root)
		self.create_content()


	def create_content(self):
		TitleLabel(self.root, text=self.error_title).pack(pady=[25,5])
		ErrorLabel(self.root, text=self.error_message).pack()
		BackButton(self.root, command=self.return_panel).pack(pady=[15,0])
