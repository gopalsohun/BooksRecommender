import requests
from googleapiclient.discovery import build
from kivy.app import App
from kivy.network.urlrequest import UrlRequest
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
import json


class AddBookForm(BoxLayout):
    googleapikey = "AIzaSyDgEcXMWxJo7BMfkjHRArzvZY9-5Vw3iTk"
    search_input = ObjectProperty()

    # def search_book(self):
    #     print("The user searched for '{}'".format(self.search_input.text))

    def search_book(self):
        if self.search_input.text == "":
            print("null")
            return


        parms = {"q":self.search_input.text, 'key':self.googleapikey}
        print("here")
        search_template = "https://www.googleapis.com/books/v1/volumes"

        search_url = requests.get(url=search_template, params=parms)

        print(search_url.url)

        data = search_url.json()
        # print(data["totalItems"])

        #
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

    def found_book(self, request, data):
        data = json.loads(data.decode()) if not isinstance(data, dict) else data #turn into a dictionary
        books = ["{}{}".format(d['title'], d['authors'])
                 for d in data['items']]
        print("\n".join(books))
        self.search_results.item_strings = books


class BooksRecommendationApp(App):
    pass


if __name__ == '__main__':
    BooksRecommendationApp().run()
