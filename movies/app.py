import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", "A story of the boy and his toys that come to life.",
        "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg",
        "https://www.youtube.com/watch?v=4KPTXpQehio")

frozen = media.Movie("Frozen", "When the newly crowned Queen Elsa accidentally uses her "
                     "power to turn things into ice to curse her home in infinite winter, "
                     "her sister, Anna, teams up with a mountain man, his playful reindeer, "
                     "and a snowman to change the weather condition.",
                     "https://en.wikipedia.org/wiki/Frozen_(2013_film)#/media/File:Frozen_(2013_film)_poster.jpg",
                     "https://www.youtube.com/watch?v=TbQm5doF_Uc")
#print(frozen.storyline)

#frozen.show_trailer()

adidas_vs_puma = media.Movie("Adidas vs. Puma", "In the 1920s the two brothers Adolf and Rudolf Dassler "
                             "start manufacturing sport shoes. Adolf is a talented craftsman and his dream is "
                             "that one day all the best sportsmen in the world will ...", "https://images-na.ssl-images-amazon.com/images/M/MV5BMjZkMWRlMjctYTVhNy00YWI1LThkNjMtNjU2ZGVlNGY5MGU4XkEyXkFqcGdeQXVyNTY5NzI0MTQ@._V1_UY268_CR4,0,182,268_AL_.jpg",
                             "https://www.youtube.com/watch?v=tyT0VAfOEpQ")
ratatouille = media.Movie("Ratatouille","A rat who can cook makes an unusual alliance with a "
                          "young kitchen worker at a famous restaurant.",
                          "https://en.wikipedia.org/wiki/Ratatouille_(film)#/media/File:RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

secret_life_of_pets = media.Movie("Secret Life of pets", "The quiet life of a terrier named Max is upended when "
                                  "his owner takes in Duke, a stray whom Max instantly dislikes.",
                                  "https://en.wikipedia.org/wiki/The_Secret_Life_of_Pets#/media/File:The_Secret_Life_of_Pets_poster.jpg",
                                  "https://www.youtube.com/watch?v=eWI_Jsw9qUs")
ice_age = media.Movie("Ice Age: Continental Drift", "Manny, Diego, and Sid embark upon another adventure after their "
                      "continent is set adrift. Using an iceberg as a ship, they encounter sea creatures and battle "
                      "pirates as they explore a new world.",
                      "https://en.wikipedia.org/wiki/Ice_Age:_Continental_Drift#/media/File:Ice_Age_Continental_Drift.jpg",
                      "https://www.youtube.com/watch?v=xal3sxSSZp0")
movies= [toy_story, frozen, adidas_vs_puma, ratatouille, secret_life_of_pets, ice_age]

fresh_tomatoes.open_movies_page(movies)
