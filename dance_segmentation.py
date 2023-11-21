import moviepy.editor as mp

video_clip = mp.VideoFileClip(r"dance_video.mp4")

#Extract the Audio
audio = video_clip.audio

print(audio)
print(video_clip)