# calculates π, accurate to 6 decimal digits. you can add more zeros to the range
# function near the top to get more accuracy, but the program runs pretty long because
# the Leibniz formula is slow
import numpy as np


def calc_pi():
    denominators = [3]
    for i in range(5, 10000001, 2):
        denominators.append(i)

    right_side = 1
    switch = 0
    # simulate the Leibniz formula to calculate π. https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80
    for i in denominators:
        if switch == 0:
            right_side = right_side - 1 / i
            switch = 1
        else:
            right_side = right_side + 1 / i
            switch = 0

    pi_estimate = right_side * 4

    return pi_estimate


def floor(num, precision=0):
    return np.round(num - 0.5 * 10**(-precision), precision)


π = calc_pi()

# floor the number to 6 decimals, because the calculation is not accurate beyond that
π_floored = floor(π,6)

print(π_floored)
