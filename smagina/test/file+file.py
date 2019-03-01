import glob,os
import random
import os
import os.path

surce2 =("C:\\Users\\Гусев\\Desktop\\Projects\\smagina\\test\\file.txt")
f=open(surce2,'r')
s= f.read()
f.close()
b=[0]
b=s.split("\n")
name_image = b[0]
quantity = b[1]


name_arr=name_image.split(';')
del name_arr[len(name_arr)-1]
#print(name_arr)


quantity_arr=quantity.split(';')
del quantity_arr[len(quantity_arr)-1]#delte element
y=1
x=0
i=0
quant_len=len(quantity_arr)
name_len = len(name_arr)+1
list_list =[]
for i in range(0,quant_len):
    list_list.append(i)

list_list=str(list_list)
for char in '[,] ':
    list_list=list_list.replace(char,'')

for i in range (0,quant_len):
    

    s1=name_arr[i]
    ls1=str(s1)
    s2=quantity_arr[i]
    ls2=str(s2)
    file_new=open(list_list[i]+'.txt','w')
    file_new.write(ls1+ls2)
    file_new.close()




    

file_name = name_arr[0]#file to be searched
cur_dir = os.getcwd() # Dir from where search starts can be replaced with any path
i=str(2)
while True:
    file_list = os.listdir(cur_dir)
    parent_dir = os.path.dirname(cur_dir)
    if file_name in file_list:
        os.rename(file_name, i+'.png')
        
    
input()