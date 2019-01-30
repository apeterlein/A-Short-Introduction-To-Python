# A Short Introduction To Python
# FILE 12 - PROBLEM 3
# Adam Peterlein - Last updated 2019-01-29 with python 3.6.5 and Visual Studio 15.7.1.
# Any questions, suggestions, or comments welcome and appreciated.

euler = __import__("9_Intro_To_Euler_Problems")

# PROBLEM STATEMENT
#   The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the 
#   number 600851475143?

factor = 600851475143 # The number to be factorized.

# A function to tell if a number is prime
def isPrime(num):
    # First a quick check. If it's 2 it's prime. If it's not 2, but is even, throw it away.
    if num == 2:
       return true
    if num % 2 == 0:
        return False
    # If it's divisible by any number between 3 and its square root, it's not prime.
    for i in range(3, int(num**.5), 2):
        if num % i == 0:
            return False
    # Otherwise it is.
    return True

def Attempt_One():
    # Sqaure root the target number.
    mx = int(factor**.5)
    # Subtract 1 if the target number is even.
    mx -= 1 if mx % 2 == 0 else 0
    # Starting at mx and decreasing by 2s
    for i in range(mx, 1, -2):
        # If it's a factor of the target and a prime we've found a prime factor! Since
        # We're counting down, the first one we find is the largest prime factor!
        if factor % i == 0 and isPrime(i):
            return i
    # Just in case there are no prime factors (like for 1) we return -1.
    return -1

# Run it and let's see how we do!
if __name__ == "__main__":
    atmpt_1 = euler.Problem(Attempt_One, 3)
    euler.display(*atmpt_1.run())
# If you can make a faster version of this program let me know! I love seeing fast sneaky
# math tricks.

