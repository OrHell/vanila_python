
import psutil
import os.path,time
import datetime
def toFixed(time_power, digits=0):
    return f"{time_power:.{digits}f}"
while True:
	today = datetime.datetime.now()#.strftime("%Y-%m-%d %H:%M:%S")
	now = datetime.datetime.fromtimestamp(psutil.boot_time())#.strftime("%Y-%m-%d %H:%M:%S")#Время с включения пк
	delta = today - now  #delta.minute.strftime("%Y-%m-%d %H:%M:%S")
	time_power = delta.seconds
	time_power=time_power/3600
	time_power = toFixed(time_power,2)
	some_were = dict(psutil.virtual_memory()._asdict())

	print("RAM")
	print("------------------------------------------------")
	print("All: ",toFixed(some_were['total']/1000000000,2))
	print("Free: ",toFixed(some_were['free']/1000000000,2))
	print("Used: ",toFixed(some_were['used']/1000000000,2))
	print("Percent: ",some_were['percent'],"%")
	print("PC")
	print("------------------------------------------------")
	print("Time Work: ",time_power) #Время с включения пк
	print("CPU%: ",psutil.cpu_percent(interval=1),"%") #Загрузка процессора
	print("Battery: ",psutil.sensors_battery()) #батарея
	#print("Кол-во ядер CPU: ",psutil.cpu_count())
	print("------------------------------------------------")
	
	time.sleep(500/100)
	


