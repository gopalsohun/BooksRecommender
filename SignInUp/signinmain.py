from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.properties import ObjectProperty  # at top of file
import sqlite3

class SignInForm(AnchorLayout):
    username_box = ObjectProperty()
    password_box = ObjectProperty()

    def login(self):
        conn = sqlite3.connect('booksrecommender.db')
        password = self.password_box.text
        username = self.username_box.text
        cursor = conn.cursor()
        for row in username:
            cursor.execute("SELECT UserID FROM Authentication WHERE UserName = ?", (username,))
            data = cursor.fetchall()
        if len(data) == 0:
            print("No username available you need to sign up!")
            popup = Popup(title="Information", content=Label(text="No username available you need to sign up!"),
                          size_hint=(None, None),
                          size=(400, 200))
            popup.open()
            return

        else:
            for row in password:
                cursor.execute("SELECT UserID FROM Authentication WHERE Password = ?", (password,))
                data = cursor.fetchall()
            if len(data) == 0:
                print("Wrong password. Try again!")
                popup = Popup(title="Information", content=Label(text="Wrong password. Try again!"), size_hint=(None, None),
                              size=(400, 200))
                popup.open()
                return
            else:
                print("Welcome")
                popup = Popup(title="Information", content=Label(text="Welcome"),
                              size_hint=(None, None),
                              size=(400, 200))
                popup.open()
                return

class SignIn(App):
    def build(self):
        return SignInForm()

if __name__ == '__main__':
    SignIn().run()



