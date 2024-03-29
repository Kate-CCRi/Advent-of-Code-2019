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
            opcode = int(str(item[0]) + str(item[1]))
            mode1 = item[2]
            mode2 = item[3]
            mode3 = item [4]
            return [opcode, mode1, mode2, mode3]
        # Otherwise, put in zeroes until it does specify all five positions, then reverse and return it
        else:
            for i in range(5-len(item)):
                item.insert(0, 0)
            item.reverse()
            opcode = int(str(item[1]) + str(item[0]))
            mode1 = item[2]
            mode2 = item[3]
            mode3 = item[4]
            return [opcode, mode1, mode2, mode3]

print(get_opcodes(1002))