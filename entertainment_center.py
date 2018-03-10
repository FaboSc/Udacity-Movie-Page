import media
import fresh_tomatoes

# Create Movies and add them to a List
lodr_fellowship = media.Movie("Lord of the Rings - The Fellowship of the Ring",
                              "https://en.wikipedia.org/wiki/The_Lord_of_the_Rings:_The_Fellowship_of_the_Ring#/media/File:The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_(2001)_theatrical_poster.jpg", "https://www.youtube.com/watch?v=V75dMMIW2B4")

despicable_me = media.Movie("Despicable Me", "https://en.wikipedia.org/wiki/Despicable_Me#/media/File:Despicable_Me_Poster.jpg",
                            "https://www.youtube.com/watch?v=sUkZFetWYY0")

avengers = media.Movie("Marvel's The Avengers", "https://en.wikipedia.org/wiki/The_Avengers_(2012_film)#/media/File:TheAvengers2012Poster.jpg",
                       "https://www.youtube.com/watch?v=eOrNdBpGMv8")

# Create movie_list and add movies
movie_list = [lodr_fellowship, despicable_me, avengers]

fresh_tomatoes.open_movies_page(movie_list)
