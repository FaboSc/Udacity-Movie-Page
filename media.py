class Movie:
    '''Class that saves Movie title, poster Url and trailer link'''

    #Constructor
    def __init__(self, title, poster_image_url, trailer_youtube_id):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_id = trailer_youtube_id