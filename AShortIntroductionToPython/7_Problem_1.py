euler = __import__("6_Intro_To_Euler_Problems")

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def Attempt_One():
    ans = 0
    for i in range(1,1000):
        if i % 3 == 0 or i % 5 == 0:
            ans += i
    return ans

def Attempt_Two():
    return sum(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(1,1000)))

if __name__ == "__main__":
    atmpt_1 = euler.Problem(Attempt_One, 1)
    euler.display(*atmpt_1.run())

    atmpt_2 = euler.Problem(Attempt_Two, 1)
    euler.display(*atmpt_2.run())
