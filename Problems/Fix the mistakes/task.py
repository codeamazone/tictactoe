text = input()
words = text.split()
# result = [x for x in words if 'https://' in x.lower() or 'http://' in x.lower() or 'www.' in x.lower()]
for word in words:
    if 'https://' in word.lower() or 'http://' in word.lower() or 'www.' in word.lower():
        print(word)
# result = ' '.join(result)
# print(result.replace(' ', '\n'))
