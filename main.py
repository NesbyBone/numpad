from kivy.app import App
from kivy.config import Config
from kivy.uix.gridlayout import GridLayout

Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '800')


class GuiGridLayout(GridLayout):
    pass


class MyGui(App):
    def build(self):
        return GuiGridLayout()

if __name__ == '__main__':
    MyGui().run()