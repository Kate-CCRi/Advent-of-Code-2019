# Import the regex package
import re

# Open the input file, read it into the "data" variable, and clean it up
f = open("input.txt", "r")
data = f.read()
f.close()

# Split the input file into two entries in an array, one for each line
sep = data.splitlines()

# Turn the lines into two arrays of objects split on ,
line1 = sep[0].split(",")
line2 = sep[1].split(",")

line1_moves = []
line2_moves = []

# Split up the input moves into letters and numbers and put it back into a list as a sub-list
def distances(input_list, output_list):
    for item in input_list:

        things = re.split("(\d+)", item)
         output_list.append([things[0], things[1]])

# Run the "distances" code over line1 and line 2
distances(line1, line1_moves)
distances(line2, line2_moves)

line1_points = []
line2_points = []

# Turn the moves into a list of points, including all the interstitial points to make the complete list of points in the line
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

# Make the list of points for both lines
init_points(line1_moves, line1_points)
init_points(line2_moves, line2_points)

# Convert the list of points on the lines into sets
line1_set = set([])
line2_set = set([])

def make_set(input_list, output_set):
    for item in input_list:
        temp = tuple(item)
        output_set.add(temp)

make_set(line1_points, line1_set)
make_set(line2_points, line2_set)

# Get the intersections of the lines
intersections = line1_set.intersection(line2_set)

intersections_list = []

# Turn the set of intersections back into a list for easier manipulation
def make_list(input_set, output_list):
    for item in input_set:
        if item == (0, 0):
            next
        else:
            temp = list(item)
            output_list.append(temp)

make_list(intersections, intersections_list)

# For each intersection, pull the index out of the lists and add it, then print the lowest number
def fewest_total_steps():
    total_steps = [line1_points.index(i) + line2_points.index(i) for i in intersections_list]
    print(min(total_steps))

fewest_total_steps()