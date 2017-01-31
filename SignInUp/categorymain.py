from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.actionbar import ActionBar
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_string('''
<profile>:
    ActionBar:
        pos_hint: {'top':1}
        ActionView:
            ActionPrevious:
                with_previous: True
                title: 'User'

            ActionButton:
                text: 'Btn0'
                icon: 'description.png'

    BoxLayout:
        orientation: "vertical"
        padding: "10dp"
        spacing: "30dp"
        BoxLayout:
            size_hint_y: 90
        BoxLayout:
            size_hint_y: 300
            padding: "10dp"
            canvas:
                Color:
                    rgb: [0.129, 0.125, 0.125]
                Rectangle:
                    pos: self.pos
                    size:self.size
            AsyncImage
                source: 'user1.png'
            Label:
                text: "ratings"

            Label:
                text: "Books Viewed"
        BoxLayout:
            size_hint_y: 75
            spacing: "30dp"
            # canvas:
            #     Color:
            #         rgb: [0.129, 0.125, 0.125]
            #     Rectangle:
            #         pos: self.pos
            #         size:self.size
            # AsyncImage
            #     source: 'star.png'
            #     size_hint_x: 2
            # Label:
            #     text: "Preferences"
            #     size_hint_x: 3
            # Button:
            #     size_hint_x: 5
            #     Image:
            #         source: 'plus1.png'
            #     # text: "+"

            ActionBar:
                pos_hint: {'top':1}
                ActionView:
                    ActionPrevious:
                        with_previous: False
                        app_icon: 'star.png'
                        title: 'Preferences'

                    ActionButton:
                        text: 'Btn0'
                        icon: 'plus1.png'
        BoxLayout:
            size_hint_y: 400




        ''')

class profile(Screen):
    pass

class TestApp(App):
    def build(self):
        return profile()

if __name__ == '__main__':
    TestApp().run()


