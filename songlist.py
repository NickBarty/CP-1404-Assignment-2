import csv
from song import Song
from operator import attrgetter


class SongList:
    """
    SongList class initialises a list for songs to be stored in, specifies how to print the song list and gives the
    ability to find a song by its title, add a song to the list, get the number of required/learned songs in the list,
    load & save the CSV file and sort the song list by specific attributes
    """

    def __init__(self):
        """
        initialises a list for songs to be stored in
        :return: None
        """
        self.songs = []

    def __str__(self):
        """
        specifies how to print the song list
        :return: formatted songs list string
        """
        songs_list = ""
        for song in self.songs:
            songs_list += "{} \n".format(song)
        return songs_list

    def get_song_by_title(self, song_to_try):
        """
        get all attributes of a song by entering in just the title
        :param song_to_try: song to find title in
        :return: song
        """
        # Gets song title to compare from parameter
        title = song_to_try.split("\"")[1]
        # Loops through song list to find song with matching title
        for song in self.songs:
            if song.title == title:
                return song

    def add_song(self, song):
        """
        add a song to the song list
        :param song: song to add to song list
        :return: None
        """
        self.songs += [song]

    def get_number_of_required_songs(self):
        """
        gets number of songs that are required (haven't been learnt) and returns that number
        :return: number of required (not learnt) songs
        """
        return len([song for song in self.songs if song.required])

    def get_number_of_learned_songs(self):
        """
        gets number of songs that have been learnt and returns that number
        :return: number of learned songs
        """
        return len([song for song in self.songs if not song.required])

    def load_songs(self, file_name):
        """
        reads a CSV file line by line, adding each line (song) to the song list
        :param file_name: name of file to load
        :return: None
        """
        with open(file_name, "r") as open_file:
            read_file = csv.reader(open_file, delimiter=',')
            for row in read_file:
                song_to_load = Song(row[0], row[1], int(row[2]), True if row[3] == "y" else False)
                self.songs.append(song_to_load)

    def save_songs(self, file_name):
        """
        writes CSV file line by line using the attributes from each song in the list
        :param file_name: name of file to save to
        :return: None
        """
        with open(file_name, "w") as open_file:
            write_to_file = csv.writer(open_file, delimiter=",", lineterminator="\n")
            for song in self.songs:
                write_to_file.writerow([song.title, song.artist, song.year, "y" if song.required else "n"])

    def sort_songs(self, attribute):
        """
        sorts the song list by the specified attribute (title, artist, year, is_required) and then by the title
        :param attribute: attribute to sort the songs by
        :return: None
        """
        self.songs.sort(key=attrgetter(attribute.lower(), "title"))
