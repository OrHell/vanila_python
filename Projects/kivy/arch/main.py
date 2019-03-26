import os
import zipfile##Импорт архивации
from kivy.app import App##Импорт киви
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput##импорт кнопачек
from kivy.config import Config##Импорт изменения окошка
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout

Config.set('graphics','resizeble','0');##Изминения чтобы окошко не двигалось
Config.set('graphics','width','320');##Изминения ширина
Config.set('graphics','height','240');##Изминение высоты

class BoxApp(App):
	def build(self):
		self.formula = "0"
		al = AnchorLayout()
		bl = BoxLayout(orientation= 'vertical',size_hint =[.4,.4])
		bl.add_widget(TextInput(text = "C:\\Users\\Mentall\\Desktop\\Project\\Arch\\kim.jpg", font_size = "12"))
		bl.add_widget(Button(text="Save", on_press = self.btn_pressss,font_size = "14"))
		bl.add_widget(Button(text = "Zip", on_press = self.btn_press,font_size = "14"))
		bl.add_widget(Button(text = "AllZip",on_press = self.btn_presss,font_size = "14"))
		al.add_widget(bl)
		return al
		



	def btn_pressss(self,instance):
		instance = b = print ('Pisa is jopi')


	def btn_press(self, instance):##Сам класс архивации
		instance = jungle_zip = zipfile.ZipFile('yes.zip', 'w')
		jungle_zip.write('kim.jpg', compress_type=zipfile.ZIP_DEFLATED)
		jungle_zip.close()##Конец
		
	
	
		
	
	def btn_presss(self, instance):##Сам этот класс разорхивации
		instance = fantasy_zip = zipfile.ZipFile('yes_two.zip', 'w')
		for folder, subfolders, files in os.walk('C:\\Users\\Гусев\\Desktop\\Project\\Arch'):
			for file in files:
				if file.endswith('.py'):
					fantasy_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), 'C:\\Users\\Гусев\\Desktop\\Project\\Arch'), compress_type = zipfile.ZIP_DEFLATED)
		fantasy_zip.close()
		
 		


if __name__ == "__main__":##
	 BoxApp().run()##

