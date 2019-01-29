# A Short Introduction To Python
# FILE 4 - DATA STRUCTURES
# Adam Peterlein - Last updated 2019-01-28 with python 3.6.5 and Visual Studio 15.7.1.
# Any questions, suggestions, or comments welcome and appreciated.

#       In previous files we have discussed the basic types (integers, floats, strings, and booleans), but we have not yet discussed composite
#   types, such as data structures (collections of other elements). Python contains six built in data structures, four of which we shall discuss, 
#   and the last two of which are very uncommon and so I shall mention them only briefly while we're here so that you know of their existence.
#   The four built in data structures we're most interested in are:
#   1.  Strings - We have already seen strings, they are a sequence of characters.
#   2.  Lists - The most commonly used data structure, a list is simply an ordered collection of any number of values (including one or none).
#   3.  Tuples - Another ordered collection of several elements, we shall discuss the differences between lists and tuples a little later.
#   4.  Dictionaries - An unordered collection of key and value pairs.
#   And the two others are:
#   5.  Sets - Unordered collections of elements.
#   6.  Frozen Sets - Like sets, but a frozen set cannot be changed once it is declared. It is what's called "immutable." More on this later.
# SECTION 1 - STRINGS
#       Data structures consist of a series of element, in the case of strings these elements are characters. Unlike many other programming languages
#   a character itself is not a type in python, but rather is represented by a string of length 1.
a = "teststring"
#   In the example above we have defined a string. In this string the "t" character occupies the 0th index, the "e" character occupies the 1st index,
#   the "s" character occupies the 2nd index, and etc. We can access a single character from the string by index using square brackets:
print(a[0])
#   This prints the 0th index: "t." Likewise:
print(a[4])
#   Prints the 4th index: "s." We can also index from the back of the string. If we want to get the last character of a string we can do that with:
print(a[-1])
#   Or the second last:
print(a[-2])
#   We can get the length of the string with the len() function.
print(len(a))
#   Which prints 10, the length of our string. We can also select a range of a string. For example:
print(a[1:3])
#   This selects the characters from a string beginning at the character in the 1st index ("e") and stopping before the character in the 3rd index
#   ("t") and so returns the string "es." Omitting the number before the colon begins the selection at the first character. Ommitting the number
#   after the colon ends the selection at the end of the string. So:
print(a[:3]) # Prints "tes" and is equivalent to print(a[0:3])
print(a[1:]) # Prints "eststring" and is equivalent to print(a[1:-1])
print(a[:])  # Prints the entire string and is equivalent to print(a) or print(a[0:-1])
#   We can also select a range with a certain step. The step is how many indices are traversed after a character is selected. The default is 1, so
#   after a character is selected we just jump to the next character and select it. With a step of 2 we would select every other character:
print(a[::2]) # Prints "tssrn"
#   Or with a step of -1 we would reverse our selection:
print(a[::-1]) # Prints "gnirtstset" the string a backwards.
#   It is also important to note that strings in python are "immutable" i.e. they cannot be changed once set. If we want to change the second character
#   of our string (the one occupying the first index) from an "e" to an "a" we cannot simply do:
# a[1] = 'a'
#   As python will compain that you can't change strings that are already set. We would have to redefine our string completely. We could do that like so:
a = a[0] + 'a' + a[2:]
#   The '+' operator, recall, concatenates strings. The a[0] returns the first letter of our string, the 'a' is the letter we hope to insert, and the
#   a[2:] is the rest of the string after the replacement. We could define a function to replace one letter in any given string:
def replace(strng: str, indx: int, letter: str) -> str:
    return strng[:indx] + letter + strng[indx+1:]
# SECTION 2 - LISTS
#       Lists operate much like strings, but instead of being sequences of characters they are sequences of whatever one might like. Lists are defined
#   with square brackets and elements are seperated by commas. For example:
l = [1, 2, 3]
#   lists are indexed exactly like strings. That is to say one can access just the first element of the list as follows:
print(l[0])
#   or the first two elements of the list:
print(l[:2])
#   or the last element of the list:
print(l[-1])
#   It is very simple in python to turn other iterables into lists once can simply call the built-in list function.
print(list(a))
# SECTION 3 - TUPLES
#       Very similar to lists are tuples, defined with parentheses or sometimes nothing at all. For example:
t = (3, 1) # this is equivalent to t = 3, 1
#   The main difference between lists and tuples is that tuples are immutable like strings. Recall that immutable means they cannot be changed once created,
#   you have to create them all over again. Tuples are typically used in conjunction with functions in the following way. Say you have a function that takes a magnitude
#   and direction and returns the x and y components
from math import sin, cos

def XandY(dir: float, mag: float) -> (int, int):
    x = mag*cos(dir)
    y = mag*sin(dir)
    return x, y
#   We could also have simply written "return mag*cos(dir), mag*sin(dir)"

print(XandY(2.5, 5))
#   Now say we have a tuple r
r = (1.2, 15)
#   And we want to feed this tuple directly into the function XandY. We could do this with indexing:
XandY(r[0], r[1])
#   Or we could take advantage of the operator "*" which "unpacks" a tuple into it's individual values.
xy = XandY(*r)
print(xy)
# SECTION 4 - Dictionaries
#       Dictionaries are unlike any of the other data structures we've encountered so far in that they are not simply collections of individual elements (characters in the case of a string
#   or anything in the case of lists and tuples). Instead, dictionaries consist of name and value pairs. The name is a string which is used as the indentifier of the value, which can be almost
#   anything. For example:
d = {'a': 3, 'b': 'test', 'c': 1.2}
#   We have just created a new dictionary, d, and put into it the entries "a", which contains 3; "b", which contains the string "test"; and "c", which contains the number 1.2. To lookup a value
#   we simply use its key.
d['a'] # returns 3

#   End of file 4. Possible exercises:
#   TODO: Excercises for file 4.