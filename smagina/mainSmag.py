import os.path, time
import os,glob
import subprocess
import webbrowser
from fpdf import FPDF
from docx import Document
from docx.shared import Inches
def check():
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
		file_new=open('C:\\Users\\Гусев\\Desktop\\Projects\\smagina\\order\\'+list_list[i]+'.txt','w')
		file_new.write(ls1+ls2)
		file_new.close()

	

	return main()
			
		


		
		
def dock_write():


	print('1.PDF')
	print('2.DOCX')
	print('3.TXT')
	print('4.Exit')
	option = input('>')
	if option == '1':
		pdf = FPDF()
		pdf.add_page()
		pdf.set_font("Arial", size=12)
		pdf.cell(200, 10, txt="Welcome to Python!", ln=1, align="C")
		pdf.output("1.pdf")
	if option == '2':
		pass
	if option == '3':
		pass
	if option == '4':
		return main()
def main():
	
	print('1.Start work')
	print('2.Find files')
	print('3.Exit')
	chose = input('>')
	if chose == '1':
		#webbrowser.open('find_file.py')
		return check()
	if chose =='2':
		webbrowser.open('find_file.py') 
		return main()  

	if chose == '3':
		exit()
if __name__ == '__main__':
	main()


	 
			
