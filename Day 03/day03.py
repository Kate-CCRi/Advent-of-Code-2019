# Import array functions
import array

# Open the input file, read it into the "data" variable, and clean it up
f = open("test.txt", "r")
data = f.read()
f.close()

sep = data.splitlines()

line1 = sep[0].split(",")
line2 = sep[1].split(",")

line1_mover = []
line2_mover = []

def mover(source_array, target_array):

    print(source_array)
    print(target_array)
    coords = [0, 0]

    for index in range(0, len(source_array)):
        move = source_array[index]
        move = [char for char in move]

        if move[0] == "U":
            coords[0] += int(move[1])
        elif move[0] == "D":
            coords[0] -= int(move[1])
        elif move[0] == "R":
            coords[1] += int(move[1])
        elif move[0] == "L":
            coords[1] -= int(move[1])

        target_array += (coords)

        print(coords)
        print(target_array)



    return(target_array)

line1_coords = mover(line1, line1_mover)
line2_coords = mover(line2, line2_mover)

potentials = []

for index in line1_coords (0, len(line1_coords), 2):
    for index in line2_coords (0, len(line2_coords), 2):
        line1_x = line1[index]
        line1_y = line1[index + 1]
        line2_x = line2[index]
        line2_y = line2[index + 1]

        if line1_x == line2_x:
            attempt = [[line1_x, line1_y], [line2_x, line2_y]]
            potentials += attempt
        elif line1_y == line2_y:
            attempt = [[line1_x, line1_y], [line2_x, line2_y]]
            potentials += attempt

print(potentials)

