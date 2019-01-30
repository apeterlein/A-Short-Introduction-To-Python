# A Short Introduction To Python
# FILE 8 - GENERATORS
# Adam Peterlein - Last updated 2019-01-29 with python 3.6.5 and Visual Studio 15.7.1.
# Any questions, suggestions, or comments welcome and appreciated.

from typing import Generator

#       We will now discuss a special type of function: the generator. 

def fib(max: int) -> Generator[int, None, int]:
    previous = 0
    current = 1
    yield 0
    yield 1
    while current + previous <= max:
        tmp = current
        current = previous + current
        previous = tmp
        yield current
    return current + previous

if __name__ == "__main__":
    f = fib(8)
    for a in f:
        print(a)