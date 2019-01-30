# A Short Introduction To Python
# FILE 3 - CONDITIONALS
# Adam Peterlein - Last updated 2018-06-27 with python 3.6.5 and Visual Studio 15.7.1.
# Any questions, suggestions, or comments welcome and appreciated.

#       An important structure in programming is the ability to define conditionals, i.e. do something 
#   if this is true, otherwise do something else (potentially nothing). In python conditionals take a 
#   very simple form
if True:
    # Do something
    pass
else:
    # Do something else
    pass
#   The "True" in the first statement can be replaced with the condition you want to evalutate. The 
#   "else" statement is optional, and can be preceded by any number of "elif" statements (short for "else 
#   if"). Notice the colon at the end of each line and the indented line following. This indented line is 
#   the body of the if statement. As before, the "pass" statement is a placeholder. Without the pass 
#   statement there would be nothing in the body of the conditional, which in python is unacceptable. 
#   The "pass" command does nothing.
#       Let us explore a slightly more complex if statement:
a = 6 * 2
if a == 12:
    print("Yep. It's 12.")
elif a == 13:
    print("That's weird. It's 13.")
else:
    print("It's not 12 or 13. It's " + str(a))
#   Let's break down that little snippet line-by-line. The first line is easy. We declare a variable "a" 
#   and set it equal to the product of 6 and 2. On the second line we check to see if the value stored 
#   in a is equivelent to 12 (a single "=" in python sets something equal to something else, a double "="
#   - written "==" and pronouced "is equivalent to" - checks if the left and right hand arguments are 
#   equivalent). The thrid line is within this if statement and prints a simple message. Then we have 
#   another similar elif statement that is evaluated only if the first if statement is not true. Finally 
#   we have the else statement, the catch-all bucket for when none of the other conditions are true. There 
#   is a small catch in the body of the else statement. The str() call. We would like to print out the value 
#   of a at the end of the line. To do this we must append the value of a to the end of the string we've 
#   already printed. We can't just use the "+" operator because python doesn't know how to add a string and 
#   a number, so we use str(a) to convert a to a string (12 becomes "12"). An equivalent way to write this 
#   is:
    print("It's not 12 or 13. It's", a)
#   Notice that because both of these lines are indented they both are within the else statement. I 
#   recommend changing the value of a we set earlier and seeing what happens. Note that the "==" operator 
#   takes two arguments, one of the right and one on the left, and returns a boolean (true or false) depending 
#   on whether they are equivalent or not. But it is not necessary to use this operator at all. One could use 
#   "!=" (not equal), ">" (greater than), "<=" (less than or equal to) and etc. Or one could use no comparison 
#   operator at all. For example:
m = True
if m:
    print("Yep, m is true")
#   Because there is no else statement nothing will be done if m is not true. We can also use "not" to flip 
#   a boolean, "and" to combine two conditions, or "or" to capture either one condition or another. An example 
#   of a complex conditional is:
if m and not a == 12:
    print("Interesting...")
#   This conditional is true if m is true and if a is not 12. Another way to write a not equal to 12 is "a != 12."
#       There is one final way python handles conditionals: the so-called "ternary conditional" or sometimes 
#   "ternary operator." The ternary refers to the fact that this operator takes three arguments, a condition, 
#   something to do if it's true, and something to do if it's false. It collapses the if else structure into one 
#   line. For example:
b = 1 if a == 12 else 2
#   This statement sets the value of b to be 1 if a is 12, and otherwise sets it equal to 2. As you can see this 
#   is significantly more compact than a full if else statement. Conditional statements can also be combined 
#   with the "and" and "or" operators. For example:
if b == 1 or b == 2:
    pass
#       Let us finally make our first usable program. We shall make a program that flips a coin and prints 
#   the result. Firstly we must get a random number (our coin flip):
from random import randint
coin = randint(0, 1)
if coin == 1:
    print("Heads!")
else:
    print("Tails!")
#   In this program we first get a random number between 0 and 1 (i.e. 0 or 1) and print "Heads!" if the 
#   number is 1, and print "Tails!" otherwise (i.e. if our random number is 0). A more concise way to 
#   write this program would be:
print("Heads!" if randint(0, 1) == 1 else "Tails!")
#   Perhaps we want to make our game a little more fun though. Maybe we could get the user to guess what 
#   the result of the coin flip is before they see it. Let's see. First we will need to flip a coin, but 
#   this time let's make the coin variable store the string "heads" or "tails" instead of 0 or 1.
coin = "heads" if randint(0, 1) == 1 else "tails"
#   Great! Now we just need to get the user to guess. In python user input from the console is taken with 
#   the "input()" function.
guess = str(input('Call it! (Type "heads" for heads and "tails" for tails): ')).lower()
#   The input command takes a string which it prints to prompt the user, then waits for the user to type 
#   something and hit enter. It then returns what they typed. Just to be safe  (in case the user types 
#   something odd, users can be an odd bunch sometimes) we use the str() function to make sure the result 
#   is a string, then use .lower() to make the result all lowercase before assigning guess that value.
#       Next we have to test whether or not the values of guess and coin are equivalent.
if guess == coin:
    print("You got it! Mazel tov!")
elif guess == "heads" or guess == "tails":
    print("Sorry, you got it wrong...")
else:
    print("Hmmm... I don't recognize that answer.")
#   The first block checks if you got it right, the second block checks that if you got it wrong that 
#   you at least gave a valid answer, and the last block catches invalid answers and warns the user 
#   that they've made a mistake.

#   End of file 3. Possible exercises:
#   1.  Create a program like we did before, but have the user guess the result of a dice roll.
#   2.  Declare a variable v that has the value one greater than the value the user puts in.