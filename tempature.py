#!/usr/bin/env python3

# Created by: Michael Zagon
# Created on: Oct 2021
# This program converts Celsius to Fahrenheit


def fahrenheit():
    # This function does the conversion

    Tc = 0
    Tf = 0

    # Input
    Celsius = input("Enter a temperature (°C): ")
    print("")

    # Process and Output
    try:
        Tc = int(Celsius)
        Tf = 9 / 5 * Tc + 32
        print("{0}°C is equal to {1}°F.".format(Tc, Tf))
    except Exception:
        print("\nInvalid Input")


def main():
    # This function calls functions

    # Call functions
    fahrenheit()

    print("\nDone.")


if __name__ == "__main__":
    main()
