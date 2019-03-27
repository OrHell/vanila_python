import os.path,time
import os,glob
from shutil import copyfile
import shutil
import progressbar
def leght_frag():
	with open ('C:\\info\\QualityOrder.txt','r') as leng_string:
		leng_string =leng_string.read()
	delet_symb = ";"
	leng = leng_string.count(delet_symb)
	return leng
def path_created():
	new_path = r'C:\\order'
	if not os.path.exists(new_path):
		os.makedir(new_path)
def main():
	file_quant = 'C:\\info\\QualityOrder.txt'
	file_image = 'C:\\info\\Name_imageOrder.txt'
	while True:
		with open(file_quant,'r') as text_quant:
			str_quant = text_quant.read()
		with open(file_image, 'r') as text_image:
			str_image =text_image.read()
		for x in progressbar.progressbar(range(100)):
			time.sleep(5/100)
		lenght_for = leght_frag()
		name = str_image.split(';')
		quant = str_quant.split(';')
		del name[len(name)-1]
		del quant[len(quant)-1]
		id_list=[]
		for i in range(0,lenght_for):
			id_list.append(i)
		id_list=str(id_list)
		for char in '[,] ':
			id_list=id_list.replace(char,'')
		for i in range(0,lenght_for):
			str_one = "Выполнить деталь "
			str_two = name[i]
			str_three = " в количестве: "
			str_four = quant[i]
			ls_one =str(str_one)
			ls_two = str(str_two)
			ls_three =str(str_three)
			ls_four =str(str_four)
			with open('C:\\order\\'+id_list[i]+'.txt','w') as order_file:
				order_file.write(ls_one+ls_two+ls_three+ls_four+" шт")
			image_name = name[i]
			file_list=os.listdir('C:\\info')
			parent_dir = os.path.dirname('C:\\info')
			try:
				if image_name in file_list:
					os.rename("C:\\info\\"+image_name, id_list[i]+'.png')
					shutil.move(id_list[i]+'.png',"C:\\order")
				if image_name in file_list:
					os.rename("C:\\info\\"+image_name, id_list[i]+'.jpg')
					shutil.move(id_list[i]+'.jpg',"C:\\order")
			except:
				return main()
if __name__ == '__main__':
	main()