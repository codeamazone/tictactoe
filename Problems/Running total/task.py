sequence = input()
digit_list = [int(x) for x in sequence]
cumulative_sum_list = [sum(digit_list[0:x + 1]) for x in range(len(digit_list))]
print(cumulative_sum_list)
