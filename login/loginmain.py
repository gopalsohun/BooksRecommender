from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

class AddLoginForm(BoxLayout):
    def do_login(self):
        self.login.text= " Text data " + self.User.text

class LoginApp(App):
    def build(self):
        return AddLoginForm()

if __name__ == '__main__':
    LoginApp().run()
