string = input()
integers = [int(x) for x in string]
averages = [sum(integers[i:i + 2]) / 2 for i in range(len(integers) - 1)]
print(averages)
