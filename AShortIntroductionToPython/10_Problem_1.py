# A Short Introduction To Python
# FILE 9 - INTRO TO EULER PROBLEMS
# Adam Peterlein - Last updated 2019-01-29 with python 3.6.5 and Visual Studio 15.7.1.
# Any questions, suggestions, or comments welcome and appreciated.

#   This is the import of our helper file. This import statement looks a little weird. This is
#   because modules in python can't start with numbers. The work-around is to use this slightly
#   weird looking version of import.
euler = __import__("9_Intro_To_Euler_Problems")
#   This statement is equivalent to:
# import 9_Intro_To_Euler_Problems as euler

# PROBLEM STATEMENT
#   If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 
#   and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 
#   below 1000.

#   For our first attempt we will be kind of niave. It's often A good idea to start with the easy
#   approach and optimize from there, rather than trying to optimize and write at the same time.
def Attempt_One():
    ans = 0
#   First we declare a variable "ans" and set it to 0.
    for i in range(1,1000):
#   Next we loop through all the numbers 1 to 1000.
        if i % 3 == 0 or i % 5 == 0:
#   If they're a multiple of 3 or 5 we add them to answer.
            ans += i
#   And after we've looped all the way through we return the answer.
    return ans

#   Now let's try to be a little more clever. Let's try to use meta functions to make this program
#   a little shorter.
def Attempt_Two():
    return sum(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(1,1000)))
#   This line takes the range 1 to 1000 and filters out (using the filter method discussed earlier)
#   all the values that aren't multiples of 3 or 5. Then it finds the sum of this list.

if __name__ == "__main__":
    atmpt_1 = euler.Problem(Attempt_One, 1)
    euler.display(*atmpt_1.run())

    atmpt_2 = euler.Problem(Attempt_Two, 1)
    euler.display(*atmpt_2.run())
