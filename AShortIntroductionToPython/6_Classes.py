# A Short Introduction To Python
# FILE 6 - CLASSES
# Adam Peterlein - Last updated 2019-01-29 with python 3.6.5 and Visual Studio 15.7.1.
# Any questions, suggestions, or comments welcome and appreciated.

#   At the top of my program I'm going to import all the modules I will be using:
from time import time

#       I have shown you several different types of variables, including tuples, lists, strings, 
#   floating point numbers, and integers. But how might one create your own type of "variable"?
#   The answer is classes. To illustrate I will create a class called "Student":
class Student:
#   This is the beginning of my class. All the indented blocks after this are part of the student 
#   class. Traditionally class names are capitalized. Inside my student class I'm going to define 
#   functions which we can do on our student objects.
    def __init__(self, name: str, grade: int) -> None:
#   This is kind of an odd piece of code. I've made a function inside of my student class called 
#   __init__ (notice the double underscores, called dunderscores in Python). What does it do? Well 
#   this is what is called the "initializer" and it is the function we call when we first create a 
#   new student object. More on this later, for right now notice it takes three arguments, self, name, 
#   and grade. The self argument is special. We don't pass this argument when we call the function, 
#   it get's passed automatically. It represents the current object. Notice there is not type hint for 
#   self. That is because the type of self is "Student," but if we try to assign "Student" as a type
#   hint the interpreter will give us an error: Student hasn't been defined yet. We can add attributes 
#   to the "self" object as follows:
        self.name = name
        self.grade = grade
#   Now both name and grade are parts of the student object. We could also make a variable that stores 
#   the time this student object was created:
        self.__created = time()
#   Recall that time() returns the seconds since January 1st, 1970. Notice the dunderscore in the name 
#   of our variable "__created"? This tells Python that the variable __created is private, meaning we 
#   can't access it other than from methods we define here, inside the class. Please note that __init__ 
#   functions always return None. Now let us define another method.
    def nameBackwards(self) -> str:
#   What I want this method to do is return the name of the student, but backwards. Recalling our days 
#   with iterables we can do this fairly easily:
        return self.name[::-1]
#   Recall that when we use square brackets in Python the first number is the start, then a colon, then 
#   the next number is the end. Leaving both blank gives us the entire iterable, in this case the entire 
#   name. The -1 represents the step size, - indicates that we want the string backwards, and 1 indicates 
#   that we want every letter. A 2 would give us every other letter, 3 every third letter, etc.
#       Now we have defined our class, lets see how we would use it.

if __name__ == "__main__":
#   Recall this snippet from file 1 means that this bit of code is only executed if the file is executed 
#   directly, not if we import this file as a module in another program.
    s = Student("Billy Smith", 9)
#   We have created a new student called s, with the name Billy Smith, and the grade 9. Notice that the 
#   __init__ function is called just with the name of the class itself. In this case the variable "s" is
#   the "self" of our init function.
#   We can access attributes in s easily:
    print(s.name)
    print(s.grade)
#   But if we tried to do print(s.__created) we would get an error. __created is private.
#   We can also call other function of student with s. For example:
    print(s.nameBackwards())
#   We can even make another student:
    d = Student("Jill Smith", 11)
    print(d.name)
    print(d.grade)
    print(d.nameBackwards())

#   End of file 6. Possible exercises:
#   1.  Add a method to our student class that returns the time it was created.
#   TODO: Add more exercises to file 6.
