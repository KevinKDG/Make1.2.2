#!/usr/bin/env python
"""
Een raadspelletje waarbij je een woord moet raden dat in een lijst staat
De lijst mag je kiezen:

    ofwel uit een bestand lezen
    ofwel zelf een lijst samenstellen in je script

"""


#               IMPORTS               #


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
__status__ = "Development"

#              VARIABLES              #
word = ["hello", "bonjour", "konnichiwa", "guten tag"]

#              MAIN CODE              #
def main():

    guess = input("Can you guess a popular greeting in different languages? Hint: English, French, German, Japanese: ")

    if guess == "hello" or guess == "bonjour" or guess == "konichiwa" or guess == "guten tag":
        print("You guessed correctly!")
    else:
        print("You're wrong :(")


if __name__ == '__main__':    #run tests if called from command-line
    main()