from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import ObjectProperty  # at top of file

class SignInForm(AnchorLayout):
    username_box = ObjectProperty()
    password_box = ObjectProperty()

    def login(self):
        print(self.username_box.text)
        print(self.password_box.text)

class SignIn(App):
    def build(self):
        return SignInForm()

if __name__ == '__main__':
    SignIn().run()



