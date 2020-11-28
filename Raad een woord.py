#!/usr/bin/env python
"""
Een raadspelletje waarbij je een woord moet raden dat in een lijst staat
De lijst mag je kiezen:

    ofwel uit een bestand lezen
    ofwel zelf een lijst samenstellen in je script

"""


#               IMPORTS               #
import time

#          AUTHOR INFORMATION         #

#        _____
#      .'     `.
#     /  .-=-.  \   \ __
#     | (  C\ \  \_.'')
#     _\  `--' |,'   _/
#    /__`.____.'__.-' The coding snail~

__author__ = "Kevin Vervloet"
__email__ = "kevin.vervloet@student.kdg.be"
__Version__ = "(Code version)"
__status__ = "Finished"

#              VARIABLES              #
list = ["hello", "bonjour", "konnichiwa", "guten tag"]


#              MAIN CODE              #
def main():

    guess = input("""Can you guess one of these popular greetings?
    Hint: English, French, German, Japanese: """)

    if guess in list:
        print("You guessed correctly!")
    else:
        print("You're wrong :(, Try again")
        time.sleep(0.5)
        main()


if __name__ == '__main__':    #run tests if called from command-line
    main()