# create your SongList class in this file
import csv
from song import Song


class SongList:
    def __init__(self):
        self.songs = []

    def __str__(self):
        song_to_print = ""
        for song in self.songs:
            song_to_print += str(song)
            song_to_print += "\n"
        return song_to_print

    def get_song_by_title(self, title):
        for song in self.songs:
            if song.title == title:
                return song

    def add_song(self, song):
        self.songs += [song]

    def get_number_of_required_songs(self):
        return len([song for song in self.songs if song.is_required])

    def get_number_of_learned_songs(self):
        return len([song for song in self.songs if not song.is_required])

    def load_songs(self, file_name):
        with open(file_name, "r") as open_file:
            read_file = csv.reader(open_file, delimiter=',')
            for row in read_file:
                song_to_load = Song(row[0], row[1], int(row[2]), True if row[3] == "y" else False)
                self.add_song(song_to_load)

    def save_songs(self):
        pass

    def sort(self):
        pass
