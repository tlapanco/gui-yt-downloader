from constants.app import IMG_WIN_ICON
from frames.root import MainWindow

#Main window configurations
TITLE = "Youtube Downloader"
W_SIZE = "1000x600"
W_ICON = IMG_WIN_ICON

app = MainWindow()
app.title(TITLE)
app.geometry(W_SIZE)
app.iconbitmap(W_ICON)
app.resizable(0,0)

#Starting app
if __name__ == "__main__":
	app.mainloop()
	