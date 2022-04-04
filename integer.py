#!/usr/bin/env python3
# Created By: Titwech Wal
# Date: April.1. 2022

# program that asks the user to enter an
# integer. then says what integer it is


def main():
    # Get the integer from user
    user_input = float(input("Enter an integer: "))

    # Check if number is negative, positive or zero
    if user_input < 0:
        print("")
        print(user_input, "is a negitive number")
    elif user_input > 0:
        print("")
        print(user_input, "is a postive number")
    elif user_input == 0:
        print("")
        print(user_input, "is just zero!")


if __name__ == "__main__":
    main()
