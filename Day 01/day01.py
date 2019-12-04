# import the math module so you can use it later
import math

# this is a function that forces it to round down rather than up
def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier

# read in the data file and split it into lines
data = open("input.txt")
lines = data.readlines()

# PART ONE
# a global variable to hold the total
total1 = 0
total2 = 0

# for each line
for line in lines:

    # convert it from a string to a float
    line_num = float(line)

    # do the required math operations
    mass = line_num / 3
    mass = round_down(mass)
    mass = mass - 2

    # a testing output step
    print(mass)

    #add the resulting mass to the total
    total1 += mass

    # calculate the additional fuel needs for part 2

# print the final result
print(f"The part one fuel requirements are: {str(total1)}")
print(f"The part two fuel requirements are: {str(total2)}")

