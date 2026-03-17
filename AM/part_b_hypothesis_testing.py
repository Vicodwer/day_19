# Part B - Two Sample T-Test

import math
from scipy import stats

A = [12, 23, 3, 34, 45, 56, 5]
B = [12, 1, 3, 1, 1, 2, 3, 4, 5, 3, 4]

def sample_mean(data):
    return sum(data) / len(data)

def sample_variance(data):
    m = sample_mean(data)
    return sum((x - m)**2 for x in data) / (len(data) - 1)

def two_sample_t_test(s1, s2, alpha=0.05):
    n1, n2 = len(s1), len(s2)
    m1, m2 = sample_mean(s1), sample_mean(s2)
    v1, v2 = sample_variance(s1), sample_variance(s2)

    t = (m1 - m2) / math.sqrt(v1/n1 + v2/n2)
    df = (v1/n1 + v2/n2)**2 / ((v1/n1)**2/(n1-1) + (v2/n2)**2/(n2-1))
    p = 2 * stats.t.sf(abs(t), df)

    print(f"Mean A={m1:.2f}, Mean B={m2:.2f}")
    print(f"t = {t:.4f}, p = {p:.4f}, df = {df:.2f}")

    if p < alpha:
        print("Reject H0 - groups are significantly different")
    else:
        print("Fail to reject H0 - no significant difference")

two_sample_t_test(A, B)
