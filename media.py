import webbrowser

class Movie():

    
    def __init__(self,movie_title,storyline,poster_link,trailer_link):
        self.title = movie_title
        self.storyline = storyline
        self.poster_image_url = poster_link
        self.trailer_youtube_url = trailer_link 
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)