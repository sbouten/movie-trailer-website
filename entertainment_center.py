""" Sheila Bouten...May 26, 2015...Project 1: Movie Website"""

import fresh_tomatoes 
import MovieWebsite

""" Movie details: instances of the class Movie """

little_mermaid = MovieWebsite.Movie("The Little Mermaid",
                                    "A love story of a mermaid turned human",
                                    "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQzgDW7g9uFU-n3ORkL9qgx70UTba6K4zLvcIak6DIfclLhTlX5",
                                    "https://www.youtube.com/watch?v=ZGZX5-PAwR8",
                                    "1898")

capote = MovieWebsite.Movie("Capote",
                            "The story of a writer and a criminal",
                            "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcS60gXnvADT52J8nqyDq2_S186XIwNNRi_0TAdNI4S-R1yomLhH",
                            "https://www.youtube.com/watch?v=-rWX7AFoOyI",
                            "2005")

emperors_new_groove = MovieWebsite.Movie("Emperor's New Groove",
                                         "The story of an emperor turned llama",
                                         "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcSGErxI8e6ZMFPgvazbKhjBo_KjaRtYjnTOfbgfk-5MeyiGvxMbqw",
                                         "https://www.youtube.com/watch?v=t_YjSbp5KHM",
                                         "2000")

furious_7 = MovieWebsite.Movie("Furious 7",
                               "Many cars",
                               "http://screenrant.com/wp-content/uploads/fast-furious-7-poster.jpg",
                               "https://www.youtube.com/watch?v=Skpu5HaVkOc",
                               "2014")

pretty_in_pink = MovieWebsite.Movie("Pretty in Pink",
                                    "A coming of age story",
                                    "http://moviefiles.alphacoders.com/115/poster-11521.jpg",
                                    "https://www.youtube.com/watch?v=F8vzL9Xdm_o",
                                    "1986")

""" All movies placed into an array """

movies = [little_mermaid, capote, emperors_new_groove, furious_7, pretty_in_pink]


fresh_tomatoes.open_movies_page(movies)


