"""Python makes it super easy to download YouTube videos. With 
just a few lines of code, you will have your favorite videos saved 
on your computer. The Python library that you need to 
download videos is pytube. Install it with"""

from pytube import YouTube
yt_video = YouTube ("https://www.youtube.com/watch?v=NrpKKR96YAw")

v_file = yt_video.streams.filter(file_extension="mp4")\
 .get_by_resolution("360p")

v_file.download("D:\My_learning")
