from time import perf_counter as timer

answers = [
        233168,
        4613732,
        6857
    ]

class Problem:
    def __init__(self, fun, num):
        self.fun = fun
        self.num = num
    def run(self):
        t = timer()
        return self.fun(), answers[self.num-1], timer() - t

def display(ans, answer, time):
    print("Result:\t", ans, "\nAnswer:\t", answer, "\n\t " + ("C" if ans == answer else "Inc") + "orrect\nTime:\t", time, "\n")
