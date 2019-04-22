import moviepy.editor as mp


clip = mp.VideoFileClip("Prekrasnoe Daleko.mp4")
clip.audio.write_audiofile("theaudio.mp3")