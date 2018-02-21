# ---------------------------------- PART A ------------------------------------
# LISTS
# A.1 - Create a list containing any 4 strings.
friendship = ['my', 'friends', 'are', 'unhelpful']
# A.2 - Print the 3rd item in the list
print(friendship[2])
# A.3 - Print the 1st and 2nd item in the list using [:] index slicing.
print(friendship[:2])
# A.4 - Add a new string with text “last” to the end of the list and print the list.
friendship.append('last')
print(friendship)
# A.5 - Get the list length and print it.
print(len(friendship))
# A.6 - Replace the last item in the list with the string “new” and print
friendship[4] = 'new'
print(friendship)

# ---------------------------------- PART B ------------------------------------
# STRINGS
sentence_words = ['I', 'am', 'learning', 'Python', 'to', 'munge', 'large', 'datasets', 'and', 'visualize', 'them']
# B.1 - Convert the list into a normal sentence with join(), then print.
print(' '.join(sentence_words))
# B.2 - Reverse the order of this list using the .reverse() method, then print.
sentence_words.reverse()
print(sentence_words)
# B.3 - Now use the .sort() method to sort the list using the default sort order.
sentence_words.sort()
print(sentence_words)
# B.4 - Perform the same operation using the sorted() function. Provide a brief
# description of how the sorted() function differs from the .sort() method.
sorted(sentence_words)
"""
'.sort' saves the changes to the list (the changes to its order) and does not
return anything, while 'sorted' only returns a copy of the list, now sorted,
without changing the original
"""
# B.5 - Modify the sort to do a case case-insensitive alphabetical sort.
sentence_words.sort(key = lambda a: a.lower())
print(sentence_words)

# ---------------------------------- PART C ------------------------------------
# RANDOM FUNCTION
from random import randint
def random_between(x, bottom = 0):
    num = randint(bottom, x)
    return(num)
assert(0 <= random_between(100) <= 100)
assert(50 <= random_between(100, bottom = 50) <= 100)

# EXAMPLES
random_between(357, bottom = 29)
random_between(357)

# ---------------------------------- PART D ------------------------------------
# STRING FORMATTING FUNCTION
def bestseller(n, title):
    print(f'The number {n} bestseller today is: {title.title()}')

# EXAMPLE
bestseller(35, "dogs are nice")

# ---------------------------------- PART E ------------------------------------
# PASSWORD VALIDATION FUNCTION
def password(x):
    pw = list(x)
    j = 0
    k = 0
    l = 0
    for i in pw:
        if i.isdigit():
            j += 1
        if i.isupper():
            k = 1
        if (i=='!')|(i=='?')|(i=='@')|(i=='#')|(i=='$')|(i=='%')|(i=='^')|(i=='&')|(i=='*')|(i=='(')|(i==')')|(i=='-')|(i=='_')|(i=='+')|(i=='='):
            l = 1
    if (8 <= len(pw) <= 14) & (j >= 2) & (k == 1) & (l == 1):
        print("Yay! Your password is strong")
    if len(pw) < 8:
        print("Your password is too short")
    if len(pw) > 14:
        print("Your password is too long")
    if j < 2:
        print("Your password needs to include at least 2 digits")
    if k == 0:
        print("Your password needs to include at least one capital letter")
    if l == 0:
        print("Your password needs to include at least one special character")

# EXAMPLES
password("hi")
password("This is 2 many requirements!")
password("4m I val1d?")

# ---------------------------------- PART F ------------------------------------
# EXPONENTIATION FUNCTION
def exp(x, y):
    exponent = 1
    for i in range(y):
        exponent = exponent*x
    else:
        print(exponent)

# EXAMPLES
exp(2, 3)
exp(5, 4)

# ---------------------------------- PART G ------------------------------------
# MIN AND MAX FUNCTIONS
# solution based on hint (see examples at bottom)
def minimum(x):
    currentmin = sum(x)
    for i in range(len(x)):
        if x[i] < currentmin:
            currentmin = x[i]
    else:
        print(currentmin)

def maximum(x):
    currentmax = 0
    for i in range(len(x)):
        if x[i] > currentmax:
            currentmax = x[i]
    else:
        print(currentmax)

# alternate solution (see examples at bottom)
def altminimum(x):
    x.sort()
    print(x[0])

def altmaximum(x):
    x.sort()
    x.reverse()
    print(x[0])

# EXAMPLES
my_list = [5,87,54,92,67,3,23,18]
minimum(my_list)
maximum(my_list)
altminimum(my_list)
altmaximum(my_list)
