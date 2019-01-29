euler = __import__("6_Intro_To_Euler_Problems")

# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms 
# will be 1, 2, 3, 5, 8, 13, 21, 34, 55, and 89. By considering the terms in the Fibonacci sequence whose values do not exceed four 
# million, find the sum of the even-valued terms.

def Attempt_One():
    fib = [1, 2]
    while True:
        nxt = fib[-1] + fib[-2]
        if nxt > 4E6:
            break
        fib.append(nxt)
    return sum(filter(lambda x: x % 2 == 0, fib))

def fib(mx):
    lst, snd = 2, 1
    yield snd
    yield lst
    while True:
        nxt = lst + snd
        if nxt > mx:
            break
        yield nxt
        snd = lst
        lst = nxt
    
def Attempt_Two():
    return sum(filter(lambda x: x % 2 == 0, fib(4E6)))

def evenFib(mx):
    c, p = 1, 1
    yield 2
    while True:
        p += 2 * c
        c = 2 * p - c
        if(p + c > mx):
            break
        yield p + c

def Attempt_Three():
    return sum(evenFib(4E6))

def Attempt_Four():
    ans = 2
    c, p = 1, 1
    while True:
        p += 2 * c
        c = 2 * p - c
        if(p + c > 4E6):
            break
        ans += p + c
    return ans

if __name__ == "__main__":
    atmpt_1 = euler.Problem(Attempt_One, 2)
    euler.display(*atmpt_1.run())

    atmpt_2 = euler.Problem(Attempt_Two, 2)
    euler.display(*atmpt_2.run())

    atmpt_3 = euler.Problem(Attempt_Three, 2)
    euler.display(*atmpt_3.run())

    atmpt_4 = euler.Problem(Attempt_Four, 2)
    euler.display(*atmpt_4.run())
