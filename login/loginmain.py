from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

class AddLoginForm(BoxLayout):

    UserText = ObjectProperty()
    Password = ObjectProperty()

    def do_login(self):
        print(self.UserText.text)
        print(self.Password.text)

class LoginApp(App):

    def build(self):
        return AddLoginForm()

if __name__ == '__main__':
    LoginApp().run()
