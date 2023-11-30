
# Import everything needed to edit video clips 
import moviepy.editor as mp
import os
import glob

video_files = glob.glob('./dance_video/*')
for video_file in video_files:
    
    video_clip = mp.VideoFileClip(video_file)
    # getting audio from the clip 
    audioclip = video_clip.audio

    filename, file_extension = os.path.splitext(video_file)

    vidio_filename = os.path.basename(filename)
    
    audioclip.write_audiofile(f"./audio_files/{vidio_filename}.mp3")

    print(audioclip)