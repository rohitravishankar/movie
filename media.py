# import all the necessary stuff to run our program
import webbrowser


# The Movie class describes all the properties common to any movie
class Movie():
    # __init__ function initialises all the instance variables of the class
    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

# show_trailer function to show the trailer for the movie
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
