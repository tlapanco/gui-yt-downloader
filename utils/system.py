from tkinter import filedialog
import os
import sys
import webbrowser

#Resolves source path for assets.
def resource_path(relative_path):    
    try:        
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


#Function to open a new browser tap 
def open_in_browser( URL):
    webbrowser.open( URL )

#Function that returns filename and filepath as strings.
def set_path(file_path, type, file_name, path_entry):
	#Option for only video
	if type == 3:
		path = filedialog.asksaveasfilename(
			defaultextension='.webm',
			filetypes=[('WEBM','*.webm')],
			initialdir=file_path,
			initialfile=file_name,
			title='Guardar video como')		
	
	#Option for audio
	elif type == 2:
		path = filedialog.asksaveasfilename(
			defaultextension='.mp3',
			filetypes=[('MP3','*.mp3')],
			initialdir=file_path,
			initialfile=file_name,
			title='Guardar audio como')
	
	#Option for video
	elif type == 1:
		path= filedialog.asksaveasfilename(
			defaultextension='.mp4',
			filetypes=[('MP4','*.mp4')],
			initialdir=file_path,
			initialfile=file_name,
			title='Guardar video como')
	#When no path changes, returns old file path and filename
	if path !='':		
		path_entry.delete(0,'end')
		path_entry.insert(0,path)
		
		file_name = path.split('/')[-1]
		
		file_path = path.replace(file_name,'')
		file_name = file_name.split('.')[0]
	
	return file_name, file_path

#Returns a string with the current path 
def get_current_path():
	path = os.path.abspath(os.getcwd())
	path = path.replace('\\','/') + '/'

	return path