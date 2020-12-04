#!/usr/bin/env python3

# created by: Ryan Walsh
# created on: December 2020
# this program checks if the number placed is negative or positive


def main():
    # this program checks if the number placed is negative or positive

    # input
    number_of_choice = int(input("Enter an integer: "))
    print("")

    # process & output
    if number_of_choice > 0:
        print("The number you placed in is positive: +")
    elif number_of_choice < 0:
        print("The number you placed in is negative: -")
    else:
        print("The number you placed in is zero")


if __name__ == "__main__":
    main()
