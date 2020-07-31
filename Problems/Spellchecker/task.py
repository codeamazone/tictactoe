dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']
sentence = input().split()
output = [word for word in sentence if word not in dictionary]
print('\n'.join(output) if len(output) >= 1 else 'OK')
