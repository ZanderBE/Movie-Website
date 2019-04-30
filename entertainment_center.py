import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that came to life.", "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc", "November 22, 1995", "John Lasseter")

twelve_angry_men = media.Movie("12 Angry Men", "Story of a jury made up of 12 men as they deliberate the conviction or acquittal of a defendant.", "https://upload.wikimedia.org/wikipedia/en/9/91/12_angry_men.jpg", "https://www.youtube.com/watch?v=A7CBKT0PWFA", "April 1957", "Sidney Lumet")

night_at_the_roxbury = media.Movie("A Night at the Roxbury", "The Butabi brothers will never be cool enough to make the Roxbury club's guest list.", "https://upload.wikimedia.org/wikipedia/en/0/02/A_night_at_the_roxbury.jpg", "https://www.youtube.com/watch?v=BuqeN2FjrRQ", "October 1, 1998", "John Fortenberry")

star_wars_new_hope = media.Movie("Star Wars: A New Hope", "Follow the the Rebel Alliance, led by Princess Leia (Fisher), and its attempt to destroy the Galactic Empire's space station, the Death Star.", "https://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg", "https://www.youtube.com/watch?v=1g3_CFmnU7k", "May 25, 1977", "George Lucas")

the_matrix = media.Movie("The Matrix", "Travel to a dystopian future in which reality as perceived by most humans is actually a simulated reality called 'the Matrix', created by sentient machines to subdue the human population", "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg", "https://www.youtube.com/watch?v=vKQi3bBA1y8", "March 31, 1999", "The Wachowski Brothers")

black_panther = media.Movie("Black Panther", "In Black Panther, T'Challa is crowned king of Wakanda following his father's death, but his sovereignty is challenged by an adversary who plans to abandon the country's isolationist policies and begin a global revolution.", "https://upload.wikimedia.org/wikipedia/en/0/0c/Black_Panther_film_poster.jpg", "https://www.youtube.com/watch?v=xjDjIWPwcPU", "February 16, 2018", "Ryan Coogler")

movies = [toy_story, twelve_angry_men, night_at_the_roxbury, star_wars_new_hope, the_matrix, black_panther]

fresh_tomatoes.open_movies_page(movies)
