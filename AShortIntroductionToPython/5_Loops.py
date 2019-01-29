# A Short Introduction To Python
# FILE 5 - LOOPS
# Adam Peterlein - Last updated 2019-01-29 with python 3.6.5 and Visual Studio 15.7.1.
# Any questions, suggestions, or comments welcome and appreciated.

#       It often becomes necessary when writing code to do something more than once. Perhaps it must be done a set number of time, perhaps it must be done until a condition is
#   met. Either way, the tools we use to accomplish this feat are called loops. We will discuss 2 types of loops in this file.
#   1.  For loops
#   2.  While loops
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
#   Now the loop is over and we can spit out the result.
print(ans)
#   Another, slightly more concise, way we could get to the same result:
ans = sum(range(1,101))
#   We could also use a for loop to cycle through types of iterables, including tuples.
for i in ('a', 'b', 'cde'):
    print(i,) # The comma at the end of this print statement prevents the automatic line-break
#   This code should print out "abcde."
#       We could achieve the same result looping through a string. Recall that strings are just an sequence of characters in python, so when we say
for i in 'abcde':
#   i first becomes 'a', then 'b', then 'c', etc.
    pass # Recall that the pass keyword tells python we don't actually want to do anything with the 
# SECTION 2 - WHILE LOOPS
#       Unlike for loops, while loops first check a condition, then, if the condition evaluates to true, executes the contents of the loop. Then it checks the condition again
#   and repeats the process. For example:
a = 0
while a < 10:
    a += 1
#   First we define a variable a, initially set to 0, then we hit the while loop. The condition of the while loop is that a is less than 10, which is currently is, so the loop is
#   executed. Inside the loop a is increased by 1, making it 1, and then the loop ends. The condition is then evaluated again and is again true, 1 < 10, so the loop is executed
#   again and a becomes 2, then 3, then 4, etc. until a becomes 10. Now at this point the while loops asks is 10 < 10? The answer is, of course, no, and so the loop ends.
#       Now you might ask, what happens if I want to end the loop early when a certain condition is met? Or what happens if the condition is always true? And to answer this question
#   I will introduce the "break" statement. Consider the following infinite loop:
while True:
#   Why is this loop infinite? Well True of course always evaluates as true, so the loop will never terminate. But say we wanted it to terminate anyways. We could use a break:
    break
#   This statement tells Python to immediately exit the loop. Say we want a program that waits exactly 2 seconds. We might start by getting the current time:
from time import time
start_time = time()
#   "start_time" is now a floating point number containing the number of seconds since the stroke of midnight, January 1st, 1970. Now for our loop:
while True:
#   An infinite loop! We'll need a break statement somewhere or the interpreter will just get stuck right here.
    if time() - start_time == 2:
        break
#   If the current time minus the time we started is 2, then we break out of the loop. Infinite loops, in general, are considered bad form. Here's a little bit of a nicer way we could
#   write the same thing:
start_time = time()
while time() - start_time < 2:
    pass

#   End of file 5. Possible exercises:
#   1.  Write a loop that adds 1 to a number for 5 seconds, see how high your computer can get!
#   TODO: Add more exercises to file 5.
