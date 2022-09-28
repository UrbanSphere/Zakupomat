from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder


Builder.load_file('StartMenu.kv')


class StartMenu(Screen):
    @staticmethod
    def on_pressed(self):
        print('Hello')


class Zakupomat(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(StartMenu(name='startmenu'))

        return sm



if __name__ == '__main__':
    Zakupomat.run()


