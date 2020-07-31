prime_numbers = [n for n in range(2, 1001) if all([n % i for i in range(2, n - 1)])]
'''
for number in range(2, 1000):
    if all([number % i for i in range(2, number - 1)]):
        prime_numbers.append(number)
'''

