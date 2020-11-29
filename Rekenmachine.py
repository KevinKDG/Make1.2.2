#!/usr/bin/env python
"""
Een re-make van je rekenmachine die voldoet aan flowcontrol.

    Je vraagt de gebruiker om 2 getallen
    Je vraagt de gebruiker om een bewerking op te geven
    Je geeft correcte output

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


#              MAIN CODE              #
def main():

    try:
        Number_1 = int(input("Pick a number: "))        # Input, pick your first number
        Number_2 = int(input("Pick another number: "))  # Input, it lets you pick a second number

        what = input('''What would you like to do?              

            + for addition
            - for subtraction
            * for multiplication
            / for division
            ''')
        if what == "+":
            print(Number_1, "+", Number_2, "is", Number_1 + Number_2)

        elif what == '-':
            print(Number_1, "-", Number_2, "is", Number_1 - Number_2)

        elif what == '*':
            print(Number_1, "*", Number_2, "is", Number_1 * Number_2)

        elif what == '/':
            print(Number_1, "/", Number_2, "is", Number_1 / Number_2)

    except ValueError:                                              # If the input is not a number, retry
        print('this is not a valid number, Please try again')
        time.sleep(0.5)
        main()


if __name__ == '__main__':    #run tests if called from command-line
    main()