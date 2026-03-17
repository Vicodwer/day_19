# Part C - Interview Questions

# Q1 Answer (written):
# - Loops: use when you need index, complex logic, or early exit
# - List comprehension: best for simple transform/filter into a new list (concise)
# - HOFs (map/filter/reduce): use for functional pipelines and reusability
# Rule: loop = control, list comp = quick transform, HOF = composable functions

# Q2 - Flatten nested list and remove even numbers

nested = [[1, 2, 3], [4, 5], [6, [7, 8, 9]]]

def flatten(lst):
    return [x for sub in lst for x in (flatten(sub) if isinstance(sub, list) else [sub])]

flat = flatten(nested)
odds = [x for x in flat if x % 2 != 0]

print("Flattened:", flat)
print("Odd only :", odds)

# Q3 Answer (written):
# Hypothesis testing checks if an observed result is statistically significant.
#
# H0 (Null): Default assumption - "no difference" e.g. mean score = 70
# H1 (Alt) : What we want to prove - "there IS a difference"
# p-value  : Probability of getting this result if H0 were true
# alpha    : Threshold (usually 0.05). If p < alpha, reject H0
#
# Example: A class average is claimed to be 70.
# Sample gives mean=65, t-test gives p=0.03.
# 0.03 < 0.05 → Reject H0 → Mean is significantly different from 70.
