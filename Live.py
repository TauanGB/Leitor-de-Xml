"""
This is an example of kaki app usin kivymd modules.
"""
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivy import Config
Config.set('graphics', 'multisamples', '0')

from kivymd.app import MDApp
from kaki.app import App 
from kivy.factory import Factory




# main app class for kaki app with kivymd modules
class LiveApp(MDApp, App):
    """ Hi Windows users """

    DEBUG = 1 # set this to 0 make live app not working

    # *.kv files to watch
    KV_FILES = {
        os.path.join(os.getcwd(), "Menu.kv"),
    }

    # class to watch from *.py files
    CLASSES = {
        "Box_categorias": "Front_end",
        "Box_SubCategorias": "Front_end",
        "Tela_Inicial": "Front_end",
        "Menu": "Front_end"
    }

    # auto reload path
    AUTORELOADER_PATHS = [
        (".", {"recursive": True}),
    ]


    def build_app(self):

        return Factory.Menu()




# finally, run the app
if __name__ == "__main__":
    LiveApp().run()