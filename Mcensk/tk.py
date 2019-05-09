import os
import glob
import time
import sys
from playsound import playsound
os.system("mode con cols=40 lines=30")
with open ("test.txt",'r') as file:
	id_file=file.read()
try:
	lenght_track = os.path.getsize(id_file)
	lenght_track = int(lenght_track/1000000)
	print('==============================')
	print('            MENTALL           ')
	print('==============================')
	print ("Music: ",id_file)
	print("Lenght music: ",lenght_track,"min")
	playsound(id_file)
	print('==============================')
	print('                              ')
	print('==============================')
except:
	print('Пй')
	input('>')

