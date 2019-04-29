import psutil
import datetime
def toFixed(time_power, digits=0):
    return f"{time_power:.{digits}f}"
today = datetime.datetime.now()#.strftime("%Y-%m-%d %H:%M:%S")
now = datetime.datetime.fromtimestamp(psutil.boot_time())#.strftime("%Y-%m-%d %H:%M:%S")#Время с включения пк
delta = today - now  #delta.minute.strftime("%Y-%m-%d %H:%M:%S")
time_power = delta.seconds
time_power=time_power/3600
time_power = toFixed(time_power,2)

print(today)
print(now) 
print("Время работы ПК: ",time_power) #Время с включения пк
print("Загрузка CPU: ",psutil.cpu_percent(interval=1),"%") #Загрузка процессора
print("Заряд батареи: ",psutil.sensors_battery()) #батарея
print("Кол-во ядер CPU: ",psutil.cpu_count())
print(psutil.cpu_stats())
#psutil.sensors_temperatures()
