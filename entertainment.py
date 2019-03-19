

import media
import marvelhub

avengers1 =  media.Movie("The Avengers",
	"S.H.I.E.L.D. leader Nick Fury is compelled to launch the Avengers Initiative when Loki poses a threat to planet Earth. His squad of superheroes put their minds together to accomplish the task.",
	"https://pre00.deviantart.net/8549/th/pre/i/2012/091/2/c/____the_avengers_______movie_poster_by_andrewss7-d4un6qw.jpg",
	"https://www.youtube.com/watch?v=eOrNdBpGMv8")

avengers2 =  media.Movie("Avengers: Age of Ultron",
	"Tony Stark builds an artificial intelligence system named Ultron with the help of Bruce Banner. When the sentient Ultron makes plans to wipe out the human race, the Avengers set out to stop him.",
	"https://upload.wikimedia.org/wikipedia/en/f/ff/Avengers_Age_of_Ultron_poster.jpg",
	"https://www.youtube.com/watch?v=tmeOjFno6Do")


avengers3 =  media.Movie("the avengers end game",
	"The Avengers unite to battle their most powerful enemy yet -- the evil Thanos. On a mission to collect all six Infinity Stones, Thanos plans to use the artifacts to inflict his twisted will on reality.",
	"https://i.redd.it/wmqx4vhgt4s01.jpg",
	"https://www.youtube.com/watch?v=6ZfuNTqbHE8")




movies=[avengers1,avengers2,avengers3]

marvelhub.open_movies_page(movies)





