euler = __import__("6_Intro_To_Euler_Problems")

# The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143?

from math import sqrt
factor = 600851475143

def isPrime(num):
    if num % 2 == 0:
        return False
    for i in range(3, int(sqrt(num)), 2):
        if num % i == 0:
            return False
    return True

def Attempt_One():
    mx = int(sqrt(factor))
    mx -= 1 if mx % 2 == 0 else 0
    for i in range(mx, 1, -2):
        if factor % i == 0 and isPrime(i):
            return i
    return -1

if __name__ == "__main__":
    atmpt_1 = euler.Problem(Attempt_One, 3)
    euler.display(*atmpt_1.run())

