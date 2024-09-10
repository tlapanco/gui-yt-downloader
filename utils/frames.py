#Delete content from a frame
def clear_frame( frame ):
		for widget in frame.winfo_children():
			widget.destroy()


#Config the number of columns to use grid
def config_frame_columns( frame, columns ):
	for i in range(0, columns):
		frame.columnconfigure(i, weight=1)