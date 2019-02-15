import random
import termcolor
import subprocess
import shutil
import webbrowser
import glob,os
from termcolor import colored
import os
def creat_file():#Функция генерации пароля, а также создания текстового файла содержащего пароли в будущем добавлю шифрование паролей
	Big = 'QWERTYUIOPASDFGHJKLZXCVBNM'
	Low = 'qwertyuiopasdfghjklzxcvbnm'
	Num = '1234567890'
	Spe = '!@#$%^&*()'
	BI = False
	LO = True
	NU = True
	PS = True 
	Password_len = input('Длинна пароля: ')


	if Password_len:
	   if Password_len.isdigit() == True:
	       Password_len = int(Password_len)
	   else:
	      print('Значение должно быть цифровым')
	      exit(0)
	else:
	   print('Выход ... Не указана длина паролей')
	   exit(0)

	Password_cou = input('Количество паролей в списке: ')
	print('\n')

	if Password_cou:
	   if Password_cou.isdigit() == True:
	       Password_cou = int(Password_cou)
	   else:
	      print('Значение должно быть цифровым')
	      exit(0)
	else:
	   print('Выход ... Не указано количество паролей ...')
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


	chose = input('Последний созданный список паролей будет безвозвратно удален (y/n) ?...')
	if chose == 'y':
		subprocess.call(['attrib', '-h', 'Password.txt'])
		file_Pass = open('Password.txt', 'w')
		file_Pass.write('\n'.join(psw))
		file_Pass.close()
		subprocess.call(['attrib', '+h', 'Password.txt'])
		print('Список паролей создан успешно >>>')

	if chose == 'n':
		return main()

	return main()

def dont_work():#Функция чтения изи файла и вывод паролей в консоль в будущем добавить ключ вводимы чтобы прочитать пароли
	password_key = input('Введите ключ доступа к файлу >>')
	if password_key == '2584':
		subprocess.call(['attrib', '-h', 'Password.txt'])
		if os.path.exists('Password.txt'):
			print('\n')
			f = open('Password.txt', 'r+')
			s= f.read()
			print (s)
			f.close()
			print('\n')
			subprocess.call(['attrib', '+h', 'Password.txt'])
			return main()
		else:
			print ('Файл не найден')
			return main()
	else:
		print ('Пароль неверен')
		return main()

def delete_file():#Функция удаления файла и проверка его существования
	subprocess.call(['attrib', '-h', 'Password.txt'])
	maybe = input('Удалить последний созданный файл (y/n)?...')
	if maybe =='y':
		
		os.remove(os.path.join('Password.txt'))
		print ('YOU KILL HIM !!!')
		section = input('Продолжить работу ? (y/n)')
		if section == 'y':
			return main()

	else:
		return main()
	




def main():
	#os.system("mode con cols=30 lines=10")#Размер окна

	print('==============================')
	print('            MENTALL           ')
	print('==============================')
	print ('1. Создать новый список паролей')
	print ('2. Открыть последний созданный список')
	print('3. Удалить список паролей')
	print ('4. Выйти')
	print('5. Открыть redme.txt')
	print('==============================')
	print('            ENDLINE            ')
	print('==============================')
	option = input('> ')#Выбор опции
	if option == '2':
		return dont_work()
	if option =='3':
		return delete_file()

	if option == '1':
		return creat_file()
	if option == '5':
		webbrowser.open('readme.txt')
		return main()
	if option == '4':
	   exit()
	
if __name__ == '__main__':
    main()
