def AreNumbersEven(numbers):
    output_list = []
    for n in numbers:
        if (n % 2) == 0:
            output_list.append(True)
        else:
            output_list.append(False)
    return output_list


# Read space delimited integers from stdin and 
# pass a list of them to AreNumbersEven()
numbers = raw_input()
integer_list = [int(i) for i in numbers.split(' ')]
even_odd_boolean_list = AreNumbersEven(integer_list)
print even_odd_boolean_list 
