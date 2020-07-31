sequence = input().split()
number = input()
output = [str(x) for x in range(len(sequence)) if sequence[x] == number]
print(' '.join(output) if len(output) > 0 else 'not found')
