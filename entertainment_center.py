import media
import fresh_tomatoes

# Create Movies and add them to a List
lodr_fellowship = media.Movie("Lord of the Rings - The Fellowship of the Ring",
                              "https://upload.wikimedia.org/wikipedia/en/9/9d/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_%282001%29_theatrical_poster.jpg",
                              "https://www.youtube.com/watch?v=z_WZxJpHzEE")

despicable_me = media.Movie("Despicable Me",
                            "https://upload.wikimedia.org/wikipedia/en/d/db/Despicable_Me_Poster.jpg",
                            "https://www.youtube.com/watch?v=zzCZ1W_CUoI")

avengers = media.Movie("Marvel's The Avengers",
                       "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
                       "https://www.youtube.com/watch?v=eOrNdBpGMv8")

# Create movie_list and add movies
movie_list = [lodr_fellowship, despicable_me, avengers]

# Call fresh_tomatoes function in order to create a html page
fresh_tomatoes.open_movies_page(movie_list)
