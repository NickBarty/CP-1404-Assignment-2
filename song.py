# create your Song class in this file


class Song:
    def __init__(self, title="", artist="", year=0, is_required=True):
        self.title = title
        self.artist = artist
        self.year = year
        self.is_required = is_required

    def __str__(self):
        check_learned = "" if self.is_required else "(learned)"
        return '"{}" by {} ({}){}'.format(self.title, self.artist, self.year, check_learned)

    def mark_required(self):
        self.is_required = True
        return self.is_required

    def mark_learned(self):
        self.is_required = False
        return self.is_required
