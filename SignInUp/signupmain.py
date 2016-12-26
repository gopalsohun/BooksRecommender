from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import ObjectProperty  # at top of file

class SignUpForm(AnchorLayout):
    username_box = ObjectProperty()
    password_box = ObjectProperty()
    confirm_box = ObjectProperty()

    def login(self):
        print(self.username_box.text)
        print(self.password_box.text)
        print(self.confirm_box.text)

class SignUp(App):
    def build(self):
        return SignUpForm()

if __name__ == '__main__':
    SignUp().run()
