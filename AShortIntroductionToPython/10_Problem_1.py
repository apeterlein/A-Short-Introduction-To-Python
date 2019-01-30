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
def Attempt_One() -> int:
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
def Attempt_Two() -> int:
    return sum(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(1,1000)))
#   This line takes the range 1 to 1000 and filters out (using the filter method discussed earlier)
#   all the values that aren't multiples of 3 or 5. Then it finds the sum of this list.

if __name__ == "__main__":
#   Make a new instance of our Problem class with the function Attempt_One.
    atmpt_1 = euler.Problem(Attempt_One, 1)
#   Recall that "*" "unpacks" a tuple. Meaning the following line is equivalent to:
#   tmp = atmpt_1.run()
#   euler.display(tmp[0], tmp[1], tmp[2])
#   just a little shorter.
    euler.display(*atmpt_1.run())

#   Now we try the same thing again with the second function.
    atmpt_2 = euler.Problem(Attempt_Two, 1)
    euler.display(*atmpt_2.run())
#       Which do you image will be faster and why? Run the program yourself and find out...
#   Ok, so the first one was faster. How come? The second one is shorter and uses more of those cool
#   builtin functions we learned about. We'll if we think about what the second one is doing it's first
#   determining which of the values in our range to keep, and then it adds them all together. The
#   difference is subtle, but notice it has to loop twice, first when it filters out values we don't want
#   and second when it sums up everything that's left. The first attempt only loops once.

#   As with all the other Euler problems you should now try to see if you can solve this Euler problem 
#   a different way. If you come up with a very clever solution feel free to email it to me at 
#   apeterlein@gmail.com.