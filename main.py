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
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from songlist import SongList
from song import Song

# Create your main program in this file, using the SongsToLearnApp class

RED = (1, 0, 0, 1)
GREEN = (0, 1, 0, 1)
SORT_OPTIONS = ["Title", "Artist", "Year", "Required"]
FILE_NAME = 'songs.csv'


class SongsToLearnApp(App):
    current_sort_option = StringProperty()
    sort_options = ListProperty()

    def __init__(self, **kwargs):
        self.songs = SongList()
        self.song = Song()
        self.songs.load_songs(FILE_NAME)
        super(SongsToLearnApp, self).__init__(**kwargs)

    def build(self):
        self.title = "Songs To Learn 2.0"
        self.root = Builder.load_file('app.kv')
        self.sort_options = SORT_OPTIONS
        self.current_sort_option = self.sort_options[0]
        self.create_widgets()
        return self.root

    def sort_songs(self, current_sort_option):
        # self.current_sort_option = current_sort_option
        self.songs.sort(current_sort_option)
        self.root.ids.songsBox.clear_widgets()
        SongsToLearnApp.create_widgets(self)

    def clear_inputs(self):
        self.root.ids.input_title.text = ""
        self.root.ids.input_artist.text = ""
        self.root.ids.input_year.text = ""

    def create_widgets(self):
        self.root.ids.songsBox.clear_widgets()
        for song in self.songs.songs:
            temp_button = Button(text=str(song))
            if song.required is True:
                temp_button.background_color = RED
            else:
                temp_button.background_color = GREEN
            self.root.ids.songsBox.add_widget(temp_button)
            temp_button.bind(on_release=self.change_learned_status)
            self.root.ids.output_song_learned_status_label.text = "To learn: {}. Learned: {}".format(
                self.songs.get_number_of_required_songs(), self.songs.get_number_of_learned_songs())

    def change_learned_status(self, instance):
        self.song = self.songs.get_song_by_title(instance.text)
        if self.song.required is True:
            self.song.mark_learned()
            status_text = "You have learned {}".format(str(self.song.title))
        else:
            self.song.mark_required()
            status_text = "You need to learn {}".format(str(self.song.title))
        self.root.ids.status_text.text = str(status_text)
        self.sort_songs(self.root.ids.sort_options.text)

    def add_song(self):
        if self.root.ids.input_title.text == "" or self.root.ids.input_artist.text == "" \
                or self.root.ids.input_year.text == "":
            self.root.ids.status_text.text = "All fields must be completed"
            return
        try:
            if int(self.root.ids.input_year.text) < 0:
                self.root.ids.status_text.text = "Year must be >= 0"
                return
        except ValueError:
            self.root.ids.status_text.text = "Please enter a valid number"
            return
        song_to_add = Song(self.root.ids.input_title.text, self.root.ids.input_artist.text,
                           int(self.root.ids.input_year.text))
        self.songs.add_song(song_to_add)
        SongsToLearnApp.clear_inputs(self)
        self.sort_songs(self.root.ids.sort_options.text)

    def on_stop(self):
        self.songs.save_songs(FILE_NAME)


SongsToLearnApp().run()
