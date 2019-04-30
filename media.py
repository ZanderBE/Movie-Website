import webbrowser

class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, launch_date, director):
        """This instance outlines the variables for each movie that will run through the Movie class."""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.launch_date = launch_date
        self.director = director
    def show_trailer(self):
        """This will open the movie's trailer from the youtube URL provided."""
        webbrowser.open(self.trailer_youtube_url)
