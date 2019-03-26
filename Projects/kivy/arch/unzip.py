import zipfile

fantasy_zip = zipfile.ZipFile('C:\\Users\\Гусев\\Desktop\\Project\\yes.zip')
fantasy_zip.extractall('C:\\Users\\Гусев\\Desktop\\Project\\zip\\kim.jpg')
fantasy_zip.close()