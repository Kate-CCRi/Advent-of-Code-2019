# Import the array functions
import array

# Open the input file, read it into the "data" variable, and clean it up
f = open("input.txt", "r")
data = f.read()
f.close()

# Split the input data into a list
nums = data.split(",")

# Convert each item into a integer

nums = list(map(int, nums))

# Update the values in the array to what the problem asks for

nums[1] = 12
nums[2] = 2

def process_array(nums):

    # The working array "arr" is all of "nums" from start to finish
    arr = nums[:]

   # Iterate over the working array by 4s:
    for index in range(0, len(arr), 4):
        operator = arr[index]
        numberA = arr[arr[index+1]]
        numberB = arr[arr[index+2]]
        if operator == 99:
            return arr[0]
        elif operator == 1:
            arr[arr[index+3]] = numberA + numberB
        elif operator == 2:
            arr[arr[index+3]] = numberA * numberB

    return arr[0]

# Part 2 specific

# Range takes an argument that is one higher than where you want it to stop
for noun in range(100):
    # Nesting it this way makes it check each noun against each verb
    for verb in range(100):
        nums[1] = noun
        nums[2] = verb

        output = process_array(nums)

        if output == 19690720:
            print(100 * noun + verb)
            break