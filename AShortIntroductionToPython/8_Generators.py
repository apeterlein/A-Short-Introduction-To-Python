# A Short Introduction To Python
# FILE 8 - GENERATORS
# Adam Peterlein - Last updated 2019-01-29 with python 3.6.5 and Visual Studio 15.7.1.
# Any questions, suggestions, or comments welcome and appreciated.

from typing import Generator # Necessary only for generator type hints.

#       We will now discuss a special type of function: the generator. A generator is half function
#   half iterable. They work like this: a generator is created just like a function, except they
#   have so-called "yield" commands in them. When a new generator is created (just like a class is
#   created) you can get the first yield value with the next() command. At this point the generator
#   function executes up to the first yield command, and next() returns what is yielded. At this point
#   execution of the function is paused, right where it is, and is resumed the next time next() is
#   called. It then returns the next yielded value and pauses once more. This continues until we get
#   to an actual return statement, at which point the generator is done.
#       To make this all a little more concrete let us consider the following generator:
def fib(max: int) -> Generator[int, None, int]:
#   Here I have defined a generator in the same way I would define an ordinary function. Notice the type
#   hint: Generator[int, None, int]. The "Generator" tells us that the function is a generator and the 
#   three values tell us what the yield type, send type, and return type are respectively. Our function 
#   yields integers, cannot accept sends (don't worry about send type, it is an advanced topic we won't
#   cover), and returns another integer when all is said and done.
    previous = 0
    current = 1
    yield 0
#   Our first yielded value! On the first call of next() we'll get back 0 and the execution of the function
#   will pause here.
    yield 1
#   Another yield. Pause again.
    while current + previous <= max:
        tmp = current
        current = previous + current
        previous = tmp
        yield current
#   Another yield. This one will pause the function in the middle of a loop. That's no problem though. On 
#   the next call of next() it will pick up right where it left off.
    return current + previous
#   Finally a return value. This indicates the end of our generator. This generator generates fibbinacci 
#   numbers up to and including the given max.

if __name__ == "__main__":
#   Recall that this block of code is only executed when this file is run directly, not imported as a module.
    f = fib(8)
#   We create a new instance of our generator with a maximum of 8 and call it "f."
    for a in f:
#   Since a generator is a form of an iterable we can use a for loop to call next() for us. This for loop will
#   loop through the entire generator.
        print(a)

#   End of file 7. Possible exercises:
#   1.  Make a generator that yields all the prime numbers below a given maximum.
#   TODO: Add more exercises to file 8.