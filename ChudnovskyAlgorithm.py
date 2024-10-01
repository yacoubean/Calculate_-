# The interwebs say that the Chudnovsky Algorithm is the fastest way to calculate digits of π
# Note: see /ChudnovskyAlgorithm.png for an image of the algorithm

from math import factorial
from decimal import Decimal, getcontext
import datetime

# save start time to calculate how long this operation takes at the end
start_time = datetime.datetime.now()

# Set precision high enough for calculating and displaying the specified number of digits of π
num_digits = 1000
getcontext().prec = num_digits

finite_series = []

num_iterations = 100
# calculate π using the Chudnovsky Algorithm
for n in range(0,num_iterations):
    numerator = (-1) ** n * factorial(6 * n) * (545140134 * n + 13591409)
    denominator = factorial(3 * n) * factorial(n) ** 3 * Decimal(640320) ** (3 * n + Decimal(3) / 2)
    finite_series.append(Decimal(numerator) / denominator)

π = Decimal(1) / (12 * sum(finite_series))

print(π)

# calculate how long the algorithm took
end_time = datetime.datetime.now()
calc_time = round((end_time - start_time).total_seconds(),3)

print(num_digits, "digits of π calculated in", calc_time, "seconds")
