import glob,os
import shutil
import zipfile
print("Введите путь копирования, формата C:/Users/username/../name.zip :")
kuda = input()
print("Введите путь откуда, формата C:/Users/username/../ :")
otkuda = input()
print("Введите расширение файлов :")
raspr = input()
fantasy_zip = zipfile.ZipFile(kuda, 'w')
 
for folder, subfolders, files in os.walk(otkuda):
 
    for file in files:
        if file.endswith(raspr):
            fantasy_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), otkuda), compress_type = zipfile.ZIP_DEFLATED)
 		
 
fantasy_zip.close()

for files in os.listdir(otkuda):
	if files.endswith(raspr):
		os.remove(os.path.join(otkuda,files))

