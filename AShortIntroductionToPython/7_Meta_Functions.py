# A Short Introduction To Python
# FILE 7 - META FUNCTIONS
# Adam Peterlein - Last updated 2019-01-29 with python 3.6.5 and Visual Studio 15.7.1.
# Any questions, suggestions, or comments welcome and appreciated.

from functools import reduce

#       We discussed funtions at length, but there is another kind of function I would be remiss if I 
#   didn't mention: meta functions. A meta functions is a function that takes a function as an argument.
#   For example, one of the most common meta functions is the "map" function. Which takes a function and 
#   an iterable, and applies that function to all the elements of the iterable. Say we have a function:
def square(x: float) -> float:
    return x**2
#   and we wanted to apply that function to all the elements of the list:
a = [1, 2, 3, 4]
#   We might simply call
squares = map(square, a)
print(list(squares)) # Map returns a "map object," so we call list() to turn it back into a list
#   You see the map function takes each element of a (1, 2, 3, and 4) and applies the "sqaure" function 
#   to them. But map isn't usually used this way. It's usually used with something called a "lambda 
#   function." A lambda function is a kind of inline function. It's a shorthand for avoiding all of 
#   the notation that comes with a full function. The same map command with a lambda function might 
#   look like this:
squares = map(lambda x: x**2, a)
#   To define a lambda function we firts use the keyword lambda, followed by all the variables the 
#   function takes seperated by commas, in our case just "x," then a colon, then what the function 
#   returns. Let's look at a slightly more complex meta function: reduce. Reduce uses a function 
#   that takes two inputs and returns one. Reduce applies the function to the first two elements of 
#   the iterable, then applies the function to the result and the next element of the iterable. It 
#   continues this until there are no elements left in the list, and it returns the accumulated result. 
#   For example, say we wanted to sum list a.
s = reduce(lambda x, y: x + y, a)
#   Now our lambda function takes two arguments: x and y, and returns their sum.
print(s)
#       There is one more meta function I will discuss herein: filter. Filter is perhaps the most 
#   useful of the meta functions. It takes a function and an iterable like map and reduce, and 
#   returns all of the elements of the iterable for which the function evaluates to true. For example:
s = filter(lambda x: x % 2 == 0, a)
#   Returns a filter object containing only the even elements of a (the % operator is called a modulo, 
#   it returns the remainder of division, so if something mod 2 is 0 it means that something is evenly 
#   divisable by 2).
print(list(s))

#   End of file 7. Possible exercises:
#   1.  Use filter, map, and range to find the sum of the squares of 1 to 100.
#   TODO: Add more exercises to file 7.