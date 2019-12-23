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
    # If the input opcode is 99, break.
    if input_opcode == 99:
        return("The data getter found a break code.")

    # Otherwise, get the data - single-digit input codes have all parameters in position mode, so that's easy
    elif len(str(input_opcode)) == 1:

        # Opcodes 1 and 2 have three inputs - the first piece of data, the second piece of data, and the storage point
        if input_opcode == 1 or input_opcode == 2:
            param1 = input_list[input_index + 1]
            param2 = input_list[input_index + 2]
            param3 = input_list[input_index + 3]
            data = [param1, param2, param3]

        # Opcodes 3 and 4 only have one input - the location to store an input or get an output from
        else:
            param1 = input_list[input_index + 1]
            data = [param1]

    # This section handles multi-digit opcodes
    else:

        # If the opcode is 99, break
        if input_opcode[0] == 99:
            return("The data getter found a break code.")

        # Otherwise, get the data to the extent that it exists
        # TODO: This code works for inputs 1, 2, and 99, but not for 3 or 4 -- add a section that handles only having
        #  one parameter
        else:

            if input_opcode[1] == 0:
                param1 = input_list[input_list[input_index + 1]]
            else:
                param1 = input_list[input_index + 1]

            if input_opcode[2] == 0:
                param2 = input_list[input_list[input_index + 2]]
            else:
                param2 = input_list[input_index + 2]

            # Location storage info is always in position mode, but what you want returned is the position, not
            # the value currently stored in that position. (The current value does not matter except for opcode 4.)
            param3 = input_list[input_index + 3]

            data = [param1, param2, param3]

    return data