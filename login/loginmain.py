from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class AddLoginForm(BoxLayout):
    def do_login(self):
        self.login.text= " Text data " + self.UserTextField.text

class LoginApp(App):
    def build(self):
        return AddLoginForm()

if __name__ == '__main__':
    LoginApp().run()
