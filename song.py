# create your Song class in this file


class Song:
    def __init__(self, title="", artist="", year=0, is_required=True):
        self.title = title
        self.artist = artist
        self.year = year
        self.is_required = is_required

    def __str__(self):
        set_learned = "(learned)" if self.is_required else ""
        return '"{}" by {} ({}){}'.format(self.title, self.artist, self.year, set_learned )

    def mark_required(self):
        pass

    def mark_learned(self):
        pass
