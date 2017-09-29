"""(Incomplete) Tests for Song class."""
from song import Song

# test empty song (defaults)
song = Song()
print(song)
assert song.artist == ""
assert song.title == ""
assert song.year == 0
assert song.is_required

# test initial-value song
song2 = Song("Amazing Grace", "John Newton", 1779, True)
print(song2)

print("Title    - Expected: {:<15} Got {}".format("Amazing grace", song2.title))
print("Artist   - Expected: {:<15} Got {}".format("John Newton", song2.artist))
print("Year     - Expected: {:<15} Got {}".format(1779, song2.year))
print("Required - Expected: {:<15} Got {}".format(True, song2.is_required))

# test mark_learned()
# TODO: write tests to show the mark_learned() method works
