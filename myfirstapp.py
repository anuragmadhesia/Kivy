from kivy.app import App
from kivy.uix.label import Label
class FirstKivy(App):
    def build(self):
        lbl=Label(text="Hello Kivy")
        return lbl
if __name__=='__main__':
    FirstKivy().run()