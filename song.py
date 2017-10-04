# create your Song class in this file


class Song:
    """Song class initialises the attributes every song will have, how they will be printed and the ability to mark a
    song as required or learned"""

    def __init__(self, title="", artist="", year=0, required=True):
        """initialises the attributes songs will have with default values"""
        self.title = title
        self.artist = artist
        self.year = year
        self.is_required = required

    def __str__(self):
        """specifies how songs will be printed and if they are learned or not"""
        check_learned = "" if self.is_required else "(learned)"
        return '"{}" by {} ({}) {}'.format(self.title, self.artist, self.year, check_learned)

    def mark_required(self):
        """marks the song as required (not learned)"""
        self.is_required = True
        return self.is_required

    def mark_learned(self):
        """marks the song as learned"""
        self.is_required = False
        return self.is_required
