"""
Tests each method of the SongList class showing how each one works at an individual level
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

# test sorting songs
print("----Testing sort----")
print("Unsorted SongList is:\n{}".format(song_list))
song_list.sort_songs("required")
print("Sorted SongList by learned or not then title is:\n{}".format(song_list))

# test adding a new Song
print("----Testing add_song----")
print("Adding {} to SongList".format(song))
song_list.add_song(song)
print("Updated SongList is: \n\n{}".format(song_list))

# test get_song_by_title()
print("----Testing get_song_by_title----")
print("With input: {}".format(str(song)))
print("Expected: {} | Got: {}".format('"Amazing Grace" by John Newton (1779)', song_list.get_song_by_title(str(song))))
print()
# test getting the number of required and learned songs (separately)
print("----Testing get_number_of_learned_songs & get_number_of_required_songs----")
print("SongList is: \n{}".format(song_list))
print()
print("Expected # of learned songs:  {} | Got: {}".format(2, song_list.get_number_of_learned_songs()))
print("Expected # of required songs: {} | Got: {}".format(5, song_list.get_number_of_required_songs()))

# test saving songs (check CSV file manually to see results)
print()
print("----Testing save_songs on out_songs.csv----")
song_list.save_songs("songs.csv")
print("Check CSV file for results")
