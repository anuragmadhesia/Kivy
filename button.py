from kivy.app import App
from kivy.uix.button import Button

class ButtonApp(App):
    def build(self):
        btn=Button(text='Press me!',size_hint=(.2,.2),pos=(300,300))
        return btn
if __name__=='__main__':
    ButtonApp().run()