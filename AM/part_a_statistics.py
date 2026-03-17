# Part A - Statistics using Loops and Higher Order Functions

import numpy as np
from functools import reduce

# ---- A1: Using Loops ----

def mean(data):
    total = 0
    for x in data:
        total += x
    return total / len(data)

def median(data):
    arr = sorted(data)
    n = len(arr)
    if n % 2 == 0:
        return (arr[n//2 - 1] + arr[n//2]) / 2
    return arr[n//2]

def variance(data):
    m = mean(data)
    total = 0
    for x in data:
        total += (x - m) ** 2
    return total / len(data)

# ---- A2: Using Higher Order Functions ----

def mean_hof(data):
    return reduce(lambda a, b: a + b, data) / len(data)

def variance_hof(data):
    m = mean_hof(data)
    sq = list(map(lambda x: (x - m) ** 2, data))
    return reduce(lambda a, b: a + b, sq) / len(data)

# ---- A3: Student Marks ----

marks = {"Ali": 82, "Bob": 55, "Charlie": 91, "Diana": 47,
         "Eve": 73, "Frank": 68, "Grace": 95, "Heidi": 38}

avg = mean(list(marks.values()))
above_avg = {k: v for k, v in marks.items() if v > avg}

grades = {k: ("A" if v >= 80 else "B" if v >= 60 else "C") for k, v in marks.items()}

# ---- A4: Standard Deviation ----

def std_dev(data):
    return variance(data) ** 0.5

sample = [4, 8, 15, 16, 23, 42]
print("Custom std:", round(std_dev(sample), 4))
print("NumPy  std:", round(np.std(sample), 4))

# ---- A5: Two Groups ----

A = [12, 23, 3, 34, 45, 56, 5]
B = [12, 1, 3, 1, 1, 2, 3, 4, 5, 3, 4]

print(f"Mean A: {mean(A):.2f}, Variance A: {variance(A):.2f}")
print(f"Mean B: {mean(B):.2f}, Variance B: {variance(B):.2f}")
print(f"Difference in means: {mean(A) - mean(B):.2f}")

# ---- Output ----

print("\nAverage marks:", round(avg, 2))
print("Above average:", above_avg)
print("Grades:", grades)
