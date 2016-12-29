from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import ObjectProperty  # at top of file
import sqlite3


class SignUpForm(AnchorLayout):
    username_box = ObjectProperty()
    password_box = ObjectProperty()
    confirm_box = ObjectProperty()

    def login(self):
        conn = sqlite3.connect('booksrecommender.db')
        password = self.password_box.text
        username = self.username_box.text
        confirm = self.confirm_box.text
        cursor = conn.cursor()
        if password == confirm:
            print("Welcome")
            cursor.execute("INSERT INTO Authentication VALUES (NULL, ?, ? )", (username, password));
            conn.commit()
            print("Table created successfully")

        else:
            print("Error in password")
            conn.close()



class SignUp(App):
    def build(self):
        return SignUpForm()

if __name__ == '__main__':
    SignUp().run()
