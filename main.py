"""Importing the required libraries. The libraries used are Pandas, numpy and matplotlib"""
import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


#   Importing the required libraries. The libraries used are Pandas, numpy and matplotlib
def intchecker(num1):
    """high level support for userinput."""
    val = None
    try:
        val = int(num1)
        print("Input is an integer number.")
        print("Input number is: ", val)
        # break;
    except ValueError:
        try:
            float(num1)
            print("Input is an float number.")
            print("Input number is: ", val)
            # break;
        except ValueError:
            print("This is not a number. Please enter a valid number")


# A function that validates user input. If a user enters an the error in this function is displayed.
def inputvalidator(num):
    """Validate user selection """
    if 0 <= num > 3:
        print("Error! Please enter an integer between 1 and 3.")
        return 0
    return int(num)


def userinput():
    """Validate user selection"""
    while 1:
        try:
            num = input("1. Population Data\n2. Housing Data\n3. "
                        "Exit the Program\n: ")
            if inputvalidator(int(num)):
                break
        except ValueError:
            print("please Try again")
    return num


# This is a function that calculates the required statistics
# i.e. count, mean, standard deviation, min, max. Also,it plots the histogram.
def statcalculator(columndata):
    """Statcalculator"""
    print("Count = ", np.count_nonzero(columndata))
    print("Mean = ", np.mean(columndata))
    print("Standard Deviation = ", np.std(columndata))
    print("Min = ", np.min(columndata))
    print("Max = ", np.max(columndata))
    print("The Histogram of this column is now displayed.")
    plt.hist(columndata)
    plt.show()


# This function selects the columns in the housing data
def housingcolumnselector(columnname):
    """Housing column selector"""
    if column == "a":
        columnname = "AGE"
    if column == "b":
        columnname = "BEDRMS"
    if column == "c":
        columnname = "BUILT"
    if column == "d":
        columnname = "NUNITS"
    if column == "e":
        columnname = "ROOMS"
    if column == "f":
        columnname = "WEIGHT"
    if column == "g":
        columnname = "UTILITY"
    if column == "h":
        sys.exit()
    return columnname


# This function selects the column 9in the population data.
# It gets a letter between a and d and returns the name of the corresponding column.
def popchangeselector(columnname):
    """pop changes in selector"""
    if column == "a":
        columnname = "Pop Apr 1"
    if column == "b":
        columnname = "Pop Jul 1"
    if column == "c":
        columnname = "Change Pop"
    if column == "d":
        sys.exit()
    return columnname


# Start of the program.
print("***************** Welcome to the Python Data Analysis "
      "App**********\nSelect the file you want to analyze:")
# Prompting the user to select the type of file
filetype = int(userinput())  # IntInputcheckerinput("1. Population
# Data\n2. Housing Data\n3. Exit the Program\n\n")
# filetype=int(input("1. Population Data\n2. Housing Data\n3. Exit the
# Program\n\n"))
if filetype == 1:
    data = pd.read_csv("PopChange.csv")
    print("You have Selected Population Data\nSelect the column you "
          "want to analyze")
    while True:
        column = input("a. Pop Apr 1\nb. Pop Jul 1\nc. Change Pop\nd. "
                       "Exit\n\n").casefold()
        if column in ["a", "b", "c", "d"]:
            print("You selected", popchangeselector(column))
            break
        print("Error! Please enter a char between a and d.")
    ColumnHeader = data[popchangeselector(column)]
    print("The statistics for this column are:")
    statcalculator(ColumnHeader)
# If the customer selects 2, this block of statement is executed.
# The block facilitates the user to select the column he/she would
# like to analyze and displays the output.
if filetype == 2:
    data = pd.read_csv("Housing.csv")
    print("You have Selected Housing data\nSelect the column you want "
          "to analyze")
    while True:
        column = input("a. Age\nb. Bedrooms\nc. Built\nd. Nunits\ne. "
                       "Rooms\nf. Weight\ng. Utility\nh. "
                       "Exit\n\n").casefold()
        if column in ["a", "b", "c", "d", "e", "f", "g", "h"]:
            print("You selected", housingcolumnselector(column))
            break
        print("Error! Please enter a char between a and g.")
    ColumnHeader = data[housingcolumnselector(column)]
    print("The statistics for this column are:")
    statcalculator(ColumnHeader)
# If the user selects 3, this block is executed.
if filetype == 3:
    print("Exiting....")
    sys.exit()
