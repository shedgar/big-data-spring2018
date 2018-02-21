# PART A
friendship = ['my', 'friends', 'are', 'unhelpful']
print(friendship[2])
print(friendship[:2])
friendship.append('last')
print(friendship)
print(len(friendship))
friendship[4] = 'new'
print(friendship)

# PART B
sentence_words = ['I', 'am', 'learning', 'Python', 'to', 'munge', 'large', 'datasets', 'and', 'visualize', 'them']
print(' '.join(sentence_words))
sentence_words.reverse()
print(sentence_words)
sentence_words.sort()
sorted(sentence_words)
"""
.sort saves the changes to the list (the changes to its order) and does not
return anything, while sorted only returns a copy of the list, now sorted,
without changing the original
"""
sentence_words.sort(key = lambda a: a.lower())
print(sentence_words)

# PART C

# PART D

# PART E

# PART F

# PART G
