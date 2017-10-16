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

RED = (1, 0, 0, 1)
GREEN = (0, 1, 0, 1)
SORT_OPTIONS = ["Title", "Artist", "Year", "Required"]
FILE_NAME = 'songs.csv'


class SongsToLearnApp(App):
    """
    SongsToLearnApp
    Takes songs from songs.csv, stores them as objects and builds the GUI, the GUI's functions are:
    - Show # of completed songs & # of required songs
    - Shows songs in a sorted list with learned songs highlighted in green & un-learned songs highlighted in red
    - Show status messages to user
    - Allows user to change songs from learned to un-learned and vice versa
    - Allows user to add new songs to the list
    Upon exiting the App the updated song list is written to the specified file
    """
    current_sort_option = StringProperty()
    sort_options = ListProperty()

    def __init__(self, **kwargs):
        """
        Constructs App, sets self.songs to SongList class, sets self.song to Song class and loads the specified song
        file with self.songs.load_songs
        """
        self.songs = SongList()
        self.song = Song()
        self.songs.load_songs(FILE_NAME)
        super(SongsToLearnApp, self).__init__(**kwargs)

    def build(self):
        """
        Build Kivy GUI from file 'app.kv' with a default sorting option
        :return: root Kivy widget
        """
        self.title = "Songs To Learn 2.0"
        self.root = Builder.load_file('app.kv')
        self.sort_options = SORT_OPTIONS
        # Set default sorting option to 'Title' (first option in sorting list)
        self.current_sort_option = self.sort_options[0]
        self.create_widgets()
        return self.root

    def sort_songs(self, current_sort_option):
        """
        Sorts songs by current_sort_option, clears all widgets in the song box and then rebuilds them
        :param current_sort_option: method to sort songs by (options are "Title", "Artist", "Year" and "Required")
        :return: None
        """
        self.songs.sort_songs(current_sort_option)
        SongsToLearnApp.create_widgets(self)

    def clear_inputs(self):
        """
        Clears all text input fields
        :return: None
        """
        self.root.ids.input_title.text, self.root.ids.input_artist.text, self.root.ids.input_year.text = ("", "", "")

    def create_widgets(self):
        """
        Clears all widgets in the song box and then builds a widget in the song box for every song in the song list,
        learned songs are coloured green and required songs are coloured red. A label is assigned to show # of learned
        songs and # of required songs.
        :return:
        """
        self.root.ids.songsBox.clear_widgets()
        for song in self.songs.songs:
            temp_song_button = Button(text=str(song))
            # Ternary operator to determine button colour
            temp_song_button.background_color = RED if song.required else GREEN
            self.root.ids.songsBox.add_widget(temp_song_button)
            # On release of a temp_song_button, call change_learned_status method
            temp_song_button.bind(on_release=self.change_learned_status)
            self.root.ids.output_song_learned_status_label.text = "To learn: {}. Learned: {}".format(
                self.songs.get_number_of_required_songs(), self.songs.get_number_of_learned_songs())

    def change_learned_status(self, instance):
        """
        Changes a songs learned status from learned to required or vice versa depending on the songs current state, a
        label shows the changed status of the song and then the songs are sorted by the current sort option
        :param instance: Kivy button instance text
        :return: None
        """
        self.song = self.songs.get_song_by_title(instance.text)
        # Marks song as learned and shows according status text
        if self.song.required:
            self.song.mark_learned()
            status_text = "You have learned {}".format(self.song.title)
        # Marks song as required and shows according status text
        else:
            self.song.mark_required()
            status_text = "You need to learn {}".format(self.song.title)
        # Shows status text, sorts songs by current s
        self.root.ids.status_text.text = status_text
        self.sort_songs(self.root.ids.sort_options.text)

    def add_song(self):
        """
        Error checks text input fields on the release of Add Song button, if all error checks are passed song is added
        to the song list, all inputs are cleared and songs are sorted by the current sort option
        :return: Prevents function from going further if an error occurs
        """
        # Error check for blank inputs
        if "" in (self.root.ids.input_title.text, self.root.ids.input_artist.text, self.root.ids.input_year.text):
            self.root.ids.status_text.text = "All fields must be completed"
            return
        # Error check for negative numbers
        try:
            if int(self.root.ids.input_year.text) < 0:
                self.root.ids.status_text.text = "Year must be >= 0"
                return
        # Error check for invalid numbers
        except ValueError:
            self.root.ids.status_text.text = "Please enter a valid number"
            return
        # Song add, clear inputs, sort songlist
        song_to_add = Song(self.root.ids.input_title.text, self.root.ids.input_artist.text,
                           int(self.root.ids.input_year.text))
        self.songs.add_song(song_to_add)
        SongsToLearnApp.clear_inputs(self)
        self.sort_songs(self.root.ids.sort_options.text)

    def on_stop(self):
        """
        Saves songs to specified file when app is closed
        :return: None
        """
        self.songs.save_songs(FILE_NAME)


SongsToLearnApp().run()
