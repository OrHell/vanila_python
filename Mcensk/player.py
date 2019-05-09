import os
import os.path
import glob
import shutil
import webbrowser	

def sound_count(folder):
	count=0
	for folder, subfolder, files in os.walk(folder):
		for file in files:
			if file.endswith(".mp3"):
				count=count+1			
	return count


def list_music():
	count=sound_count('.\\Music\\')
	count=int(count)
	some_were_arg=0
	id_file=[]  
	folder = '.\\Music\\' 
	for folder, subfolder, files in os.walk(folder):
		for file in files:
			if file.endswith(".mp3"):		
				id_file.append(file)
	print("Кол-во файлов: ",count)
	print ("Enter -1 for exit")
	for some_were_arg in range(count):
		print(some_were_arg,id_file[some_were_arg])
	while True:
		choose = input(">")
		choose = int(choose)
		for some_were_arg in range(count):
			if choose == some_were_arg:
				print(id_file[choose])
				with open ("test.txt",'w') as file:
					file.write(folder+id_file[choose])
				webbrowser.open('tk.exe')
			if choose == -1:
				print ("\n" * 100)
				return main()
	return id_file

def playlist():
	print ("1.Create playlist")
	print ("2.Open playlist")
	choose = input('>')
	if choose == '1':
		return create_list()
	if choose == '2':
		return open_playlist()

def open_playlist():
	print(os.listdir('.\\Playlist\\'))
	name_playlist = input('Name playlist >')
	id_file=[]  
	folder = '.\\Playlist\\'+name_playlist+'\\'
	count=sound_count(folder)
	count=int(count)
	if count==0:
		print("Playlist has not found or music has not found\n ")
		return main()
	some_were_arg=0
	for folder, subfolder, files in os.walk(folder):
		for file in files:
			if file.endswith(".mp3"):		
				id_file.append(file)
	print("Кол-во файлов: ",count)
	print ("Enter -1 for exit")
	for some_were_arg in range(count):
		print(some_were_arg,id_file[some_were_arg])
	while True:
		choose = input("Trcak >")
		choose = int(choose)
		for some_were_arg in range(count):
			if choose == some_were_arg:
				print(id_file[choose])
				with open ("test.txt",'w') as file:
					file.write(folder+id_file[choose])
				webbrowser.open('tk.exe')
				
			if choose == -1:
				print ("\n" * 100)
				return main()
def create_list():
	file=open("test.txt",'w')
	file.close()
	name_playlist = input('Name playlist >')
	if not os.path.exists('.\\Playlist\\'+name_playlist+'\\'):
		os.makedirs('.\\Playlist\\'+name_playlist+'\\')
	folder = '.\\Music\\' 
	count=sound_count(folder)
	count=int(count)
	some_were_arg=0
	id_file=[]  
	
	playlist_folder='.\\Playlist\\'+name_playlist+"\\"
	for folder, subfolder, files in os.walk(folder):
		for file in files:
			if file.endswith(".mp3"):		
				id_file.append(file)
	print("Кол-во файлов: ",count)
	print ("Enter -1 for exit")
	for some_were_arg in range(count):
		print(some_were_arg,id_file[some_were_arg])
	while True:
		choose = input("Track >")
		choose = int(choose)
		for some_were_arg in range(count):
			if choose == some_were_arg:
				print(id_file[choose])
				try:
					shutil.copyfile(folder+id_file[choose],playlist_folder+id_file[choose] )
				except:
					print("Такая композиция уже присутсвует в плейлисте")
			if choose == -1:
				print ("\n" * 100)
				return main()
def main():
	os.system("mode con cols=30 lines=20")
	print ("\n" * 100)
	print('==============================')
	print('            MENTALL           ')
	print('==============================')
	print("1.My music")
	print("2.Playlists")
	print ("3.Exit")
	print('==============================')
	print('                              ')
	print('==============================')
	choose = input ('>')
	if choose == '1':
		return list_music()
	if choose == '2':
		return playlist()
	if choose == '3':
		exit()			
if __name__ == '__main__':
	main()

