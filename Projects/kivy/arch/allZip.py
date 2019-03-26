import os
import zipfile
 
fantasy_zip = zipfile.ZipFile('C:\\Users\\Гусев\\Desktop\\Project\\py_and_txt.zip', 'w')
 
for folder, subfolders, files in os.walk('C:\\Users\\Гусев\\Desktop\\Project'):
 
    for file in files:
        if file.endswith('.py'):
            fantasy_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), 'C:\\Users\\Гусев\\Desktop\\Project'), compress_type = zipfile.ZIP_DEFLATED)
 		
 
fantasy_zip.close()
