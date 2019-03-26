import requests, bs4
from kivy.app import App##Импорт киви
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config##Импорт изменения окошка
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout



from kivy.uix.gridlayout import GridLayout
#from kivy.core.window import Window
#Window.clearcolor = (1, 1, 0, 20)

Config.set('graphics','resizeble','0');##Изминения чтобы окошко не двигалось
Config.set('graphics','width','520');##Изминения ширина
Config.set('graphics','height','280');##Изминение высоты


class BoxApp(App):
	def build(self):
		al = AnchorLayout()
		gl = GridLayout(rows = 3, cols=3)#size_hint =[None,None])#size = [480,80])
		bl = BoxLayout(orientation= 'vertical')


		self.lbli = Label(text = "")
		self.lblit = Label(text = " ")
		self.lble = Label(text = "")
		self.btn = Button(text = "Понедельник ", on_press = self.btn_press_os)


		gl.add_widget(self.lbli)
		

		gl.add_widget(self.lblit)
	

		gl.add_widget(self.lble)

		
		
		
		
		




		gl.add_widget(Button(text = " < ", on_press = self.btn_press_left))
		gl.add_widget(self.btn)
		gl.add_widget(Button(text = " > ", on_press = self.btn_press_right))
		bl.add_widget(gl)
		al.add_widget(bl)
		return al
	
	
	def btn_press_os(self,instance):
		
		print('Piska')
	def btn_press_left(self,instance):
		
		print('dfdsf')
	def btn_press_right(self,instance):
		if (self.btn.text.endswith('Понедельник')):
			s=requests.get('https://orhell.github.io')
			b=bs4.BeautifulSoup(s.text, "html.parser")
			p12=b.select('.pon')
			poned=p12[0].getText()
			self.lblit.text = (poned)
		self.btn.text = ('Вторник')

		if (self.btn.text.endswith('Вторник')):
			s2=requests.get('https://orhell.github.io')
			b2=bs4.BeautifulSoup(s.text, "html.parser")
			p2=b2.select('.vtor')
			vtor=p2[0].getText()
			self.lblit.text = (vtor)
			self.btn.text = ('Среда')

		if (self.btn.text.endswith('Среда')):
			s3=requests.get('https://orhell.github.io')
			b3=bs4.BeautifulSoup(s.text, "html.parser")
			p3=b3.select('.sred')
			sred=p3[0].getText()
			self.lblit.text = (sred)
			self.btn.text = ('Четверг')

		if (self.btn.text.endswith('Четверг')):
			s4=requests.get('https://orhell.github.io')
			b4=bs4.BeautifulSoup(s.text, "html.parser")
			p4=b4.select('.chet')
			chet=p4[0].getText()
			self.lblit.text = (chet)
			self.btn.text = ('Пятница')			

		if (self.btn.text.endswith('Пятница')):
			s5=requests.get('https://orhell.github.io')
			b55=bs4.BeautifulSoup(s.text, "html.parser")
			p35=b55.select('.pyat')
			pyat=p35[0].getText()
			self.lblit.text = (pyat)
			self.btn.text = ('Суббота')

		if (self.btn.text.endswith('Суббота')):
			s6=requests.get('https://orhell.github.io')
			b6=bs4.BeautifulSoup(s.text, "html.parser")
			p36=b6.select('.subb')
			subb=p36[0].getText()
			self.lblit.text = (subb)
			self.btn.text = ('Понедельник')


if __name__ == "__main__":##
	 BoxApp().run()##