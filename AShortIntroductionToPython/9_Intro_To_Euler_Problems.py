# A Short Introduction To Python
# FILE 9 - INTRO TO EULER PROBLEMS
# Adam Peterlein - Last updated 2019-01-29 with python 3.6.5 and Visual Studio 15.7.1.
# Any questions, suggestions, or comments welcome and appreciated.

#       For the remainder of this tutorial series we will focus on something called "Euler problems."
#   These are problems published on projecteuler.net designed specifically to be solved with computer
#   code. They increase in difficulty as they go, and although I will be the first to admit that I am
#   an engineer not a computer scientist and so my knowledge of effecient algorithms is limited, I hope
#   that Euler problems as a learning tool will prove as helpful and fun to you as they have been to
#   me.
#       My intention for this file is to build a module that we can import in our solutions to both time
#   our methods for finding the correct answer and to check the answer that we get. To that end we first
#   import a timer from the time module.
from time import perf_counter as timer
from typing import Callable

#   A list of the correct answers to problems, in order. No cheating!
answers = [
        233168,
        4613732,
        6857
    ]

#   Now we will define a class "Problem" this class will take two arguments, the first is the function
#   that generates the answer, and the second is the number of the problem (beginning from 1) so we can
#   check our answers.
class Problem:
    def __init__(self, fun: Callable[None], num: int) -> None:
#   Callable[None]
        self.fun = fun
        self.num = num
#   Our init function is very simple. It just takes the function and the number and attaches them to the
#   instance of our class.
#   Next we have the method that actually runs the function and returns 3 values. First the value the function
#   returned, then the correct answer, then the time it took the function to get there.
    def run(self) -> (float, float, float):
        t = timer()
        return self.fun(), answers[self.num-1], timer() - t

#   Finally, we have a method outside our function that helps us display the results.
def display(ans: float, answer: float, time: float) -> None:
    print("Result:\t", ans, "\nAnswer:\t", answer, "\n\t " + ("C" if ans == answer else "Inc") + \
        "orrect\nTime:\t", time, "\n")
#   Some things to note: "\t" represents a tab, "\n" represents a like break.

#   End of file 9.
