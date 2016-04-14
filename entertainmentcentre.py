# import all the necessary stuff for our program
import media
import fresh_tomatoes

# list of 6 movies displayed on the webpage
""" media.Movie() refers to an instance
of the Movie class contained in the media file """
jurassic_world = media.Movie("Jurassic World",
                        "https://image.tmdb.org/t/p/w185/ce9vGDMexoihZ8ta3Zt60k4FChb.jpg",  # noqa
                        "https://www.youtube.com/watch?v=RFinNxS5KN4"
                        )

avatar = media.Movie("Avatar",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",  # noqa
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY"
                     )

birdman = media.Movie("Birdman",
                      "https://image.tmdb.org/t/p/w185/zJF4JKbaYUhKFWbwY4u5WpvgvER.jpg",  # noqa
                      "https://www.youtube.com/watch?v=uJfLoE6hanc"
                      )

the_hobbit = media.Movie("The Hobbit: The Battle of the Five Armies",
                     "https://image.tmdb.org/t/p/w185/vgAHvS0bT3fpcpnJqT6uDTUsHTo.jpg",  # noqa
                     "https://www.youtube.com/watch?v=iVAgTiBrrDA"
                     )

guardians_of_the_galaxy = media.Movie("Guardians of the Galaxy",
                        "https://image.tmdb.org/t/p/w185/9gm3lL8JMTTmc3W4BmNMCuRLdL8.jpg",  # noqa
                        "https://www.youtube.com/watch?v=crIaEzXgqto"
                        )

captain_america = media.Movie("Captain America: The Winter Soldier",
                        "https://image.tmdb.org/t/p/w185/pH4oeiZAh9a40tly4D0l6aAB3ms.jpg",  # noqa
                        "https://www.youtube.com/watch?v=7SlILk2WMTI"
                        )
movies = [jurassic_world, avatar, birdman, the_hobbit,
          guardians_of_the_galaxy, captain_america]
fresh_tomatoes.open_movies_page(movies)
