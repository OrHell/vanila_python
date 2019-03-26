import sys, os
import requests
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
#from kivy.core.window import Window
#Window.clearcolor = (1, 1, 0, 20)

Config.set('graphics','resizeble','0');##Изминения чтобы окошко не двигалось
Config.set('graphics','width','480');##Изминения ширина
Config.set('graphics','height','240');##Изминение высоты


class BoxApp(App):
	def build(self):
		al = AnchorLayout()

		bl = BoxLayout(orientation= 'vertical')
		self.texi = TextInput(multiline=False)
		self.lbl = Label(text = "")
		self.texit = TextInput(multiline=False)
		self.pb = ProgressBar(value = 0,max = 100)
		bl.add_widget(self.lbl)
		bl.add_widget(self.pb)
		bl.add_widget(self.texi)
		bl.add_widget(self.texit)
		bl.add_widget(Button(text = "Зашифровать файл", on_press = self.btn_press))
		bl.add_widget(Button(text = "Дешифровать файл", on_press = self.btn_press_desh))
		
		
		al.add_widget(bl)
		return al
	def btn_press_desh(self,instance):
		if (self.texit.text == '2584'):
			source  = self.texi.text
			p=open(source, 'r')
			s=p.read()
			data = s
			alphavit = [("F", "А"), ("R", "К"), ("K", "Л"), ("C", "С"), ("X", "Ч"), ("f", "а"),
			             ("<", "Б"), ("Q", "Й"), ("V", "М"), ("N", "Т"), ("/", "Э"), ("<", "б"),
			             ("D", "В"), ("B", "И"), ("Y", "Н"), ("E", "У"), (">", "Ю"), ("b", "в"),
			             ("U", "Г"), ("P", "З"), ("J", "О"), ("A", "Ф"), ("Z", "Я"), ("u", "г"),
			             ("L", "Д"), (":", "Ж"), ("G", "П"), ("[", "Х"), ("M", "Ь"), ("l", "д"),
			             ("T", "Е"), ("~", "Ё"), ("H", "Р"), ("W", "Ц"), ("]", "ъ"), (" "," "),
			             ("t", "е"), ("+", "ё"), (";", "ж"), ("p", "з"), ("b", "и"), ("r","к"),
			             ("k", "л"), ("v", "м"), ("y", "н"), ("j", "о"), ("g", "п"), ("h","р"),
			             ("c", "с"), ("n", "т"), ("e", "у"), ("a", "ф"), ("{", "х"), ("w","ц"),
			             ("z", "я"), (".", "ю"), ("*", "э"), ("}", "ъ"), ("m", "ь"), ("x","ч"),]
			 
			lester =data.translate(str.maketrans(dict(alphavit)))
			print(data.translate(str.maketrans(dict(alphavit))))
			p.close
			f = open (source,'w')
			f.close
			d = open (source,'a')
			d.write(lester)
			d.close

			self.lbl.text = ('Файл дешифрован :3')
			self.pb.value = 100
		else:
			self.lbl.text = ('Пароль неверен :3')
	def btn_press(self, instance):
		if (self.texit.text == '2584'):
			source  = self.texi.text
			p=open(source, 'r')
			s=p.read()
			data = s
			alphavit = [("А", "F"), ("К", "R"), ("Л", "K"), ("С", "C"), ("Ч", "X"), ("а", "f"),
			             ("Б", "<"), ("Й", "Q"), ("М", "V"), ("Т", "N"), ("Э", "/"), ("б", "<"),
			             ("В", "D"), ("И", "B"), ("Н", "Y"), ("У", "E"), ("Ю", ">"), ("в", "b"),
			             ("Г", "U"), ("З", "P"), ("О", "J"), ("Ф", "A"), ("Я", "Z"), ("г", "u"),
			             ("Д", "L"), ("Ж", ":"), ("П", "G"), ("Х", "["), ("Ь", "M"), ("д", "l"),
			             ("Е", "T"), ("Ё", "~"), ("Р", "H"), ("Ц", "W"), ("Ъ", "]"), (" "," "),
			             ("е", "t"), ("ё", "+"), ("ж", ";"), ("з", "p"), ("и", "b"), ("к","r"),
			             ("л", "k"), ("м", "v"), ("н", "y"), ("о", "j"), ("п", "g"), ("р","h"),
			             ("с", "c"), ("т", "n"), ("у", "e"), ("ф", "a"), ("х", "{"), ("ц","w"),
			             ("я", "z"), ("ю", "."), ("э", "*"), ("ъ", "}"), ("ь", "m"), ("ч","x"),]
			 
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
		else:
			self.lbl.text = ('Пароль неверен :3')
	
	
	

			


		


if __name__ == "__main__":##
	 BoxApp().run()##



