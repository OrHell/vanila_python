
import requests, bs4
import os
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
Config.set('graphics','width','90');##Изминения ширина
Config.set('graphics','height','150');##Изминение высоты


class BoxApp(App):
	def build(self):
		al = AnchorLayout()
		bl = BoxLayout(orientation= 'vertical')
		self.lbl = Label(text = "")
		bl.add_widget(self.lbl)
		self.lbl_2 = Label(text = "")
		bl.add_widget(self.lbl_2)
		bl.add_widget(Button(text = "Wether", on_press = self.btn_press))
		al.add_widget(bl)
		return al
	def btn_press(self,instance):
		
		s=requests.get('https://vk.com/im?peers=148545742_199606518_298941019')
		b=bs4.BeautifulSoup(s.text, "html.parser")
		p3=b.select('.left_fixer .left_count_wrap fl_r left_void  .inl_bl left_count_sign')
		pogoda1=p3[0].getText()
		p4=b.select('.left_fixer .left_count_wrap fl_r left_void  .inl_bl left_count_sign')
		pogoda2=p4[0].getText()
		p5=b.select('.left_fixer .left_count_wrap fl_r left_void  .inl_bl left_count_sign')
		pogoda3=p5[0].getText()
		p6=b.select('.left_fixer .left_count_wrap fl_r left_void  .inl_bl left_count_sign')
		pogoda4=p6[0].getText()
		print('Утром :' + pogoda1 + ' ' + pogoda2)
		print('Днём :' + pogoda3 + ' ' + pogoda4)
		p=b.select('.rSide .description')
		self.lbl.text = ('Утром :' + pogoda1 + ' ' + pogoda2)
		self.lbl_2.text =('Днём :' + pogoda3 + ' ' + pogoda4)
		pogoda=p[0].getText()
		print(pogoda.strip())

if __name__ == "__main__":##
	 BoxApp().run()##