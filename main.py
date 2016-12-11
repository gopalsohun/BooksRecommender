from googleapiclient.discovery import build
from kivy.app import App
from kivy.network.urlrequest import UrlRequest
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
import json


class AddBookForm(BoxLayout):
    search_input = ObjectProperty()

    def search_book(self):
        print("The user searched for '{}'".format(self.search_input.text))

    def search_book(self):
        books_service = build('books', 'v1', developerKey='AIzaSyDgEcXMWxJo7BMfkjHRArzvZY9-5Vw3iTk')
        search_template = "https://www.googleapis.com/books/v1/volumes?q="
        search_url = search_template.format(self.search_input.text)
        request = UrlRequest(search_url, self.found_book)

    def found_book(self, request, data):
        data = json.loads(data.decode()) if not isinstance(data, dict) else data
        books = ["{}({})".format(d['title'], d['authors']['categories'])
            for d in data['list']]
        print("\n".join(books))
        self.search_results.item_strings = books

class BooksRecommendationApp(App):
    pass


if __name__ == '__main__':
    BooksRecommendationApp().run()