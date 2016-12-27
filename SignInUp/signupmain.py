from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import ObjectProperty  # at top of file
import sqlite3

conn= sqlite3.connect('booksrecommender.db')

class SignUpForm(AnchorLayout):
    username_box = ObjectProperty()
    password_box = ObjectProperty()
    confirm_box = ObjectProperty()

    def login(self):
        with conn:
            cursor = conn.cursor()

            password = self.password_box.text
            confirm = self.confirm_box.text

            if password == confirm:
                print("Welcome")
                cursor.execute('''INSERT INTO Authentication VALUES (?, ?);''', (self.username_box.text,password))
                conn.commit()
                print("Table created successfully")
                conn.close()

            else:
                print("Error in password")

class SignUp(App):
    def build(self):
        return SignUpForm()

if __name__ == '__main__':
    SignUp().run()
