import zipfile
import os
import time
import webbrowser	
def zip_direct():
	name_archive = input('Name:')
	source_ku = input ('Куда отправить архив:')
	source_ot  = input ('Откуда брать архив:')
	chislo = int(input('Time:'))
	i=0
	col_vo =int(input('ColVo:')) 
	while i<col_vo:
		fantasy_zip = zipfile.ZipFile(source_ku+name_archive+'.zip', 'w')
		for folder, subfolders, files in os.walk(source_ot):
			for file in files:
				fantasy_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), source_ot), compress_type = zipfile.ZIP_DEFLATED)      
		fantasy_zip.close()
		i=i+1
		#Добавить условие выхода из цикла 
		print (i,'- Архив создан')
		time.sleep(chislo)
	return main()
def main():	
	print('==============================')
	print('            MENTALL           ')
	print('==============================')
	user_name = input ('Username:')
	user_password = input('Password:')
	print('==============================')
	print('            ENDLINE            ')
	print('==============================')
	if user_name == '2584' and user_password == '2584':
		return zip_direct()
	else:
		return main()
if __name__ == '__main__':
	main()
       

	 
			
	 
			    