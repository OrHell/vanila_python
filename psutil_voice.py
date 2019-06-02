
import os 
import psutil
import time 

import pyttsx3
import datetime


engine = pyttsx3.init()
engine.say("Пробудись спящий")
engine.runAndWait()
'''today = datetime.datetime.now()#.strftime("%Y-%m-%d %H:%M:%S")
	now = datetime.datetime.fromtimestamp(psutil.boot_time())#.strftime("%Y-%m-%d %H:%M:%S")#Время с включения пк
	delta = today - now  #delta.minute.strftime("%Y-%m-%d %H:%M:%S")
	time_power = delta.seconds
	time_power=time_power/3600
	time_power = toFixed(time_power,2)
	time_power =  str(time_power)
	some_were = dict(psutil.virtual_memory()._asdict())
	ozu  =toFixed(some_were['free']/1000000000,2)

		if voice == 'сколько процентов' or 'цп' or 'загрузка процессора':
			cpi_stat = str(psutil.cpu_percent(interval=1))
			speak("Загрузка процессора"+cpi_stat+"процента"+"Свободно оперативной памяти"+ozu+"гигабайт"+"Компьютер раотает"+time_power+"Часов")
			return callback()
		else:
			speak("Нихрена не понял давай по новой")
			
	
	except sr.UnknownValueError:
		print("[log] Голос не распознан!")
	except:
		print("[log] Неизвестная ошибка, проверьте интернет!")'''



