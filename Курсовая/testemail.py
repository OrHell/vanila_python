import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
login  = "testname2584@gmail.com"
password  = "damdee2584"
url = "smtp.gmail.com"

addres = 'ya.iliagusev@gmail.com'
msg = MIMEMultipart()
msg['Subject'] = 'ОАО Алюминь'
msg['From'] = 'ya.iliagusev@gmail.com'
body = 'Ваш заказ помещен в очередь на обработку - время ожидания 456 дней.'
msg.attach(MIMEText(body,'plain'))

server = smtplib.SMTP_SSL(url, 465)
server.login(login,password)
server.sendmail(login, addres,msg.as_string())
server.quit()


