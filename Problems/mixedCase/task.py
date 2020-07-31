text = input().split()
capital_list = []
for word in text:
    x = word.capitalize()
    capital_list.append(x)
capital_list[0] = capital_list[0].lower()
print(''.join(capital_list))
