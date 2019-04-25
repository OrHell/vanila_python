import sys # import sys 
import pytube

link = input('Please enter a url link\n')
yt = pytube.YouTube(link)
stream = yt.streams.first()
finished = stream.download()
print ('Download is complete')

sys.exit()