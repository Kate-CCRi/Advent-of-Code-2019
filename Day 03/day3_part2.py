# Import the regex package
import re

# Open the input file, read it into the "data" variable, and clean it up
f = open("test2.txt", "r")
data = f.read()
f.close()

# Split the input file into two entries in an array, one for each line
sep = data.splitlines()

# Turn the lines into two arrays of objects split on ,
line1 = sep[0].split(",")
line2 = sep[1].split(",")

line1_moves = []
line2_moves = []

def distances(input_list, output_list):
    for item in input_list:

        things = re.split("(\d+)", item)

        output_list.append([things[0], things[1]])



distances(line1, line1_moves)
distances(line2, line2_moves)

line1_points = []
line2_points = []

def init_points(input_list, output_list):

    x = 0
    y = 0

    for item in input_list:

        dir = item[0]
        dist = int(item[1])

        if dir == "R":
            i = 0
            while i < dist:
                output_list.append([x, y])
                i += 1
                x += 1
        elif dir == "L":
            i = 0
            while i < dist:
                output_list.append([x, y])
                i += 1
                x -= 1
        elif dir == "U":
            i = 0
            while i < dist:
                output_list.append([x, y])
                i += 1
                y += 1
        elif dir == "D":
            i = 0
            while i < dist:
                output_list.append([x, y])
                i += 1
                y -= 1
    del(output_list[0])

init_points(line1_moves, line1_points)
init_points(line2_moves, line2_points)

steps = 0

"""
In the long run, you really only need the first intersection -- that will by definition be the smallest number of steps - maybe start by finding that?
"""


for item in line1_points:
    if item in line2_points:

        dist1 = line1_points.index(item) + 1
        dist2 = line2_points.index(item) + 1

        dist_tot = dist1 + dist2

        if steps == 0:
            steps = dist_tot
        elif dist_tot < steps:
            steps = dist_tot

print(steps)
