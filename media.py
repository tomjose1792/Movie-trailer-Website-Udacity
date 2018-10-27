"""The class Movie is defined and it contains the details of a movie"""
import webbrowser


class Movie():
    """This class is for stores movie related information with
    its attributes.

    title: string to store title of a movie.
    storyline: string to store storyline of movie.
    poster_image_url: string to store url of movie poster.
    trailer_youtube_url: string to store url of trailer of a movie."""

    def __init__(self, movie_title, storyline, poster_link, trailer_link):
        """The instance variables are initialised"""
        self.title = movie_title
        self.storyline = storyline
        self.poster_image_url = poster_link
        self.trailer_youtube_url = trailer_link

        """The instance method show_trailer is defined"""
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)