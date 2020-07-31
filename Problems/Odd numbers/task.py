input_string = (input())
integers = [int(x) for x in input_string]
odd_list = [x for x in integers if x % 2 == 1]
print(odd_list)
