from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class CoinTossBoxLayout(BoxLayout):
	
	def choice(self, guess):
		output = "You clicked the " + guess + " button!"
		self.ids.result.text=output
		
class CoinTossApp(App):
	def build(self):
		return CoinTossBoxLayout()
		
if __name__ == '__main__':
	CoinTossApp().run()		
