import os.path, time
import os,glob
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
	
if __name__ == '__main__':
	main()