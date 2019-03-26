import sys, os
import time
import requests, bs4
import webbrowser
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
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.progressbar import ProgressBar
from kivy.uix.textinput import TextInput

#from kivy.core.window import Window
#Window.clearcolor = (1, 1, 0, 20)

Config.set('graphics','resizeble','0');##Изминения чтобы окошко не двигалось
Config.set('graphics','width','480');##Изминения ширина
Config.set('graphics','height','240');##Изминение высоты


class BoxApp(App):
	def build(self):
		al = AnchorLayout()
		gl = GridLayout(rows = 2, cols=2,size_hint =[None,None],size = [480,60])
		bl = BoxLayout(orientation= 'vertical')
		self.lbl = Label(text = "")
		self.pb = ProgressBar(value = 0,max = 100)

		self.texi = TextInput(multiline=False)
		self.texit = TextInput(multiline=False,password = True)
		self.lblt = Label(text = "Путь:")
		self.lbly = Label(text = "Пароль:")
		
		bl.add_widget(self.lbl)
		bl.add_widget(self.pb)

		gl.add_widget(self.lblt)
		gl.add_widget(self.texi)#Путь
		

		gl.add_widget(self.lbly)
		gl.add_widget(self.texit)#Пароль

		
		
		bl.add_widget(Button(text = "Зашифровать файл", on_press = self.btn_press))
		bl.add_widget(Button(text = "Дешифровать файл", on_press = self.btn_press_desh))
		
		bl.add_widget(gl)
		al.add_widget(bl)
		return al
	def btn_press_desh(self,instance):
	
		if ((self.texit.text == '2584') and (self.texi.text.endswith('.txt'))):
			source  = self.texi.text
			p=open(source, 'r')
			s=p.read()
			data = s
			alphavit = [("p", "q"),
					    ("o", "w"), 
					    ("i", "e"), 
					    ("u", "r"), 
					    ("y", "t"), 
					    ("t", "y"),
			             ("r", "u"), 
			             ("e", "i"), 
			             ("w", "o"), 
			             ("q", "p"), 
			             ("l", "a"), 
			             ("k", "s"),
			             ("j", "d"), 
			             ("h", "f"), 
			             ("g", "g"), 
			             ("f", "h"), 
			             ("d", "j"), 
			             ("s", "k"),
			             ("a", "l"), 
			             ("z", "m"), 
			             ("x", "n"), 
			             ("c", "b"), 
			             ("v", "v"), 
			             ("b", "c"),
			             ("n", "x"), 
			             ("m", "z"), 

			             ("P", "Q"),
					    ("O", "W"), 
					    ("I", "E"), 
					    ("U", "R"), 
					    ("Y", "T"), 
					    ("T", "Y"),
			             ("R", "U"), 
			             ("E", "I"), 
			             ("W", "O"), 
			             ("Q", "P"), 
			             ("L", "A"), 
			             ("K", "S"),
			             ("J", "D"), 
			             ("H", "F"), 
			             ("G", "G"), 
			             ("F", "H"), 
			             ("D", "J"), 
			             ("S", "K"),
			             ("A", "L"), 
			             ("Z", "M"), 
			             ("X", "N"), 
			             ("C", "B"), 
			             ("V", "V"), 
			             ("B", "C"),
			             ("N", "X"), 
			             ("M", "Z"), 


			             ("ъ", "й"), 
			             ("х", "ц"), 
			             ("з", "у"), 
			             ("щ", "к"),
			             ("щ", "е"), 
			             ("г", "н"), 
			             ("н", "г"), 
			             ("е", "ш"), 
			             ("к", "щ"), 
			             ("у","з"),
			             ("ц", "х"), 
			             ("й", "ъ"), 
			             ("э", "ф"), 
			             ("ж", "ы"), 
			             ("д", "в"), 
			             ("л","а"),
			             ("о", "п"), 
			             ("р", "р"), 
			             ("п", "о"), 
			             ("а", "л"), 
			             ("в", "д"), 
			             ("ы","ж"),
			             ("ф", "э"),
			             ("ю", "я"), 
			             ("б", "ч"), 
			             ("ь", "с"), 
			             ("т", "м"), 
			             ("и","и"),
			             ("м", "т"), 
			             ("с", "ь"), 
			             ("ч", "б"), 
			             ("я", "ю"), 
			             
			             ("Ъ", "Й"), 
			             ("Х", "Ц"), 
			             ("З", "У"), 
			             ("Щ", "К"),
			             ("Щ", "Е"), 
			             ("Г", "Н"), 
			             ("Н", "Г"), 
			             ("Е", "Ш"), 
			             ("К", "Щ"), 
			             ("У","З"),
			             ("Ц", "Х"), 
			             ("Й", "Ъ"), 
			             ("Э", "Ф"), 
			             ("Ж", "Ы"), 
			             ("Д", "В"), 
			             ("Л","А"),
			             ("О", "П"), 
			             ("Р", "Р"), 
			             ("П", "О"), 
			             ("А", "Л"), 
			             ("В", "Д"), 
			             ("Ы","Ж"),
			             ("Ф", "Э"),
			             ("Ю", "Я"), 
			             ("Б", "Ч"), 
			             ("Ь", "С"), 
			             ("Т", "М"), 
			             ("И","И"),
			             ("М", "Т"), 
			             ("С", "Ь"), 
			             ("Ч", "Б"), 
			             ("Я", "Ю"), 
			             (" ", " ")]
			 
			lester =data.translate(str.maketrans(dict(alphavit)))
			print(data.translate(str.maketrans(dict(alphavit))))
			p.close
			f = open (source,'w')
			f.close
			d = open (source,'a')
			d.write(lester)
			d.close

			
				
			self.pb.value =100
			self.lbl.text = ('Файл дешифрован :3')
			webbrowser.open(source)
			
		else:
			self.pb.value =0
			self.lbl.text = ('Пароль неверен или путь указан неверно :3')
	def btn_press(self, instance):
		if ((self.texit.text == '2584') and (self.texi.text.endswith('.txt'))):
			source  = self.texi.text
			p=open(source, 'r')
			s=p.read()
			data = s
			alphavit = [("q", "p"),
					    ("w", "o"), 
					    ("e", "i"), 
					    ("r", "u"), 
					    ("t", "y"), 
					    ("y", "t"),
			             ("u", "r"), 
			             ("i", "e"), 
			             ("o", "w"), 
			             ("p", "q"), 
			             ("a", "l"), 
			             ("s", "k"),
			             ("d", "j"), 
			             ("f", "h"), 
			             ("g", "g"), 
			             ("h", "f"), 
			             ("j", ">d"), 
			             ("k", "s"),
			             ("l", "a"), 
			             ("m", "z"), 
			             ("n", "x"), 
			             ("b", "c"), 
			             ("v", "v"), 
			             ("c", "b"),
			             ("x", "n"), 
			             ("z", "m"), 

			             ("й", "ъ"),
			             ("ц", "х"), 
			             ("у", "з"), 
			             ("к", "щ"),
			             ("е", "ш"), 
			             ("н", "г"), 
			             ("г", "н"), 
			             ("ш", "е"), 
			             ("щ", "к"), 
			             ("з","у"),
			             ("х", "ц"), 
			             ("ъ", "й"), 
			             ("ф", "э"), 
			             ("ы", "ж"), 
			             ("в", "д"), 
			             ("а","л"),
			             ("п", "о"), 
			             ("р", "р"), 
			             ("о", "п"), 
			             ("л", "а"), 
			             ("д", "в"), 
			             ("ж","ы"),
			             ("э", "ф"),
			             ("я", "ю"), 
			             ("ч", "б"), 
			             ("с", "ь"), 
			             ("м", "т"), 
			             ("и","и"),
			             ("т", "м"), 
			             ("ь", "с"), 
			             ("б", "ч"), 
			             ("ю", "я"), 
			           
			             ("Q", "P"),
						("W", "O"), 
						("E", "I"), 
						("R", "U"), 
						("T", "Y"), 
						("Y", "T"),
						("U", "R"), 
						("I", "E"), 
						("O", "W"), 
						("P", "Q"), 
						("A", "L"), 
						("S", "K"),
						("D", "J"), 
			             ("F", "H"), 
			             ("G", "G"), 
			             ("H", "F"), 
			             ("J", ">D"), 
			             ("K", "S"),
			             ("L", "A"), 
			             ("M", "Z"), 
			             ("N", "X"), 
			             ("B", "C"), 
			             ("V", "V"), 
			             ("C", "B"),
			             ("X", "N"), 
			             ("Z", "M"),

			             ("Й", "Ъ"), 
			             ("Ц", "Х"), 
			             ("У", "З"), 
			             ("К", "Щ"),
			             ("Е", "Ш"), 
			             ("Н", "Г"), 
			             ("Г", "Н"), 
			             ("Ш", "Е"), 
			             ("Щ", "К"), 
			             ("З","У"),
			             ("Х", "Ц"), 
			             ("Ъ", "Й"), 
			             ("Ф", "Э"), 
			             ("Ы", "Ж"), 
			             ("В", "Д"), 
			             ("А","Л"),
			             ("П", "О"), 
			             ("Р", "Р"), 
			             ("О", "П"), 
			             ("Л", "А"), 
			             ("Д", "В"), 
			             ("Ж","Ы"),
			             ("Э", "Ф"),
			             ("Я", "Ю"), 
			             ("Ч", "Б"), 
			             ("С", "Ь"), 
			             ("М", "Т"), 
			             ("И","И"),
			             ("Т", "М"), 
			             ("Ь", "С"), 
			             ("Б", "Ч"), 
			             ("Ю", "Я"), 
			             (" ", " "),]
			 
			lester =data.translate(str.maketrans(dict(alphavit)))
			print(data.translate(str.maketrans(dict(alphavit))))
			p.close
			f = open (source,'w')
			f.close
			d = open (source,'a')
			d.write(lester)
			d.close

			self.lbl.text = ('Файл зашифрован :3')
			self.pb.value = 100
			webbrowser.open(source)
		else:
			self.pb.value =0
			self.lbl.text = ('Пароль неверен или путь указан неверно :3')
	
	
	

			


		


if __name__ == "__main__":##
	 BoxApp().run()##



