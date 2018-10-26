import media
import fresh_tomatoes

def main():

    the_matrix = media.Movie("The Matrix","A dystopian future with a simulated reality",'https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg','https://www.youtube.com/watch?v=vKQi3bBA1y8')
    interstellar = media.Movie("Interstellar","Exploration mission to find a planet which can sustain life.",
                                    "http://www.animationmagazine.net/wordpress/wp-content/uploads/Interstellar-post.jpg","https://www.youtube.com/watch?v=zSWdZVtXT7E")
    blade_runner = media.Movie("Blade Runner 2049","A dystopian future showing an impending war between humans and replicants.",
                                    "https://upload.wikimedia.org/wikipedia/en/9/9b/Blade_Runner_2049_poster.png","https://www.youtube.com/watch?v=gCcx85zbxz4")    
    arrival = media.Movie("Arrival","Communication with aliens arrived on Earth",'https://upload.wikimedia.org/wikipedia/en/d/df/Arrival%2C_Movie_Poster.jpg','https://www.youtube.com/watch?v=tFMo3UJ4B4g')
    jurassic_world = media.Movie("Jurassic World","Jurassic Park reopened leading to new problems",'https://upload.wikimedia.org/wikipedia/en/6/6e/Jurassic_World_poster.jpg','https://www.youtube.com/watch?v=RFinNxS5KN4')
    spotlight = media.Movie("Spotlight","Daring investigation done by a group of journalists",'https://upload.wikimedia.org/wikipedia/en/f/f3/Spotlight_%28film%29_poster.jpg','https://www.youtube.com/watch?v=EwdCIpbTN5g')

    
    movies = [the_matrix,interstellar,blade_runner,arrival,jurassic_world,spotlight]   
    fresh_tomatoes.open_movies_page(movies)

if __name__=='__main__':
    main()

