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
        return("The data getter found a break code.")

    elif len(str(input_opcode)) == 1:
        if input_opcode == 1 or input_opcode == 2:
            param1 = input_list[input_index + 1]
            param2 = input_list[input_index + 2]
            param3 = input_list[input_index + 3]
            data = [param1, param2, param3]
        else:
            param1 = input_list[input_index + 1]
            data = [param1]

    else:

        if input_opcode[1] == 9:
            return("The data getter found a break code.")
        else:
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
