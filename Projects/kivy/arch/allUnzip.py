import zipfile
       
jungle_zip = zipfile.ZipFile('C:\\Users\\Гусев\\Desktop\\Project\\yes.zip', 'w')
jungle_zip.write('C:\\Users\\Гусев\\Desktop\\Project\\kim.jpg', compress_type=zipfile.ZIP_DEFLATED)
jungle_zip.close()