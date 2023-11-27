
# Import everything needed to edit video clips 
from moviepy.editor import *
  
# loading video gfg 
clip = VideoFileClip("./dance_video/dance_2.mp4") 
  
# getting audio from the clip 
audioclip = clip.audio

audioclip.write_audiofile("dance_audio.mp3")

print(audioclip)