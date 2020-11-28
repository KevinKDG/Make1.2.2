#!/usr/bin/env python
"""
een script waarbij je om input vraagt achter een willekeurig woord en waarbij het script het woord achterstevoren
weergeeft.
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
__status__ = "Finished"

#              VARIABLES              #


#              MAIN CODE              #
def main():

    print("====The output of this program will be a backwards word====")
    word = input("Pick a random word: ")

    for i in reversed(word):
        print(i)


if __name__ == '__main__':  # run tests if called from command-line
    main()