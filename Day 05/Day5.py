# Import the array functions
import array

# Open the input file, read it into the "data" variable, and clean it up
f = open("input.txt", "r")
data = f.read()
f.close()

# Split the input data into a list
nums = data.split(",")

# Convert each item into a integer/list
nums = list(map(int, nums))

# A variable to hold the index that we're working on so we can increment it later
current_index = 0

def opcode_computer(input_list):
    """
    The code that actually makes up the opcode computer.

    Parameter:
    The list of instructions and data to be processed by the opcode computer.

    Return:
    The "diagnostic code" represented by the return value.

    What it does:
        * Takes a list of instructions and data as input
        * Recursively:
            * Retrieves the opcode from the current index and stores it as a variable
            * Retrieves the data for that opcode and stores it as a list
            * Runs the appropriate processing for the opcode on the data retrieved
            * Stores the resulting value in the appropriate place
            * Increments the index to the next opcode value
            * Breaks and returns if it finds a "stop" code (opcode 99)
    """


    # Returns the opcode
    opcode = get_opcodes(input_list[current_index])

    # Returns the 3 parameters (1 and 2 will be data, 3 will be the storage location of the data)
    data = get_data(opcode, current_index, input_list)

    processed = opcode_processor(opcode, data, current_index, input_list)

    # TODO: Figure out what the return needs to be

    # Update the index to the next point you need to look at
    current_index += len(opcode)
    current_index += len(data)


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

def get_data(input_opcode, input_index, input_list):
    """
    Using a given opcode, get the data for processing based on what the opcode says

    Parameters:
        input_opcode: An opcode that specifies what parameters to get
        input_index: The index in the input list from which the opcode came
        input_list: The list from which the parameters for processing will come from

    Returns:
        opcode: The opcode that specifies what to do with the data
        param1: The first piece of data to be processed
        param2: The second piece of data to be processed
        param3: The location in the list where the result of the processing should be stored
    """

    if input_opcode == 99:
        break

    elif len(input_opcode) == 1:
        param1 = input_list[input_index + 1]
        param2 = input_list[input_index + 2]
        param3 = input_list[input_index + 3]

    else:

        if input_opcode[1] == 9:
            break

        if input_opcode[2] == 0:
            param1 = input_list[input_list[input_index + 1]]
        else:
            param1 = input_list[input_index + 1]

        if input_opcode[3] == 0:
            param2 = input_list[input_list[input_index + 1]]
        else:
            param2 = input_list[input_index + 1]

        if input_opcode[4] == 0:
            param3 = input_list[input_list[input_index + 1]]
        else:
            param3 = input_list[input_index + 1]

    data = [param1, param2, param3]

    return data


def opcode_processor(opcode, data, input_index, input_list):
    """
    Processes incoming opcodes and data and returns the appropriate values.

    Parameters:
         opcode: The opcode that specifies the operation to be performed
         data: The supporting data for the opcode operation
         input_index: The starting index of the opcode
         input_list: The starting input list of opcodes and data

    Returns:
        index: The updated index for the next opcode
        output_list: The updated list after the opcode process has happened
    """
    # Break if the code is 99 (or 9, if it was a multi-digit opcode):
    if opcode == 99 or opcode == 9:
        break

    if opcode == 1:
        input_list[data[3]] == data[1] + data[2]

    if opcode == 2:
        input_list[data[3]] == data[1] * data[2]

    if opcode == 3:
        val = input("Enter your value: ")
        # TODO: Figure out what goes here...

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
