# BEGIN IMPORTS
import json
import requests
from kivy.app import App
from kivy.factory import Factory
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton


# END IMPORTS

# BEGIN AddBookForm
class AddBookForm(BoxLayout):
    googleapikey = "AIzaSyDgEcXMWxJo7BMfkjHRArzvZY9-5Vw3iTk"  # Google Books API key
    search_input = ObjectProperty()  # specifies default value of the property

    # def search_book(self):
    #     print("The user searched for '{}'".format(self.search_input.text))
    #BEGIN search_book
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

        # print(data["totalItems"])
        # for d in data["items"]:
        #     try:
        #         # print(repr(i["volumeInfo"]["description"]))
        #         print("".join(d["volumeInfo"]["title"]))
        #         self.search_results.item_strings =
        #     except:
        #         pass
        # try:
        #     # print(repr((i["volumeInfo"]["imageLinks"]["thumbnail"])))
        #     self.search_results.item_strings = i["volumeInfo"]["authors"]
        # except:
        #     pass

        books = ["{} by {}".format(d["volumeInfo"]["title"], d["volumeInfo"]["authors"][0])
                 for d in data["items"]]
        print("\n".join(books))
        self.search_results.item_strings = books

        # search_url = search_template.format(self.search_input.text)
        # request = UrlRequest(search_url, self.found_book)

    # END search_book

    # BEGIN found_book
    def found_book(self, request, data):
        data = json.loads(data.decode()) if not isinstance(data, dict) else data  # turn into a dictionary

        books = ["{}{}".format(d['title'], d['authors'])
                 for d in data['items']]

        print("\n".join(books))

        self.search_results.item_strings = books
        self.search_results.adapter.data.clear()
        self.search_results.adapter.data.extend(books)
        self.search_results._trigger_reset_populate()
    # END found_book


# END AddBookForm

# BEGIN BooksRecommendationRoot
class BooksRecommendationRoot(BoxLayout):
    current_book = ObjectProperty()  # specifies default value of the property

    # BEGIN show_book
    def show_book(self, title=None):
        self.clear_widgets()
        if title is None and self.current_book is None:
            title = "Harry Potter"
        if title is not None:
            self.current_book = Factory.CurrentBook()
            self.current_book.title = title
        self.add_widget(self.current_book)

    # END show_book

    # BEGIN show_book_form
    def show_book_form(self):
        self.clear_widgets()
        self.add_widget(AddBookForm())
        # END show_book_form


# END BooksRecommendationRoot

# BEGIN BookButton
class BookButton(ListItemButton):
    pass


# END BookButton

# BEGIN BooksRecommendationApp
class BooksRecommendationApp(App):
    pass


# END BooksRecommendationApp


# BEGIN MAIN
if __name__ == '__main__':
    BooksRecommendationApp().run()
# END MAIN
