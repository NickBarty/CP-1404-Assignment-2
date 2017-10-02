"""
Name: Nicholas Barty
Date: 29/09/2017

Brief Project Description:
This program uses Kivy to display a list of songs that are sorted in a way that can be changed by the user. The user can
also mark a song a learned or unlearned via the display as well as add songs to the list.

GitHub URL: https://github.com/CP1404-2017-2/a2-nbart1
"""

from kivy.app import App
from kivy.lang import Builder

# Create your main program in this file, using the SongsToLearnApp class


class SongsToLearnApp(App):
    def build(self):
        self.title = "Songs To Learn 2.0"
        self.root = Builder.load_file('app.kv')
        return self.root

SongsToLearnApp().run()
