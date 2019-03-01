import os.path, time
import os,glob
from shutil import copyfile
import shutil
import progressbar
def main():
	i = 0
	arr1=[0]*10
	surce_file=("C:\\Users\\Гусев\\Desktop\\Projects\\smagina\\test\\file.txt")
	surce_direct = ("C:\\Users\\Гусев\\Desktop\\Projects\\smagina")
	while i<666:
		file_delet = open(surce_file,'w')
		file_delet.close()
		for file in os.listdir(surce_direct):
			if file.endswith(".txt"):
				read_file = open(file,'r')
				s=read_file.read()
				
				file_file_txt=open(surce_file,'a')
				file_file_txt.write(s)
				
				file_file_txt.close()
				read_file.close()
				print("File detected")
			



		for x in progressbar.progressbar(range(100)):
			time.sleep(15/100)
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
		
		cur_dir = os.getcwd() 
		list_list=str(list_list)
		for char in '[,] ':
			list_list=list_list.replace(char,'')

		for i in range (0,quant_len):

			s1=name_arr[i]
			ls1=str(s1)
			s2=quantity_arr[i]
			ls2=str(s2)
			file_new=open('C:\\Users\\Гусев\\Desktop\\Projects\\smagina\\order\\'+list_list[i]+'.txt','w')
			file_new.write(ls1+ls2)
			file_new.close()

			cur_dir = os.getcwd()
			file_name = name_arr[i]

			file_list = os.listdir(cur_dir)
			parent_dir = os.path.dirname(cur_dir)	 
	
			if file_name in file_list:
				os.rename(file_name, list_list[i]+'.png')
				shutil.move(list_list[i]+'.png', "C:\\Users\\Гусев\\Desktop\\Projects\\smagina\\order")
				#copyfile("C:\\Users\\Гусев\\Desktop\\Projects\\smagina\\order",list_list[i]+'.png')
		      

	

	
if __name__ == '__main__':
	main()