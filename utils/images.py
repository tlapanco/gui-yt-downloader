#Read and resize an image avaiable to use in Tk.
def read_image( path, size=None):
	from PIL import ImageTk, Image
	if size ==None:
		return ImageTk.PhotoImage(Image.open(path))
	else:
		return ImageTk.PhotoImage(Image.open(path).resize(size,  Image.ADAPTIVE)) 