"""
(incomplete) Tests for SongList class
"""
from songlist import SongList
from song import Song

song = Song("Amazing Grace", "John Newton", 1779, True)

# test empty SongList
song_list = SongList()
print(song_list)
assert len(song_list.songs) == 0

# test loading songs
song_list.load_songs('songs.csv')
print("Loaded SongList: \n{}".format(song_list))
assert len(song_list.songs) > 0  # assuming CSV file is not empty

# TODO: add tests below to show the various required methods work as expected
# test sorting songs

# test adding a new Song
print("----Testing add_song----")
print("Adding {} to SongList".format(song))
song_list.add_song(song)
print("Updated SongList is: \n\n{}".format(song_list))

# test get_song()

# test getting the number of required and learned songs (separately)
print("----Testing get_number_of_learned_songs & get_number_of_required_songs----")
print("SongList is: \n{}".format(song_list))
print()
print("Expected # of learned songs:  {} | Got: {}".format(2, song_list.get_number_of_learned_songs()))
print("Expected # of required songs: {} | Got: {}".format(5, song_list.get_number_of_required_songs()))


# test saving songs (check CSV file manually to see results)
