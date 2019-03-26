import os.path, time
import os,glob
from shutil import copyfile
import shutil
import progressbar
def main():
	
	newpath = r'C:\\order' 
	if not os.path.exists(newpath):
		os.makedirs(newpath)
	i=0
	surce_file=("C:\\info\\file.txt")
	surce_direct = ("C:\\info")
	while i<666:
		file_delet = open(surce_file,'w')
		file_delet.close()
		file_quant_open= open('C:\\info\\QualityOrder.txt','r')
		file_name_image = open('C:\\info\\Name_imageOrder.txt','r')
		str_image = file_name_image.read()
		str_qunt = file_quant_open.read()
		file_quant_open.close()
		file_name_image.close()

		file_file_txt = open(surce_file,'w')
		file_file_txt.write(str_image+'\n'+str_qunt)
		file_file_txt.close()

		for x in progressbar.progressbar(range(100)):
			time.sleep(5/100)
		
		
		f=open('C:\\info\\file.txt','r')
		s= f.read()
		f.close()
		b=[0]
		
		b=s.split("\n")
		
		name_image = b[0]
		quantity = b[1]



		name_arr=name_image.split(';')
		del name_arr[len(name_arr)-1]
	


		quantity_arr=quantity.split(';')
		del quantity_arr[len(quantity_arr)-1]#delte element
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

			s1="Выполнить деталь в количестве :"
			ls1=str(s1)
			s2=quantity_arr[i]
			ls2=str(s2)
			file_new=open('C:\\order\\'+list_list[i]+'.txt','w')
			file_new.write(ls1+ls2+"шт")
			file_new.close()

			
			file_name = name_arr[i]
			cur_dir = 'C:\\info'
			#cur_dir = os.getcwd()
			file_list = os.listdir(cur_dir)
			parent_dir = os.path.dirname(cur_dir)	 
	
			if file_name in file_list:
				os.rename(file_name, list_list[i]+'.png')
				shutil.move(list_list[i]+'.png', "C:\\order")
				
if __name__ == '__main__':
	main()