class Song:
    """
    Song class initialises the attributes every song will have, how they will be printed and the ability to mark a
    song as required or learned
    """

    def __init__(self, title="", artist="", year=0, required=True):
        """
        initialises the attributes songs will have with default values
        :param title: title of the song
        :param artist: artist of the song
        :param year: year the song was made
        :param required: if the song is learned or unlearned (defaults True for un-learned)
        :return: None
        """
        self.title = title
        self.artist = artist
        self.year = year
        self.required = required

    def __str__(self):
        """
        specifies how songs will be printed and if they are learned or not
        :return: formatted string
        """
        check_learned = "" if self.required else "(learned)"
        return '"{}" by {} ({}) {}'.format(self.title, self.artist, self.year, check_learned)

    def mark_required(self):
        """
        marks the song as required (not learned)
        :return: song with required set to True (not learned)
        """
        self.required = True
        return self.required

    def mark_learned(self):
        """
        marks the song as learned
        :return: song with required set to False (learned)
        """
        self.required = False
        return self.required
