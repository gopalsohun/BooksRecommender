from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
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
        else:
            for row in password:
                cursor.execute("SELECT UserID FROM Authentication WHERE Password = ?", (password,))
                data = cursor.fetchall()
            if len(data) == 0:
                print("Wrong password. Try again!")
            else:
                print("Welcome")


class SignIn(App):
    def build(self):
        return SignInForm()

if __name__ == '__main__':
    SignIn().run()



