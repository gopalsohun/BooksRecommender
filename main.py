from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty


class AddBookForm(BoxLayout):
    search_input = ObjectProperty()

    def search_book(self):
        print("The user searched for '{}'".format(self.search_input.text))


class BooksRecommendationApp(App):
    pass


if __name__ == '__main__':
    BooksRecommendationApp().run()