text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
        ["Ephemeral", "lasts", "one", "day", "only"],
        ["Accolade", "is", "an", "expression", "of", "praise"]]
n = int(input())
word_list = [word for sentence in text for word in sentence if len(word) <= n]
print(word_list)
