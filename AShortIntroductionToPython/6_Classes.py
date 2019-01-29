# A Short Introduction To Python
# FILE 6 - CLASSES
# Adam Peterlein - Last updated 2019-01-29 with python 3.6.5 and Visual Studio 15.7.1.
# Any questions, suggestions, or comments welcome and appreciated.

#       I have shown you several different types of variables, including tuples, lists, strings, floating point numbers, and integers. But how might one create your own type of "variable"?
#   The answer is classes. To illustrate I will create a class called "Student":
class Student:
#   This is the beginning of my class. All the indented blocks after this are part of the student class. Traditionally class names are capitalized.
#   Inside my student class I'm going to define functions which we can do on our student objects.
    def __init__(self: Student, name: str, grade: int) -> None:
#   This is kind of an odd piece of code. I've made a function inside of my student class called __init__ (notice the double underscores, called dunderscores in Python). What does it do?
#   Well this is what is called the "initializer" and it is the function we call when we first create a new student object. More on this later, for right now notice it takes three arguments,
#   self, name, and grade. The self argument is special. We don't pass this argument when we call the function, it get's passed automatically. It represents the current object. We can add
#   attributes to the "self" object as follows:
        self.name = name
        self.grade = grade
#   Now both name and grade are parts of the 
