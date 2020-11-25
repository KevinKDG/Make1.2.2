#!/usr/bin/env python
"""
Information about the script goes here
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
lijst = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


#              MAIN CODE              #
def main():

        #print("\n".join(map("".join, zip(*reversed(lijst)))))

        for i in range(len(lijst[0])):
                print(''.join(x[i] for x in lijst))

        print("And reverse")

        for i in range(len(lijst[0])):
                print(''.join(x[-(i+1)] for x in lijst))

if __name__ == '__main__':    #run tests if called from command-line
    main()

