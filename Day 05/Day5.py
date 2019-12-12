# Import the array functions
import array

# Open the input file, read it into the "data" variable, and clean it up
f = open("test.txt", "r")
data = f.read()
f.close()

# Split the input data into a list
nums = data.split(",")

# Convert each item into a integer/list

nums = list(map(int, nums))



def get_opcodes(input):
    """
    Process opcodes to get useful output.

    Parameters:
    an item from the input list

    Returns:
    a properly formatted opcode (including positions if applicable)

    What it does:
        * Takes an input
        * Checks the length to see if this is a one-digit code or a multi-digit code
        * If a one-digit code, returns it immediately
        * If a multi-digit code:
            * Adds 0 as necessary to bring it up to five characters
            * Reverses it to put the opcode first and the parameter codes second
            * Returns the reversed item
    """

    # If the opcode is one character long, return it immediately for processing
    if len(str(input)) == 1:
        return input

    # If the opcode is more than one character long, turn it into something that can be processed
    if len(str(input)) > 1:

        # Turn the input into a list of individual digits
        item = [int(char) for char in str(input)]

        # If all five positions are specified, reverse it (to put the opcode first) and return it
        if len(item) == 5:
            item.reverse()
            return item
        # Otherwise, put in zeroes until it does specify all five positions, then reverse and return it
        else:
            for i in range(5-len(item)):
                item.insert(0, 0)
            item.reverse()
            return item

def get_data(input_opcode, input_list):
    """
    Using a given opcode, get the data for processing based on what the opcode says

    Parameters:
        input_opcode: An opcode that specifies what parameters to get
        input_list: The list from which the parameters for processing will come from

    Returns:
        opcode: The opcode that specifies what to do with the data
        param1: The first piece of data to be processed
        param2: The second piece of data to be processed
        param3: The location in the list where the result of the processing should be stored
    """
    # This won't work because you don't have anything storing the index of the original opcode... Update the get_opcode function?

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