# Open the input file, read it into the "data" variable, and clean it up
f = open("input.txt", "r")
data = f.read()
f.close()

# Split the input file into two entries in an array, one for each line
sep = data.splitlines()

# Turn the lines into two arrays of objects split on ,
line1 = sep[0].split(",")
line2 = sep[1].split(",")

# Initialize some blank arrays to use in a minute
line1_mover = []
line2_mover = []

# A function to create all the points defined by the moves in the input file
def mover(source_array, target_array):

    # Start at (0,0)
    coords = [0, 0]

    # For each item in the list:
    for index in range(0, len(source_array)):
        # Retrieve the item
        move = source_array[index]
        # This line basically splits the "word" into characters and pushes them back into move as an array
        move = [char for char in move]

        # Calculate the effects of each move and do the right thing to the coordinates
        if move[0] == "U":
            coords[0] += int(move[1])
        elif move[0] == "D":
            coords[0] -= int(move[1])
        elif move[0] == "R":
            coords[1] += int(move[1])
        elif move[0] == "L":
            coords[1] -= int(move[1])

        # Push the resulting point after each move into the target array
        target_array += (coords)

    # Return the array of points the line goes through
    return(target_array)

# Run the mover code on each set of moves to produce an array of coordinates
line1_coords = mover(line1, line1_mover)
line2_coords = mover(line2, line2_mover)

# Set up some more empty arrays
line1_real = []
line2_real = []

# A function that takes the coordinates produced by mover and turns them into a list of pairs
def make_coords(source_list, target_list):

    for index in range(0, len(source_list), 2):
        x = source_list[index]
        y = source_list[index + 1]

        temp = []
        temp.append(x)
        temp.append(y)

        target_list.append(temp)

# Fix the coordinate lists
make_coords(line1_coords, line1_real)
make_coords(line2_coords, line2_real)

line1_all = []
line2_all = []

def get_points(source_list, target_list):

    i_x = 0
    i_y = 0

    for point in source_list:
        x = point[0]
        y = point[1]

        if x == i_x:
            target_list.append(point)
        elif x <= i_x:
            while i_x >= x:
                point_temp = [i_x, y]
                target_list.append(point_temp)
                i_x -= 1
            else:
                i_x = x
        elif x >= i_x:
            while i_x <= x:
                point_temp = [i_x, y]
                target_list.append(point_temp)
                i_x += 1
            else:
                i_x = x

        if y == i_y:
            target_list.append(point)
        elif y <= i_y:
            while i_y >= y:
                point_temp = [x, i_y]
                target_list.append(point_temp)
                i_y -= 1
            else:
                i_y = y
        elif y >= i_y:
            while i_y <= y:
                point_temp = [x, i_y]
                target_list.append(point_temp)
                i_y += 1
            else:
                i_y = y


get_points(line1_real, line1_all)
get_points(line2_real, line2_all)

intersections = [value for value in line1_all if value in line2_all]

dist = []

for point in intersections:
    distance = abs(point[0]) + abs(point[1])
    if distance > 0:
        dist.append(distance)

print(min(dist))