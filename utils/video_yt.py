from utils.time import secs_ToHrsMinSec

#Funtion that returns a dictionary with qualities for every file type.
def get_available_qualities( yt_obj ):
	#Dictionary with video avaiable qualities
	qualities = {
		"audio": [],
		"video": [],
		"solo_video": []
	}	

	#Getting audio qualities and saving in qualities['audio']
	audio_qualities = yt_obj.streams.filter(mime_type='audio/mp4').order_by('abr')
	for audio in audio_qualities:
		if audio.abr not in qualities["audio"] and audio.abr != '':
			qualities["audio"].append(audio.abr)

	#Getting only video qualities and saving in qualities['solo_video']
	solovideo_qualities = yt_obj.streams.filter(mime_type='video/webm').order_by('resolution')
	for video in solovideo_qualities:
		if video.resolution not in qualities["solo_video"] and video.resolution != '':
			qualities["solo_video"].append(video.resolution)

	#Getting video qualities and saving in qualities['video']
	video_qualities = yt_obj.streams.filter(progressive=True).order_by('resolution')
	for video in video_qualities:
		if video.resolution not in qualities["video"] and video.resolution !='':
			qualities["video"].append(video.resolution)	

	#When there are not avaiable qualities:
	#add  a string element 'No disponible' to the file type 
	if qualities["audio"] == []:	qualities["audio"].append('No disponible')
	if qualities["video"] == []:	qualities["video"].append('No disponible')
	if qualities["solo_video"] == []:	qualities["solo_video"].append('No disponible')
	
	return qualities


#Function that returns an ImageTk object with the video thumbnail for a given URL.
def get_thumbnail( url ):	
	from PIL import ImageTk, Image
	from os import remove
	from requests import get
	from shutil import copyfileobj
	res = get(url, stream=True)	
	if res.status_code == 200:	
		with open('thumbnail.png', 'wb') as f:
			res.raw.decode_content = True
			copyfileobj(res.raw, f)	
	thumbnail = ImageTk.PhotoImage(Image.open('thumbnail.png').resize((200,150),Image.ADAPTIVE))	
	remove('thumbnail.png')

	return thumbnail

#Function that returns a dictionary with the info needed from a given video.
def get_video_info( video ):	
	qualities = get_available_qualities(video)
	videoInfo = {}
	videoInfo['title'] = video.title
	if len(video.title) > 30: 
		video.title = video.title[0:47] + '...'	
	videoInfo["short_title"] = video.title
	videoInfo['author'] = video.author
	videoInfo['publish_date'] = video.publish_date = str(video.publish_date).split()[0]
	videoInfo['length'] = secs_ToHrsMinSec(video.length)
	videoInfo['thumbnail'] = get_thumbnail(video.thumbnail_url)
	videoInfo['q_video'] = qualities["video"]
	videoInfo['q_audio'] = qualities["audio"]
	videoInfo['q_solo_video'] = qualities["solo_video"]
	return videoInfo

#function to validate an youtube video URL 
def validate_yt_URL( url ):
	#function to use regex
	from re import match
	if match("(https?:\/\/)?([\dwww\.-]+)\.([youtube\.]{2,6})([\/\w \.-]*)*\/?", url): return True
	else: return False
