import os.path, time
import os,glob
from shutil import copyfile
import shutil
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def order ():
	name_input = input("Введите свое имя:")
	surname_input= input("Введите свою фамилию:")
	email_input = input("Введите адресс эллектронной почты:")
	image_input = input ("Введите имя чертежа:")
	quant_input= input("Введите количество детали:")
	addres_input= input("Введите свое адресс доставки:")

	file_create = open("C:\\info\\client\\client_info.txt",'r')
	file_create.close()

	info_file = open ("C:\\info\\client\\client_info.txt",'a')
	info_file.write("\n"+"Имя: "+name_input+"\n"+"Фамиилия: "+surname_input+"\n"+"Доставка: "+addres_input+"\n"+"Почта: "+email_input+"\n")
	info_file.close()

	image_file = open("C:\\info\\name_image.txt",'a')
	image_file.write(image_input+";")
	image_file.close()

	quant_file= open ("C:\\info\\quant.txt",'a')
	quant_file.write(quant_input+";")
	quant_file.close()

	shutil.move(image_input, "C:\\info")

	login  = "testname2584@gmail.com"
	password  = "damdee2584"
	url = "smtp.gmail.com"

	#addres = 'ya.iliagusev@gmail.com'
	msg = MIMEMultipart()
	msg['Subject'] = 'ОАО Алюминь'
	msg['From'] = 'ya.iliagusev@gmail.com'
	body = 'Ваш заказ помещен в очередь на обработку - время ожидания 456 дней.'
	msg.attach(MIMEText(body,'plain'))

	server = smtplib.SMTP_SSL(url, 465)
	server.login(login,password)
	server.sendmail(login, email_input,msg.as_string())
	server.quit()

	print ('Ваш заказ принят ожидайте...')
	print ('\n' * 15)

	return main()
	
def main ():
	newpath = r'C:\\info\\client' 
	if not os.path.exists(newpath):
		os.makedirs(newpath)
	print("1.Создаь заказ")
	print("2.Выход")
	choose = input(">")
	if choose =='1':
		return order()
	if choose == '2':
		exit()
if __name__ == '__main__':
	main()