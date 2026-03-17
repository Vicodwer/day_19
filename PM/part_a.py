# Part A - Probability Distributions & Descriptive Statistics

import numpy as np
import matplotlib
matplotlib.use("Agg")  # remove this line if running locally with a display
import matplotlib.pyplot as plt
from scipy import stats

# ---- A1: Normal Distribution Dataset ----

data = np.random.normal(loc=0, scale=1, size=1000)

print("Mean    :", round(data.mean(), 4))
print("Variance:", round(data.var(), 4))
print("Std Dev :", round(data.std(), 4))

plt.hist(data, bins=30, color='steelblue', edgecolor='black')
plt.title("Normal Distribution (n=1000)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.savefig("a1_normal_hist.png")
plt.show()

# ---- A2: PMF for Binomial Distribution ----

from scipy.stats import binom

n, p = 10, 0.5
x = np.arange(0, n + 1)
pmf = binom.pmf(x, n, p)

print("\nBinomial PMF values:", pmf.round(4))
print("Sum of PMF:", round(pmf.sum(), 4))  # should be 1.0

plt.bar(x, pmf, color='coral', edgecolor='black')
plt.title("Binomial PMF (n=10, p=0.5)")
plt.xlabel("k")
plt.ylabel("P(X=k)")
plt.savefig("a2_binomial_pmf.png")
plt.show()

# ---- A3: Manual PDF of Normal Distribution ----

import math

def normal_pdf(x, mu=0, sigma=1):
    coeff = 1 / (sigma * math.sqrt(2 * math.pi))
    exponent = math.exp(-0.5 * ((x - mu) / sigma) ** 2)
    return coeff * exponent

x_vals = np.linspace(-4, 4, 100)
pdf_vals = [normal_pdf(x) for x in x_vals]

plt.plot(x_vals, pdf_vals, color='green')
plt.title("Normal PDF (manual)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.savefig("a3_normal_pdf.png")
plt.show()

# ---- A4: Mean, Median, Mode, Skewness ----

dataset = [2, 3, 3, 4, 5, 6, 6, 6, 7, 8, 9, 10, 15]

mean   = np.mean(dataset)
median = np.median(dataset)
mode   = stats.mode(dataset, keepdims=True).mode[0]
skew   = stats.skew(dataset)

print(f"\nMean   : {mean:.2f}")
print(f"Median : {median}")
print(f"Mode   : {mode}")
print(f"Skew   : {skew:.4f}")

if skew > 0:
    print("Right skewed - tail on the right, mean > median")
elif skew < 0:
    print("Left skewed - tail on the left, mean < median")
else:
    print("Symmetric distribution")

# ---- A5: Coin Toss Simulation ----

tosses = np.random.choice(["H", "T"], size=1000)
heads = np.sum(tosses == "H")

print(f"\nHeads count    : {heads}")
print(f"Estimated P(H) : {heads/1000:.4f}")
print(f"Theoretical P  : 0.5000")
