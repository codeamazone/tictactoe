sentence = input().split()
result = [word for word in sentence if word.endswith('s')]
print('_'.join(result))
