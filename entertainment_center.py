import fresh_tomatoes
import media

#Movie content for the page including poster and trailer.
harry_potter = media.Movie("Harry Potter",
                        "Harry Potter is a wizzrd and is set to defeat the evil Lord Voldemort.",
                        "https://vignette2.wikia.nocookie.net/harrypotter/images/2/23/Tt0373889_largeCover.jpg/revision/latest?cb=20090604141238",
                        "https://www.youtube.com/watch?v=JYLdTuL9Wjw")
    

breakfast = media.Movie("Breakfast At Tiffany's",
                     "A beautiful girl living in New York City",
                     "https://upload.wikimedia.org/wikipedia/en/a/a9/Breakfast_at_Tiffanys.jpg",
                     "https://www.youtube.com/watch?v=urQVzgEO_w8")                     


la_la_land = media.Movie("La La Land",
                        "Struggling actress and out of date jazz player fall in love and figure out life.",
                        "http://www.impawards.com/2016/posters/la_la_land_ver3.jpg",
                        "https://www.youtube.com/watch?v=0pdqf4P9MB8")

selena = media.Movie("Selena",
                          "Storyline",
                          "https://images-na.ssl-images-amazon.com/images/I/51CVMPPGSML.jpg",
                          "https://www.youtube.com/watch?v=EVMSuZXEz4s")

super_bad = media.Movie("Superbad", "Storyline",
                                "http://www.impawards.com/2007/posters/superbad.jpg",
                                "https://www.youtube.com/watch?v=1EnGKC9Lk_Y")

star_wars = media.Movie("Star Wars: Episode V", "Storyline",
                           "https://s-media-cache-ak0.pinimg.com/originals/81/76/18/8176180953311ef1d6efa99af8254dcd.jpg",
                           "https://www.youtube.com/watch?v=JNwNXF9Y6kY")


                             
movies = [harry_potter, breakfast, la_la_land, selena, super_bad, star_wars]

fresh_tomatoes.open_movies_page(movies)
#print (media.Movie.__dict__)
