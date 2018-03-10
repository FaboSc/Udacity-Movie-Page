class Movie:
    '''Class that saves Movie title, poster Url and trailer link'''

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        '''Constructor of the Class
            Sets the class values when creating a movie object

            Parameters
            ----------
            title: String
                Title of the movie
            poster_image_url: String
                Url of the movie poster image
            trailer_youtube_url: String
                Url of the movie trailer in youtube
        '''
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
