# A Short Introduction To Python
# FILE 5 - LOOPS
# Adam Peterlein - Last updated 2019-01-28 with python 3.6.5 and Visual Studio 15.7.1.
# Any questions, suggestions, or comments welcome and appreciated.

#       It often becomes necessary when writing code to do something more than once. Perhaps it must be done a set number of time, perhaps it must be done until a condition is
#   met. Either way, the tools we use to accomplish this feat are called loops. We will discuss 3 types of loops in this file.
#   1.  For loops
#   2.  While loops
#   3.  Do while loops
# SECTION 1 - FOR LOOPS
#       For loops loop through a iterable. Recall from the previous file that an "iterable" is simply a collection of objects that has some order. For example, a list or a tuple.
#   For loops take these iterables and assign their contents to a variable one at a time. For example:
for i in [1, 2, 3]:
#   takes the list [1, 2, 3] and assigns it's elements to the variable "i." First i will be 1, and the contents of the loops will be executed, then i will be 2 and the contents
#   will be executed again, then i will be 3, the contents executed once more, then, finally, the loop terminates and the program moves on.
    print(i)
#   This print(i) is the only indented line, and therefore the entire contents of the loop. This loop will print 1 then 2 then 3 each on their own line.
#   This syntax might get tiring, one would imagine, if you needed to loop through the numbers 1 to 1000. To solve this Python has a built-in function called "range." Range takes
#   either two or three values. The first represents the start value, the second the stop, and the third the increment. If no third value is passed the increment is assumed to be
#   one. But be careful! Range will stop before the stop value, not on it. For example:
range(1,10)
#   gives 1, 2, 3, 4, 5, 6, 7, 8, 9. And
range(1,10,2)
#   gives 1, 3, 5, 7, 9. We could easily sum up the numbers 1 through 100 using a for loop and a range.
ans = 0
for i in range(1,101): # We stop at 101 so we include 100 in our calculation.
    ans += i # Recall that this is short for ans = ans + i.

print(ans)
# SECTION 2 - WHILE LOOPS
