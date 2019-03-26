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
	password_list_name_tree = input('Введите имя файла:')
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


	chose = input('Последний созданный список паролей с одинаковым именем будет безвозвратно удален (y/n) ?...')
	if chose == 'y':
		subprocess.call(['attrib', '-h',  password_list_name_tree+'.txt'])
		file_Pass = open( password_list_name_tree+'.txt', 'w')
		file_Pass.write('\n'.join(psw))
		file_Pass.close()
		subprocess.call(['attrib', '+h',  password_list_name_tree+'.txt'])
		print('Список паролей создан успешно >>>')

	if chose == 'n':
		return main()

	return main()

def dont_work():#Функция чтения изи файла и вывод паролей в консоль в будущем добавить ключ вводимы чтобы прочитать пароли
	password_list_name_two = input('Введите имя файла:')
	password_key = input('Введите ключ доступа к файлу >>')
	if password_key == '2584':
		subprocess.call(['attrib', '-h',  password_list_name_two+'.txt'])
		if os.path.exists(password_list_name_two+'.txt'):
			print('\n')
			f = open(password_list_name_two+'.txt', 'r+')
			s= f.read()
			print (s)
			f.close()
			print('\n')
			subprocess.call(['attrib', '+h', password_list_name_two+'.txt'])
			return main()
		else:
			print ('Файл не найден')
			return main()
	else:
		print ('Пароль неверен')
		return main()

def delete_file():#Функция удаления файла и проверка его существования
	password_list_name = input('Введите имя файла:')
	password_key_two = input('Введите ключ доступа к файлу >>')
	if password_key_two == '2584':
		subprocess.call(['attrib', '-h', password_list_name+'.txt'])
		maybe = input('Удалить этот файл (y/n)?...')
		if maybe =='y':
			
			os.remove(os.path.join(password_list_name+'.txt'))
			print ('YOU KILL HIM !!!')
			section = input('Продолжить работу ? (y/n)')
			if section == 'y':
				return main()

		else:
			print ('Пароль неверен')
			return main()
def password_generation_func():
	lsiting_1 = 'qwertyuiopasdfghjklzxcvbnm'
	lsiting_2 = '1234567890'
	lsiting_3 = lsiting_1.upper()
	listing_4 = lsiting_1+lsiting_3+lsiting_2
	lis = list(listing_4)
	random.shuffle(lis)
	password_generation = ''.join([random.choice(lis) for x in range(10)])
	print(password_generation)
	okey = input('Сгенерировать другой ?(y/n)')
	if okey =='y':
		return password_generation_func()
	else:
		yorself_pas_name = input('От чего он:')
		file_your_pass_two = input('В какой список записать ваш пароль:')
		subprocess.call(['attrib', '-h', file_your_pass_two +'.txt'])
		yorself_pas = open(file_your_pass_two+'.txt', 'a')
		yorself_pas.write('\n'+yorself_pas_name+':'+password_generation)
		yorself_pas.close()
		print ('Ваш пароль был успешно добавлен :3')
		subprocess.call(['attrib', '+h', file_your_pass_two +'.txt'])
		return main()


def yorself_password():
	print('1.Сгенерировать')
	print('2.Записать самому')
	choose_two = input('>')
	if choose_two == '1':
		return password_generation_func()
		
	else:
		your_pass = input('Введите свой пароль:')
		yorself_pas_name = input('От чего он:')
		file_your_pass = input('В какой список записать ваш пароль:')
		subprocess.call(['attrib', '-h', file_your_pass +'.txt'])
		yorself_pas = open(file_your_pass+'.txt', 'a')
		yorself_pas.write('\n'+yorself_pas_name+':'+ your_pass)
		yorself_pas.close()
		subprocess.call(['attrib', '+h', file_your_pass +'.txt'])
		print ('Ваш пароль был успешно добавлен :3')
		return main()

	



def main():
	#os.system("mode con cols=30 lines=10")#Размер окна

	print('==============================')
	print('            MENTALL           ')
	print('==============================')
	print ('1. Создать новый список паролей')
	print ('2. Открыть список')
	print('3. Удалить список паролей')
	print ('4. Добавить свой пароль к списку')
	print ('5. Выйти')
	print('6. Открыть redme.txt')
	print('==============================')
	print('            ENDLINE            ')
	print('==============================')
	option = input('> ')#Выбор опции
	if option == '2':
		return dont_work()
	if option =='3':
		return delete_file()
	if option =='4':
		return yorself_password()

	if option == '1':
		return creat_file()
	if option == '6':
		read_me =open ('readme.txt','w')
		read_me.write("Username and Password: 2584")
		read_me.close()
		webbrowser.open('readme.txt')
		return main()
	if option == '5':
	   exit()
	
if __name__ == '__main__':
    main()
