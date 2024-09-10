from tkinter import Button
from tkinter.font import Font, nametofont
from constants.app import FONT, BACKGROUND
from constants.images_paths import IMG_BTN_SEARCH,IMG_BTN_BACK, IMG_BTN_EXAMINE, IMG_BTN_DOWNLOAD
from utils.images import read_image

class FooterMenuButton( Button ):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.style_button()
		self.bind_hover_events()


	def style_button(self):
		self.config(			
			foreground='white',
			font=[20],
			relief='flat',
			cursor='hand2'
			)

	def bind_hover_events(self):
		self.bind("<Enter>", lambda event: self.on_enter(event))
		self.bind("<Leave>", lambda event: self.on_leave(event))


	def on_enter(self, event):
		self.config(bg="#222")		


	def on_leave(self, event):
		self.config(bg='#111', fg="white")


class LinkButton ( Button ):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.style_button()
		self.bind_hover_events()

	def style_button(self):
		self.config(
			font=[FONT, 10],
			foreground='white',
			relief='flat',
			borderwidth=0,
			cursor='heart')

	def bind_hover_events(self):
		self.bind("<Enter>", lambda event: self.on_enter(event))
		self.bind("<Leave>", lambda event: self.on_leave(event))


	def on_enter(self, event):
		self.config(foreground='blue', font=[FONT, 10, 'underline'])		


	def on_leave(self, event):
		self.config(fg="white", font=[FONT, 10])


class RoundedButton(Button):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.config(width=91,height=31,bd=0,relief='sunken',bg='black',activebackground='black')     
        self.bind('<Enter>', self.on_hover)
        self.bind('<Leave>', self.on_leave)

    def set_bg(self,path_img_active,path_img_inactive):
        self.btn_inactive = read_image(path_img_inactive)
        self.btn_active = read_image(path_img_active)
        self.config(image=self.btn_inactive)

    def on_hover(self, event):
        if self['state'] == 'disabled':
            self['cursor'] ='arrow'
        else:
            self['cursor'] ='hand2'
            self.config(image=self.btn_active)

    def on_leave(self,event):
        self.config(image=self.btn_inactive)


class SearchButton(RoundedButton):
	def __init__(self, *args,**kwargs):
		super().__init__(*args,**kwargs)
		super().set_bg(IMG_BTN_SEARCH["active"], IMG_BTN_SEARCH["inactive"])


class BackButton(RoundedButton):
	def __init__(self, *args,**kwargs):
		super().__init__(*args,**kwargs)
		super().set_bg(IMG_BTN_BACK["active"], IMG_BTN_BACK["inactive"])


class ExamineButton(RoundedButton):
	def __init__(self, *args,**kwargs):
		super().__init__(*args,**kwargs)
		self.config(bg='black')
		super().set_bg(IMG_BTN_EXAMINE["active"], IMG_BTN_EXAMINE["inactive"])


class DownloadButton(RoundedButton):
	def __init__(self, *args,**kwargs):
		super().__init__(*args,**kwargs)
		super().set_bg(IMG_BTN_DOWNLOAD["active"], IMG_BTN_DOWNLOAD["inactive"])

#Button for app header
class MenuButton(Button):
	def __init__(self, *args,**kwargs):
		super().__init__(*args,**kwargs)
		self.style_button()
		self.bind_hover_events()


	def style_button(self):
		self.config(text="  ☰  ",
			foreground="white",
			bg='#222',
			font=["Comics Sans", 15],			
			borderwidth=2,
			relief="flat",
			# overrelief="raised",
			cursor='hand2')
	def bind_hover_events(self):
		self.bind("<Enter>", lambda event: self.on_enter(event))
		self.bind("<Leave>", lambda event: self.on_leave(event))


	def on_enter(self, event):
		self.config(bg="#111",cursor="hand2")		


	def on_leave(self, event):
		self.config(bg='#222', fg="white")


class OptionMenuButton(Button):
	def __init__(self, *args,**kwargs):
		super().__init__(*args,**kwargs)
		self.style_button()
		self.bind_hover_events()


	def style_button(self):
		self.config(
			bg='#222',
			fg="white",
			relief="flat",			
			font=[FONT, 13, "bold"]
		)


	def bind_hover_events(self):
		self.bind("<Enter>", lambda event: self.on_enter(event))
		self.bind("<Leave>", lambda event: self.on_leave(event))


	def on_enter(self, event):
		self.config(bg="#00659F",cursor="hand2")		


	def on_leave(self, event):
		self.config(bg='#222', fg="white")
	
		