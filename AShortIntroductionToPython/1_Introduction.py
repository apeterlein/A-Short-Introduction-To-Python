# A Short Introduction To Python
# FILE 1 - INTRODUCTION
# Adam Peterlein - Last updated 2018-06-27 with python 3.6.5 and Visual Studio 15.7.1.
# Any questions, suggestions, or comments welcome and appreciated.

# Suggested prerequisits:
#   1.  A basic knowledge of some programming structures. No previous experience of python is assumed, but may be helpful
#   2.  The python interpreter. This tutorial assumes python 3, and the user is strongly discouraged from using python 2.
#   3.  A python development environment. This tutorial is generally distributed as a Visual Studio project file, and although
#       Visual Studio is not required, it is recommended. Other common options include Atom, PyCharm, and etc.

# Goals of this file:
#   1.  Provide a reader who is a complete beginner to python with a complete foundation of python programming.
#   2.  Teach a python-like thought process to help the reader create effecient python code.
#   2.  This is not an exhaustive reference on python. Not by a longshot. It is simply to give a good solid introduction and get
#       students to a level where they can comfortably write python programs. As such, a number of topic are not included, including
#       classes, file io, threading, python as glue, and many more. The interested student is intended to seek out further resources.
#       If you contact me with your specific learning desires I would be more than happy to point you to a good learning resource if
#       I know of one thaty suits your needs.
#   3.  Inspire a love of python. Python is a very popular programming language, and for good reason. There are a lot of reasons
#       to love python and programming. Above all else, I hope you have fun.

# How to use this tutorial:
#       To run an individual file in Visual Studio, right click on the name of the file in the Solution Explorer and click "Set
#   as Startup File" then click "Start" or "Attach..." (depending on your version of Visual Studio) in the top bar. Readers are
#   encouraged to run each file at least once to ensure they understand the content, and to edit files as often as they like.
#   Experimentation is an important component of learning.

# SECTION 1 - MODULES
#       Python is what is called an "interpreted language," meaning when you run a python file a program called the "interpreter"
#   takes the file line by line and translates what is contained within into something the computer can understand. This is contrasted
#   with compiled programming languages - such as C or fortran - where a program must be compiled (i.e. translated into a form the
#   computer can understand) beforehand. The rigors of the python interpreter will not be discussed in this document, as it is
#   considered beyond it's scope, but an interested reader is encouraged to seek out further information.
#       The first thing you may encounter at the the top of a python file are imported modules. These lines take a form similar to
#   the following:
import random
#   In this example we import a single module, called "random." A method from this module can then be used, as follows:
random.randint(1, 10)
#   The method "randint" is a function that takes two numbers, and returns as random number between them. More on functions later. 
#   Notice that the name of the method (in this example "randint") is preceded by the name of the module: "random," but one can
#   also manually set a name for the module:
import random as rand
#   Here we have once again imported the module "random" but this time we gave it the alias "rand." The same method as before can
#   once again be invoked using our new alias:
rand.randint(1, 10)
#   We can also import as single method only:
from random import randint
#   This method is then called without any prefix:
randint(1, 10)
#   We can give a method an alias as before:
from random import randint as random_number
random_number(1, 10)
#   Strictly speaking, imported modules are not required to be at the top of a python file, but it is good style to put them there. You may
#   additionally notice that unlike some programming languages, python does not require any sort of marker to end a statement (like ";" in C),
#   but rather python uses the linebreak itself as the end of the statement. This is called "syntactically significant whitespace" (we will
#   discuss how other whitespace is used in python later) and whether significant whitespace is clever and intuitive, or a horrible abomination
#   is the subject of heated debate amongst certain internet communities. The bottom line, however, is that you must be careful with linebreaks
#   and tabs in python. A statement can be broken into several lines with a "\" like:
random_number(1, \
              10)
#   In python we can write something to the console relatively easily using the "print" method. For example:
print(random_number(1, 10))
#   Something you may encounter in python programs may seem a bit odd at first:
if __name__ == "__main__":
    # Python code here
    pass
#   This line is for python files that can be used either as modules, or as standalone files. The code within the if statement will only be
#   executed if the file it is contained within is run directly, and not if the file is imported. The "pass" below it is included because python
#   does not like empty if statements. The "pass" operater does nothing, it is a so-called "null operator." It's inclusion will makes more sense
#   after our discussion on conditionals.

# SECTION 2 - VARIABLES
#       Python, like most other programming languages, makes heavy use of "variables," boxes into which we put information. There
#   are four basic types of variables:
#   1.  Integer - a whole number between negative and positive infinity, ex. 4.
#   2.  Float - float is an abreviation of "floating point number." Like an integer, a float is a number, but unlike an integer a
#       float can be any rational number, ex. 3.2.
#   3.  String - a string is a series of characters enclosed with single of double quotes, ex. "cat," or '423.'
#   4.  Boolean - True or False (always writeen proper case).
#   Unlike some programming launguages, python is "weakly typed" meaning when we create a variable to store data, python isn't particularly
#   picky about what sort of data we give it. As such, declaring a variable in python does not involve naming a type for that variable. For
#   example:
a = 10
print(a)
#   We have just created a variable called "a" and set the value of a to be the integer 10. We can redefine a to be the floating point number
#   10.0 using the statement:
a = 10.
print(a)
#   The "." implies to python that there could potentially be a decimal portion of this number, as so we intend it to be floating point. We could
#   also make a stand for the string "10":
a = "10"
print(a)
#   Be careful, however, strings are not equivelent to numbers. Notice what happens when we add:
a = 10 + 10
b = "10" + "10"
print(a, b)
#   Here the variable a contains the sum of 10 and 10, i.e. 20, but the variable b contains the result of "10" + "10." Python adds strings by
#   simply combining them, making the value of b "1010." Notice also that multiple values can be printed in one print statement seperated by a
#   comma.

#   End of file 1. Possible exercises:
#   1.  Print the sum of 10, 4, and 6.
#   TODO: Add more exercises to file 1.