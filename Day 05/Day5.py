# Import the array functions
import array

# Open the input file, read it into the "data" variable, and clean it up
f = open("test.txt", "r")
data = f.read()
f.close()

# Split the input data into a list
nums = data.split(",")

# Convert each item into a integer

nums = list(map(int, nums))
step = 1

for index in range(0, len(nums), step):

    if len(str(nums[index])) == 1:
        # Do the one-code operations
        print(nums[index])
        step = 1
    else:
        item = [int(char) for char in str(nums[index])]

        if item[0] == 0:
            item.reverse()
        else:
            item.insert(0, 0)
            item.reverse()

        opcode = [item[1]]
        param1_mode = item[2]
        param2_mode = item[3]
        param3_mode = item[4]

        if opcode == 9:
            print("I hit an exit code!")
            break
        if param3_mode == 1:
            print("I hit a bad parameter!")
            break



        print(item)
        step = len(item)

"""
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
"""