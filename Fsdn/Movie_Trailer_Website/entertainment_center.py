"""
list of movies that goes into fresh_tomatoes.py file

"""

import media
import fresh_tomatoes

zootopia = media.Movie("Zootopia",
                        "http://t2.gstatic.com/images?q="
                        "tbn:ANd9GcQj1fU0-Idujcrs_MB2xEWbVEygeCkcjYUp4Z"
                        "-hSIPqgu0vFbQi",
                        "https://www.youtube.com/watch?v=WWFB-zrxn7o",
                        "March 4, 2016 (USA)",
                        "Byron Howard, Rich Moore")

storks = media.Movie("Storks",
                     "http://t3.gstatic.com/images?q="
                     "tbn:ANd9GcSQq_t91J3Rtb5v1gbnqGPF6BSDeFvtFcVmxU50"
                     "nuczt5KHWsP8",
                     "https://www.youtube.com/watch?v=Rqj8bz1sbk4",
                     "September 23, 2016 (USA)",
                     "Nicholas Stoller, Doug Sweetland")

life_of_pets = media.Movie("The Secret Life Of Pets", 
                           "http://t2.gstatic.com/images?q="
                           "tbn:ANd9GcQmH4RygTa2ipQP54pc6pJMde8e0iBbwVO"
                           "7LW1h1RhpX4zDhef6",
                           "https://www.youtube.com/watch?v=MbjZPbiOsEg",
                           "July 28, 2016 (Germany)",
                           "Chris Renaud, Yarrow Cheney")

kubo = media.Movie("KUBO And The Two Strings",
                   "http://t2.gstatic.com/images?q="
                   "tbn:ANd9GcRQeUx8alN89H9qOSbfZY9sKwIOECZSYcz2LA3auB3"
                   "bldJI-hmE",
                   "https://www.youtube.com/watch?v=ykD2W8U6wH4",
                   "August 19, 2016 (USA)",
                   "Travis Knight")

ratatouille = media.Movie("Ratatouille",
                          "http://upload.wikimedia.org/wikipedia"
                          "/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk",
                          "June 29, 2007 (USA)",
                          "Brad Bird, Jan Pinkava")

kungfu_panda_3 = media.Movie("Kung Fu Panda 3", 
                             "http://t0.gstatic.com/images?q="
                             "tbn:ANd9GcTv8AULgHD6dyYlMkjvC2YITU41wECw"
                             "kPSGxHUyr9DXvct7vwY2",
                             "https://www.youtube.com/watch?v="
                             "ytuUAve6VW4&disable_polymer=true",
                             "January 29, 2016 (USA)",
                             "Jennifer Yuh Nelson, Alessandro Carloni")

minions = media.Movie("Minions", 
                      "http://t2.gstatic.com/images?q="
                      "tbn:ANd9GcRbHFoQWQZLymKtwzfjVEvfNDOIdcWOL-tUFst"
                      "MC00m5OMf961D",
                      "https://www.youtube.com/watch?v=GGssZksONtY",
                      "July 10, 2015 (USA)",
                      "Pierre Coffin, Kyle Balda")

cinderella = media.Movie("Cinderella", 
                         "http://t1.gstatic.com/images?q="
                         "tbn:ANd9GcRl6ZJu9B44N_YzggP0_QMKJvGrSGWGGHSf"
                         "7Jv6eGXhJQMGdxny",
                         "https://www.youtube.com/watch?v=2kajFKO0fBQ",
                         "March 13, 2015 (USA)",
                         "Kenneth Branagh")

good_dinosaur = media.Movie("The Good Dinosaur", 
                            "http://t1.gstatic.com/images?q="
                            "tbn:ANd9GcRGAyjFdJJlz5XtNdDbO0fmwLswSdIZ"
                            "NTGMBdrVFi5nnss4AlHW",
                            "https://www.youtube.com/watch?v=q7LwbWH8nWo",
                            "November 25, 2015 (USA)",
                            "Peter Sohn")


angry_birds = media.Movie("The Angry Birds", 
                           "http://t3.gstatic.com/images?q="
                           "tbn:ANd9GcTL4cM7wCCXjCEoxmzvs_vmiQtNqrpMQ80r"
                           "gdjABG2_N-IEE-tp",
                           "https://www.youtube.com/watch?v=I-QSKuRa0to",
                           "May 11, 2016 (Trinidad and Tobago)",
                           "Clay Kaytis, Fergal Reilly")

spongebob = media.Movie("The Spongebob", 
                        "http://t0.gstatic.com/images?q="
                        "tbn:ANd9GcRSqIWmY8hI_csJFC9twZFOduvUtJBVRT1-y4"
                        "OgxzllJLoIMPjV",
                        "https://www.youtube.com/watch?v=n6BSuhCvJXI",
                        "January 28, 2015 (Belgium)", 
                        "Paul Tibbitt, Mike Mitchell")


finding_dori = media.Movie("Finding Dori",
                           "http://t1.gstatic.com/images?q="
                           "tbn:ANd9GcTPxyoxzLf33_chM3uqooaT3tiyEBbQmq"
                           "Jb0Ndbvpt6qfQ4ybIk",
		           "https://www.youtube.com/watch?v=agtOeNjC_3U",
                           "June 17, 2016 (USA)",
                           "Andrew Stanton, Angus MacLane, Jose Luis Angulo")

# movie instances added to movies list
movies = [zootopia,storks,life_of_pets,kubo,ratatouille,kungfu_panda_3,
          minions,cinderella,good_dinosaur,angry_birds,spongebob,
          finding_dori]

# calling the open_movies_page function in fresh_tomatoes module
fresh_tomatoes.open_movies_page(movies)
