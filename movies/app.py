import html_template
import media

toy_story = media.Movie("Toy Story", "A story of the boy and his toys that come to life.", "81 min.",
        "https://s-media-cache-ak0.pinimg.com/originals/ee/9f/21/ee9f21432dac3689d2d3100d2055f151.jpg",
        "https://www.youtube.com/watch?v=4KPTXpQehio")

frozen = media.Movie("Frozen", "When the newly crowned Queen Elsa accidentally uses her "
                     "power to turn things into ice to curse her home in infinite winter, "
                     "her sister, Anna, teams up with a mountain man, his playful reindeer, "
                     "and a snowman to change the weather condition.", "109 min.",
                     "http://b-i.forbesimg.com/scottmendelson/files/2013/11/Frozen-movie-poster.jpg",
                     "https://www.youtube.com/watch?v=TbQm5doF_Uc")
#print(frozen.storyline)

#frozen.show_trailer()

adidas_vs_puma = media.Movie("Adidas vs. Puma", "In the 1920s the two brothers Adolf and Rudolf Dassler "
                             "start manufacturing sport shoes. Adolf is a talented craftsman and his dream is "
                             "that one day all the best sportsmen in the world will ...", "115 min.", "https://images-na.ssl-images-amazon.com/images/M/MV5BMjZkMWRlMjctYTVhNy00YWI1LThkNjMtNjU2ZGVlNGY5MGU4XkEyXkFqcGdeQXVyNTY5NzI0MTQ@._V1_UY268_CR4,0,182,268_AL_.jpg",
                             "https://www.youtube.com/watch?v=tyT0VAfOEpQ")
ratatouille = media.Movie("Ratatouille","A rat who can cook makes an unusual alliance with a "
                          "young kitchen worker at a famous restaurant.", "115 min.",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

secret_life_of_pets = media.Movie("Secret Life of pets", "The quiet life of a terrier named Max is upended when "
                                  "his owner takes in Duke, a stray whom Max instantly dislikes.", "87 min.",
                                  "https://upload.wikimedia.org/wikipedia/en/6/64/The_Secret_Life_of_Pets_poster.jpg",
                                  "https://www.youtube.com/watch?v=eWI_Jsw9qUs")
ice_age = media.Movie("Ice Age: Continental Drift", "Manny, Diego, and Sid embark upon another adventure after their "
                      "continent is set adrift. Using an iceberg as a ship, they encounter sea creatures and battle "
                      "pirates as they explore a new world.", "88 min.",
                      "http://3.bp.blogspot.com/-4XOPU0FQ5FA/T_W4WGvT5OI/AAAAAAAAEFE/cJxVdrZhHgI/s640/Ice-Age-Continental-Drift-2012-poster.jpg",
                      "https://www.youtube.com/watch?v=xal3sxSSZp0")
movies= [toy_story, frozen, adidas_vs_puma, ratatouille, secret_life_of_pets, ice_age]

html_template.open_movies_page(movies)

