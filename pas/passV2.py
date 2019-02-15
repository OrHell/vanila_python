import random
import termcolor
import subprocess
import shutil
import glob,os
from termcolor import colored
import os
def creat_file():
	Big = 'QWERTYUIOPASDFGHJKLZXCVBNM'
	Low = 'qwertyuiopasdfghjklzxcvbnm'
	Num = '1234567890'
	Spe = '!@#$%^&*()'
	BI = False
	LO = True
	NU = True
	PS = True 
	Password_len = input('Length passwords: ')


	if Password_len:
	   if Password_len.isdigit() == True:
	       Password_len = int(Password_len)
	   else:
	      print('Output ... Value must be digital ..')
	      exit(0)
	else:
	   print('Exit ... No Password Length specified ...')
	   exit(0)

	Password_cou = input('Number of passwords: ')
	print('\n')

	if Password_cou:
	   if Password_cou.isdigit() == True:
	       Password_cou = int(Password_cou)
	   else:
	      print('Output ... Value must be digital ...')
	      exit(0)
	else:
	   print('Logout ... No number of passwords specified ...')
	   exit(0)

	Pass_Symbol = []
	if BI == True:
	   Pass_Symbol.extend(list(Big))

	if LO == True:
	   Pass_Symbol.extend(list(Low))

	if NU == True:
	   Pass_Symbol.extend(list(Num))

	if PS == True:
	   Pass_Symbol.extend(list(Spe))

	random.shuffle(Pass_Symbol)
	psw = []

	for yx in range(Password_cou):
	   psw.append(''.join([random.choice(Pass_Symbol) for x in range(Password_len)]))


	chose = input('Old pass have been rewrite - continue (yes/no) ?...')
	if chose == 'yes':
		file_Pass = open('Password.txt', 'w')
		file_Pass.write('\n'.join(psw))
		file_Pass.close()
		subprocess.call(['attrib', '+h', 'Password.txt'])
		print('File created successfully >>>')

	if chose == 'no':
		return main()

	return main()

def dont_work():

	print('\n')
	f = open('Password.txt', 'r+')
	s= f.read()
	print (s)
	f.close()
	print('\n')
	return main()


def delete_file():
	maybe = input('Delete last file (yes/no)?...')
	if maybe =='yes':
		last_file = input('Enter name file: ')
		os.remove(os.path.join(last_file))
		print ('YOU KILL HIM !!!')

	else:
		return main()
	return main()




def main():
	os.system("mode con cols=30 lines=10")

	print('==============================')
	print('            MENTALL          ')
	print('==============================')
	print ('1. Create')
	print ('2. Open file')
	print('3. Delete file')
	print ('4. Exit')
	option = input('> ')
	if option == '2':
		return dont_work()
	if option =='3':
		return delete_file()

	if option == '1':

		return creat_file()
	if option == '4':
	   exit()
if __name__ == '__main__':
    main()
