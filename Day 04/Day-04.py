# Since there are only two numbers in the input, I'll just hard-code them instead of importing from a file
input1 = 156218
input2 = 652527

num_doubles = []

# This generates every number in the range:

for number in range(input1, input2):

    # Makes a list of all the numbers with each number represented as a list itself
    num_list = [int(d) for d in str(number)]

    # For the index of every character in the number-as-a-list up to one before the end
    for index in range(0, (len(num_list) -1)):

        # If that character is not equal to the next one, go on to the next set of characters
        if num_list[index] != num_list[index + 1]:
            next
        # Otherwise, add it to the list of doubles and move on to the next number entirely ("break")
        else:
            num_doubles.append(number)
            break

count = 0

# For each index in the list of numbers containing doubles
for index in range(0, len(num_doubles)):

    # Pull the number at that index and turn it into a list
    num = num_doubles[index]
    num_list = [int(d) for d in str(num)]

    temp_count = 0

    # For the each index in the number-as-a list:
    for char_index in range(0, (len(num_list) - 1)):

        # If any digit is larger than the next digit, go on to the next number entirely
        if num_list[char_index] > num_list[char_index + 1]:
            break
        # Otherwise, increment the temp counter and move on to the next comparison
        else:
            temp_count += 1

        # If all five comparisons are correct, add one to the count
        if temp_count == 5:
            count += 1

print(count)





