import os
path = 'C:/Users/Гусев/Desktop'
projectname = 'sort'
folders = \
['png',
'jpg',
'py']

fullPath = os.path.join(path , projectname)
if not os.path.exists(fullPath):
	os.mkdir(fullPath)
for f in folders:
	folder = os.path.join(fullPath, f)
	if not os.path.exists(folder):
		os.mkdir(folder)
