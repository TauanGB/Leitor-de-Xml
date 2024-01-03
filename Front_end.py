import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivy import Config
Config.set('graphics', 'multisamples', '0')

from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from tkinter.filedialog import askdirectory
from kivy.clock import Clock
from Back_end import Busca

class Box_categorias(MDBoxLayout):
	def __init__(self,Titulo = '', *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.ids.Titulo_Categoria.text = Titulo

class Box_SubCategorias(MDBoxLayout):
	def __init__(self,Titulo = '' ,Texto='' , *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.ids.Sub_Titulo.text = Titulo
		self.ids.Sub_Texto.text = Texto

class Box_Telas(MDScreen):
	def __init__(self,Nome, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.name = Nome

class Tela_Inicial(MDScreen):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

class Menu(MDApp):
	def build(self):
		super().build()
		self.root = Tela_Inicial()
		self.Arq_atual = 0
	
	def on_start(self):
		super().on_start()
		'''Teste_Catego = Box_categorias("Titulo Teste")
		Teste_SubCatego = Box_SubCategorias("SubCategoria Teste","Texto Generico Teste")
		Teste_SubCatego_2 = Box_SubCategorias("Chav Cte","90202139401239412543223423556")


		Teste_Catego.ids.Box_Bau.add_widget(Teste_SubCatego)
		Teste_Catego.ids.Box_Bau.add_widget(Teste_SubCatego_2)
		self.root.ids.Categorias.add_widget(Teste_Catego)'''

		Diretorio = str(askdirectory())
		XML_diretorio = [i for i in os.listdir(Diretorio) if os.path.isfile(os.path.join(Diretorio, i)) if ".xml" in i]

		self.XML_Buscas = Busca(XML_diretorio,Diretorio)

		for Xml in list(self.XML_Buscas.keys()):
			Tela_Xml = Box_Telas(Xml)
			self.root.ids.Gerenc_telas.add_widget(Tela_Xml)
			for Categoria in self.XML_Buscas[Xml].keys():
				Catego_tmp = Box_categorias(Categoria)
				for SubCategoria in self.XML_Buscas[Xml][Categoria].keys():
					SubCatego_tmp = Box_SubCategorias(SubCategoria,self.XML_Buscas[Xml][Categoria][SubCategoria])
					Catego_tmp.add_widget(SubCatego_tmp)
				Tela_Xml.ids.Categorias.add_widget(Catego_tmp)

		self.root.ids.Gerenc_telas.current = list(self.XML_Buscas.keys())[0]
	
	def Prox_arq(self):
		if self.Arq_atual < len(list(self.XML_Buscas.keys())) - 1:
			self.root.ids.Gerenc_telas.current = list(self.XML_Buscas.keys())[self.Arq_atual + 1]
			self.Arq_atual += 1

		else:
			self.root.ids.Gerenc_telas.current = list(self.XML_Buscas.keys())[0]
			self.Arq_atual = 0
		
		self.root.ids.indice_label.text = str(self.Arq_atual + 1)
	
	def Anter_arq(self):
		if self.Arq_atual > 0:
			self.root.ids.Gerenc_telas.current = list(self.XML_Buscas.keys())[self.Arq_atual - 1]
			self.Arq_atual -= 1

		else:
			self.root.ids.Gerenc_telas.current = list(self.XML_Buscas.keys())[len(list(self.XML_Buscas.keys())) - 1]
			self.Arq_atual = len(list(self.XML_Buscas.keys())) - 1
		
		self.root.ids.indice_label.text = str(self.Arq_atual + 1)


	
if __name__ == "__main__":
	global app
	app = Menu().run()