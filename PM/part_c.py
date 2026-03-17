# Part C - Interview Ready

# Q1 Answer:
# PMF (Probability Mass Function) is for DISCRETE variables.
#   - Gives exact probability P(X = k) for each value k
#   - Example: probability of getting exactly 3 heads in 5 tosses
#   - All values sum to 1
#
# PDF (Probability Density Function) is for CONTINUOUS variables.
#   - Does NOT give exact probability at a point (that's always 0)
#   - Gives probability over an interval: P(a < X < b) = area under curve
#   - Example: probability that a person's height is between 170-175 cm
#   - Area under the full curve = 1

# Q2 - Compute probability from frequency data (relative frequency)

def probability_from_freq(data, event):
    count = sum(1 for x in data if x == event)
    return count / len(data)

outcomes = ["H", "T", "H", "H", "T", "H", "T", "H", "T", "T", "H"]
print("P(Heads):", probability_from_freq(outcomes, "H"))
print("P(Tails):", probability_from_freq(outcomes, "T"))

grades = ["A", "B", "A", "C", "B", "A", "B", "A", "C", "B"]
print("P(A):", probability_from_freq(grades, "A"))
print("P(B):", probability_from_freq(grades, "B"))

# Q3 Answer:
# Central Limit Theorem (CLT):
#   No matter what the original distribution looks like, if you take
#   many random samples and compute their means, those sample means
#   will form a NORMAL distribution as sample size grows (n >= 30).
#
# Why it matters in ML:
#   - Most statistical tests (t-test, z-test) assume normality.
#     CLT justifies using them even when original data isn't normal.
#   - Helps estimate confidence intervals and make predictions.
#   - Gradient-based optimisation in neural networks relies on
#     averaging many gradients - CLT makes this mathematically stable.
#   - Ensures that performance metrics (accuracy, loss) averaged over
#     batches behave predictably.
