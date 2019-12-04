# Open the input file, read it into the "data" variable, and clean it up
f = open("input.txt", "r")
data = f.read()
f.close()

# Split the input data into a list
nums = data.split(",")

# Convert each item into a integer

nums = list(map(int, nums))

nums[1] = 12
nums[2] = 2

pos_place = 0
first_op_place = 1
second_op_place = 2
location_place = 3

while True:

    if nums[pos_place] == 1:
        op1_loc = nums[first_op_place]
        op2_loc = nums[second_op_place]
        op = nums[op1_loc] + nums[op2_loc]
        loc = nums[location_place]
        nums[loc] = op
        pos_place += 4
        first_op_place += 4
        second_op_place += 4
        location_place += 4
        print(nums)

    elif nums[pos_place] == 2:
        op1_loc = nums[first_op_place]
        op2_loc = nums[second_op_place]
        op = nums[op1_loc] * nums[op2_loc]
        loc = nums[location_place]
        nums[loc] = op
        pos_place += 4
        first_op_place += 4
        second_op_place += 4
        location_place += 4
        print(nums)

    elif nums[pos_place] == 99:
        break

    else:
        print("I found a number that doesn't work!")

print(nums)




