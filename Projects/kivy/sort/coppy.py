import os
import zipfile
kuda = input()
otkuda = input()
fantasy_zip = zipfile.ZipFile(kuda, 'w')
 
for folder, subfolders, files in os.walk(otkuda):
 
    for file in files:
        if file.endswith('.jpg'):
            fantasy_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), otkuda), compress_type = zipfile.ZIP_DEFLATED)
 		
 
fantasy_zip.close()
