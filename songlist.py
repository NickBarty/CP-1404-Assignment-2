import csv
from song import Song
from operator import attrgetter


class SongList:
    """SongList class initialises a list for songs to be stored in, specifies how to print the song list and gives the
    ability to find a song by its title, add a song to the list, get the number of required/learned songs in the list,
    load & save the CSV file and sort the song list by specific attributes"""

    def __init__(self):
        """initialises a list for songs to be stored in"""
        self.songs = []

    def __str__(self):
        """specifies how to print the song list"""
        songs_to_print = ""
        for song in self.songs:
            songs_to_print += "{} \n".format(song)
        return songs_to_print

    def get_song_by_title(self, song_to_try):
        """get all attributes of a song by entering in just the title"""
        for song in self.songs:
            if song.title in song_to_try:
                return song

    def add_song(self, song):
        self.songs += [song]

    def get_number_of_required_songs(self):
        """gets number of songs that are required (haven't been learnt) and returns that number"""
        return len([song for song in self.songs if song.required])

    def get_number_of_learned_songs(self):
        """gets number of songs that have been learnt and returns that number"""
        return len([song for song in self.songs if not song.required])

    def load_songs(self, file_name):
        """reads CSV file line by line, adding each line (song) to the song list"""
        with open(file_name, "r") as open_file:
            read_file = csv.reader(open_file, delimiter=',')
            for row in read_file:
                song_to_load = Song(row[0], row[1], int(row[2]), True if row[3] == "y" else False)
                self.songs.append(song_to_load)

    def save_songs(self, file_name):
        """writes CSV file line by line using the attributes from each song in the list"""
        with open(file_name, "w") as open_file:
            write_to_file = csv.writer(open_file, delimiter=",", lineterminator="\n")
            for song in self.songs:
                write_to_file.writerow([song.title, song.artist, song.year, "y" if song.required else "n"])

    def sort(self, attribute):
        """sorts the song list by the specified attribute (title, artist, year, is_required) and then by the title"""
        self.songs.sort(key=attrgetter(attribute.lower(), "title"))
