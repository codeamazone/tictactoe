lines = int(input())
counter = 1
for _i in range(lines):
    result = counter * '#'
    result = result.center(lines * 2)
    print(result)
    counter += 2
