import glob,os
import shutil

for files in os.listdir("C:/Users/Гусев/Desktop/"):
	if files.endswith(".jpg"):
		os.remove(os.path.join("C:/Users/Гусев/Desktop/",files))

