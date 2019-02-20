import zipfile
import os
import time
import progressbar
import webbrowser	
#from tqdm import tqdm
def auth_user():
	user_name = input ('Username:')
	user_password = input('Password:')
	if user_name == '2584' and user_password == '2584':
		return zip_direct()
	else:
		return main()
def zip_direct():
	name_archive = input('Name zipfile:')
	source_ku = input ('Save location zipfile:')
	source_ot  = input ('File Copy Location:')
	chislo = int(input('Time:'))
	i=0
	x=1
	col_vo =int(input('Quantity:')) 
	while i<col_vo:
		fantasy_zip = zipfile.ZipFile(source_ku+name_archive+'.zip', 'w')
		for folder, subfolders, files in os.walk(source_ot):
			for file in files:
				fantasy_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), source_ot), compress_type = zipfile.ZIP_DEFLATED)      
		fantasy_zip.close()
		i=i+1
		for x in progressbar.progressbar(range(100)):
			time.sleep(chislo/100)
		print (i,'- Archiving was successful - No errors found')		
	return main()
def main():	
	print('==============================')
	print('            MENTALL           ')
	print('==============================')
	print('1. Start backup')
	print('2. Open Readme')
	print('3. Exit')
	print('==============================')
	print('            ENDLINE            ')
	print('==============================')
	option  = input('>')
	if option == '1':
		return auth_user()
	if option == '2':
		
		read_me =open ('readme.txt','w')
		read_me.write("Username and Password: 2584")
		read_me.close()
		webbrowser.open('readme.txt')
		return main()
	if option == '3':
		exit()
if __name__ == '__main__':
	main()
       

	 
			
	 