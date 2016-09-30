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
print(frozen.storyline)

frozen.show_trailer()
