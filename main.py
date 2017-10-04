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
from kivy.uix.button import Button
from songlist import SongList

# Create your main program in this file, using the SongsToLearnApp class

RED = (1, 0, 0, 1)
GREEN = (0, 1, 0, 1)


class SongsToLearnApp(App):
    def __init__(self, **kwargs):
        self.songs = SongList()
        self.songs.load_songs('songs.csv')
        super(SongsToLearnApp, self).__init__(**kwargs)

    def build(self):
        self.title = "Songs To Learn 2.0"
        self.root = Builder.load_file('app.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for song in self.songs.songs:
            temp_button = Button(text=str(song))
            if song.is_required is True:
                temp_button.background_color = RED
            else:
                temp_button.background_color = GREEN
            self.root.ids.songsBox.add_widget(temp_button)


SongsToLearnApp().run()
