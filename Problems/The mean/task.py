number_string = input()
digits = [int(x) for x in number_string]
print(sum(digits) / len(digits))
