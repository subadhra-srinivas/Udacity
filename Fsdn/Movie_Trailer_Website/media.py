"""
This module contains the movie class that will be used in the 
entertainment_center.py file

"""

class Movie:
	"""
           This class provides a way to store movie related information
           Movie object is initialized below

           title:
                should be the movie title
           poster_image_url:
                must be the fully qualified image address url
                ex: "http://t2.gstatic.com/images?q="
                    "tbn:ANd9GcQj1fU0-Idujcrs_MB2xEWbVEygeCkc"
                    "jYUp4Z-hSIPqgu0vFbQi"
           trailer_youtube:
                need to be the youtube link
                ex:"https://www.youtube.com/watch?v=WWFB-zrxn7o" 
           release_date:
                release date of the movie
           directors:
                directors of the movie
        """

	def __init__(self,movie_title,poster_image,trailer_youtube,
                     release_date,directors):

		self.title = movie_title
                self.poster_image_url = poster_image
                self.trailer_youtube_url = trailer_youtube
                self.release_date = release_date
                self.directors = directors
