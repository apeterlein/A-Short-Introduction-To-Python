# A Short Introduction To Python
# FILE 2 - FUNCTIONS
# Adam Peterlein - Last updated 2019-01-28 with python 3.6.5 and Visual Studio 15.7.1.
# Any questions, suggestions, or comments welcome and appreciated.

#       Python allows for the defintion of functions, little peices of code outside the main body 
#   that one can invoke anywhere in the file. Functions are defined as follows:
def sum(first, second):
    c = first + second
    return c
#   In this example we defined a function called "sum" that takes two inputs (called first and second). 
#   Within the function the variable c is created (and exists only within the function, it cannot be 
#   refered to elsewhere, nor does it keep its value between uses of the sum function) and sets it to 
#   the sum of the two inputs. The function then returns the value of c. It is important to note that 
#   the two lines in this function could be rewritten more concisely as one line:
def sum_2(first, second):
    return first + second
#   The text within the function is indented. Indentation in python is used to seperate blocks of code. 
#   Tabs or spaces can be used but tabs are typical. The function we have defined might be used like this:
a = sum(10, 20) # returns 30
print(a)
#   This function call takes the two things we passed to our sum function (10 and 20) and sets them to be 
#   the variables first and second respectively. It then executes the contents of the function.

#   We can also use the functions python has provided for us. For example str() takes a single input and 
#   turns it into a string. For example if we feed it the integer 10:
b = str(10) # returns "10"
print(b)
#   Or we can use functions from modules we have imported. For example randint from the module random 
#   takes two integers and returns a random number between them.
import random
c = random.randint(1, 10)
print(c)

#   Functions can also return multiple values, packed into tuples which we shall discuss later. For 
#   example:
def sumAndDifference(input1, input2):
    return input1 + input2, input1 - input2
#   Here we return two values (serperated by a comma) the sum of input1 and input2, and the difference 
#   of input1 and input2. This function would be invoked like:
d, e = sumAndDifference(30, 10) # d = 40, e = 20
print(d, e)

#   Another thing you'll sometimes see with function is "type hints." These are clues we give to the 
#   reader about what kind of thing the function expects you to feed it and what sort of thing it might 
#   spit out. For example, a function that takes in an integer and returns a floating point number may 
#   be written as follows:
def sqrt(i: int) -> float:
    return i ** .5
#   Here the "i: int" tells us that the variable i needs to be an integer, and the "-> float" tells us 
#   that the functions returns a float. The operator "**" means "raised to the power of." We can also 
#   indicate that a function returns nothing at all with "-> None".

#   End of file 2. Possible exercises:
#   1.  Create a function that takes two inputs and returns their difference.
#   2.  Generate a random number between 50 and 100 and print that number divided by 20.
#   2.  Create a fucntion that takes two integers and returns the string equivelent of their sum.