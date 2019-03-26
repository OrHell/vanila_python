import glob,os
import shutil
import zipfile##Импорт архивации
from kivy.app import App##Импорт киви
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config##Импорт изменения окошка
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.progressbar import ProgressBar
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
#from kivy.core.window import Window
#Window.clearcolor = (1, 1, 0, 20)

Config.set('graphics','resizeble','0');##Изминения чтобы окошко не двигалось
Config.set('graphics','width','520');##Изминения ширина
Config.set('graphics','height','280');##Изминение высоты


class BoxApp(App):
	def build(self):
		al = AnchorLayout()
		gl = GridLayout(rows = 3, cols=2,size_hint =[None,None],size = [480,80])
		bl = BoxLayout(orientation= 'vertical')

		
		self.lbl = Label(text = "")

		self.texi = TextInput(multiline=False)
		self.texit = TextInput(multiline=False)
		self.texet = TextInput(multiline=False)
		self.lbli = Label(text = "Куда:")
		self.lblit = Label(text = "Откуда:")
		self.lble = Label(text = "Расширение:")

		self.pb = ProgressBar(value = 0,max = 100)

		gl.add_widget(self.lbli)
		gl.add_widget(self.texi)

		gl.add_widget(self.lblit)
		gl.add_widget(self.texit)

		gl.add_widget(self.lble)
		gl.add_widget(self.texet)
		
		
		
		
		

		bl.add_widget(self.lbl)
		bl.add_widget(self.pb)


		#bl.add_widget(Button(text = "Указать путь", on_press = self.btn_press_surce))
		#bl.add_widget(Button(text = "Создать Папки", on_press = self.btn_press))
		bl.add_widget(Button(text = "Сожмать ", on_press = self.btn_press_jpg))
		bl.add_widget(gl)
		al.add_widget(bl)
		return al
	#def btn_press_surce(self, instance):
	#	kuda  = self.texi.text
		#otkuda  = self.texit.text
		#raspr  = self.texet.text

	#def btn_press(self,instance):
		#path = 'C:\\'
		#projectname = 'sort'
		#folders = \
		#['picture',
		#'py']

		#fullPath = os.path.join(path , projectname)
		#if not os.path.exists(fullPath):
		#	os.mkdir(fullPath)
		#for f in folders:
		#	folder = os.path.join(fullPath, f)
			
	#		if not os.path.exists(folder):
	#			os.mkdir(folder)

#		self.lbl.text = ('Папки созданы :3')
#		self.pb.value = 100

	
	
	def btn_press_jpg(self,instance):
		if (self.texi.text.endswith('.zip') ):
			kuda  = self.texi.text
			otkuda  = self.texit.text
			raspr  = self.texet.text
			fantasy_zip = zipfile.ZipFile(kuda, 'w')
	 
			for folder, subfolders, files in os.walk(otkuda):
	 
			    for file in files:
			        if file.endswith(raspr):
			             fantasy_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), otkuda), compress_type = zipfile.ZIP_DEFLATED)
			        
			fantasy_zip.close()



			for files in os.listdir(otkuda):
				if files.endswith(raspr):
					os.remove(os.path.join(otkuda,files))
				
			

			self.lbl.text = ('Архив готов :3')
			self.pb.value = 100
		else:
			self.pb.value =0
			self.lbl.text = ('Что то пошло не так :3')
	

			


		


if __name__ == "__main__":##
	 BoxApp().run()##