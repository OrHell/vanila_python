import os
import requests, bs4
import zipfile##Импорт архивации
from kivy.app import App##Импорт киви
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config##Импорт изменения окошка
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout

Config.set('graphics','resizeble','0');##Изминения чтобы окошко не двигалось
Config.set('graphics','width','240');##Изминения ширина
Config.set('graphics','height','360');##Изминение высоты


class BoxApp(App):

	

	def build(self):
		al = AnchorLayout()
		bl = BoxLayout(orientation= 'vertical')
		self.lbl = Label(text = "",size_hint =[None,None],size = [250,80],font_size = 13)
		bl.add_widget(self.lbl)
		bl.add_widget(Button(text = "Понедельник",halign = "center" ,on_press = self.btn_press_ponedel))
		bl.add_widget(Button(text = "Вторник",halign = "center" ,on_press = self.btn_press_vtornick))
		bl.add_widget(Button(text = "Среда",halign = "center" , on_press = self.btn_press_sreda))
		bl.add_widget(Button(text = "Четверг",halign = "center" ,on_press = self.btn_press_chetverg))
		bl.add_widget(Button(text = "Пятница",halign = "center" ,on_press = self.btn_press_pytnica))
		bl.add_widget(Button(text = "Суббота",halign = "center" ,on_press = self.btn_press_subbota))
		al.add_widget(bl)
		return al
		
	def btn_press_ponedel(self,instance):
		s=requests.get('https://orhell.github.io')
		b=bs4.BeautifulSoup(s.text, "html.parser")
		p3=b.select('.pon')
		poned=p3[0].getText()
		self.lbl.text = poned
		
	def btn_press_vtornick(self,instance):
		s=requests.get('https://orhell.github.io')
		b=bs4.BeautifulSoup(s.text, "html.parser")
		p3=b.select('.vtor')
		vtor=p3[0].getText()
		self.lbl.text = vtor
	def btn_press_sreda(self,instance):
		s=requests.get('https://orhell.github.io')
		b=bs4.BeautifulSoup(s.text, "html.parser")
		p3=b.select('.sred')
		sred=p3[0].getText()
		self.lbl.text = sred
	def btn_press_chetverg(self,instance):
		s=requests.get('https://orhell.github.io')
		b=bs4.BeautifulSoup(s.text, "html.parser")
		p3=b.select('.chet')
		chet=p3[0].getText()
		self.lbl.text = chet
	def btn_press_pytnica(self,instance):
		s=requests.get('https://orhell.github.io')
		b=bs4.BeautifulSoup(s.text, "html.parser")
		p3=b.select('.pyat')
		pyat=p3[0].getText()
		self.lbl.text = pyat
	def btn_press_subbota(self,instance):
		s=requests.get('https://orhell.github.io')
		b=bs4.BeautifulSoup(s.text, "html.parser")
		p3=b.select('.subb')
		subb=p3[0].getText()
		self.lbl.text = subb



			

		
		
 		


if __name__ == "__main__":##
	 BoxApp().run()##

