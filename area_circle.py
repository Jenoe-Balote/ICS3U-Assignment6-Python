#!/usr/bin/env python3

# Created by Jenoe Balote
# Created on May 2021
# This program calculates the area of a circle

import constant


def calculate_area(radius_from_user):
    # calculate area
    area = constant.PI * radius_from_user ** 2

    return area


def main():
    # this function calls other functions
    # input

    print("Let's calculate the area of a circle!")
    print("")
    string_radius = str(input("Enter base (cm): "))

    # call function and output
    try:
        radius_from_user = int(string_radius)
        circle_area = calculate_area(radius_from_user)
        print("\nThe area is: {} cm².".format(circle_area))
    except Exception:
        print("\nInvalid.")
    finally:
        print("\nThanks for participating!")


if __name__ == "__main__":
    main()
