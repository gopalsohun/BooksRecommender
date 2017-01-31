import json
import requests
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, ListProperty, StringProperty
from kivy.uix.listview import ListItemButton


# BEGIN AddBookForm
from kivy.utils import get_color_from_hex


class AddBookForm(BoxLayout):
    googleapikey = "AIzaSyDgEcXMWxJo7BMfkjHRArzvZY9-5Vw3iTk"  # Google Books API key
    search_input = ObjectProperty()  # specifies default value of the property

    # BEGIN search_book
    def search_book(self):
        self.search_results.item_strings = ""
        if self.search_input.text == "":
            popup = Popup(title="Information",
                          content=Label(text="No book name specified"),
                          size_hint=(None, None), size=(400, 200))
            popup.open()
            return

        parms = {"q": self.search_input.text, 'key': self.googleapikey}
        search_template = "https://www.googleapis.com/books/v1/volumes"
        search_url = requests.get(url=search_template, params=parms)
        print(search_url.url)
        data = search_url.json()

        books = [(d["volumeInfo"]["title"], d["volumeInfo"]["authors"][0])
                 for d in data["items"]]
        # print("\n".join(books))

        # test = [(d["volumeInfo"]["imageLinks"]["smallThumbnail"]) #d["volumeInfo"]["publishedDate"]
        #         for d in data["items"]]
        # print(test)

        self.search_results.item_strings = books

        # search_url = search_template.format(self.search_input.text)
        # request = UrlRequest(search_url, self.found_book)

    # END search_book

    def found_book(self, request, data):
        data = json.loads(data.decode()) if not isinstance(data, dict) else data  # turn into a dictionary

        books = [(d['title'], d['authors'])
                 for d in data['items']]

        print("\n".join(books))

        self.search_results.item_strings = books
        self.search_results.adapter.data.clear()
        self.search_results.adapter.data.extend(books)
        self.search_results._trigger_reset_populate()

    def args_converter(self, index, data_item):
        title, authors = data_item
        return {'book': (title, authors)}


# END AddBookForm

class CurrentBook(BoxLayout):
    googleapikey = "AIzaSyDgEcXMWxJo7BMfkjHRArzvZY9-5Vw3iTk"  # Google Books API key
    book = ListProperty(["Harry Potter", "J.K Rowling"])
    thumbnail = StringProperty()
    publisher = StringProperty()
    date = StringProperty()
    description = StringProperty()

    def update_book(self):
        query = self.book[0]
        print("{} saem sa".format(query))
        parms = {"q": query, 'key': self.googleapikey}
        print(parms)
        search_template = "https://www.googleapis.com/books/v1/volumes"
        search_url = requests.get(url=search_template, params=parms)
        print(search_url.url)
        data = search_url.json()
        # self.thumbnail = data["volumeInfo"]["imageLinks"]["smallThumbnail"]
        # self.publisher = data["volumeInfo"]["publisher"]
        # self.date = data["volumeInfo"]["publishedDate"]
        # self.description = data["volumeInfo"]["description"]

    def book_retrieved(self, request, data):
        data = json.loads(data.decode()) if not isinstance(data, dict) else data
        self.thumbnail = data["volumeInfo"]["imageLinks"]["smallThumbnail"]
        self.publisher = data["volumeInfo"]["publisher"]
        self.date = data["volumeInfo"]["publishedDate"]
        self.description = data["volumeInfo"]["description"]


# BEGIN BooksRecommendationRoot
class BooksRecommendationRoot(BoxLayout):
    current_book = ObjectProperty()  # specifies default value of the property

    def show_book(self, book=None):
        self.clear_widgets()
        if book is None and self.current_book is None:
            book = ("Nothing found", "None")
            self.current_book = CurrentBook()
        if book is not None:
            # self.current_book = Factory.CurrentBook()
            self.current_book = CurrentBook(book=book)
            # self.current_book.title = book
        self.current_book.update_book()
        self.add_widget(self.current_book)

    def show_book_form(self):
        self.clear_widgets()
        self.add_widget(AddBookForm())


# END BooksRecommendationRoot

# BEGIN BookButton
class BookButton(ListItemButton):
    book = ListProperty()


# END BookButton

# BEGIN BooksRecommendationApp
class BooksRecommendationApp(App):
    pass


# END BooksRecommendationApp


# BEGIN MAIN
if __name__ == '__main__':
    Window.clearcolor = get_color_from_hex('#101216')
    BooksRecommendationApp().run()
    # END MAIN
