import os
import subprocess
import webbrowser
def sound_count(folder):
	count=0
	for folder, subfolder, files in os.walk(folder):
		for file in files:
			if file.endswith(".mp3"):
				count=count+1			
	return count # Возвращает колво песенок в папке
def main():
	i=sound_count('C:\\sort') # Обращается к функции подсчета песен с путем folder 
	print (i) # выводит колво песен в указанном пути
if __name__ == '__main__':
	main()
