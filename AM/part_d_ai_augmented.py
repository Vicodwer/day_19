# Part D - AI Augmented Task

# Prompt used:
# "Explain descriptive statistics and hypothesis testing with a Python example using real-world data."

# AI Output Summary:
# - Descriptive stats summarise data: mean, median, std dev, min/max
# - Hypothesis testing uses H0, p-value and alpha to make decisions from data
# - Example used Iris dataset to compare sepal lengths of two species

# Code from AI output (tested and verified below):

import pandas as pd
import numpy as np
from scipy import stats
from sklearn.datasets import load_iris

iris = load_iris(as_frame=True)
df = iris.frame
df["species"] = df["target"].map({0: "setosa", 1: "versicolor", 2: "virginica"})

setosa = df[df.species == "setosa"]["sepal length (cm)"]
versicolor = df[df.species == "versicolor"]["sepal length (cm)"]

print("Setosa mean:", round(setosa.mean(), 2), "| std:", round(setosa.std(), 2))
print("Versicolor mean:", round(versicolor.mean(), 2), "| std:", round(versicolor.std(), 2))

t, p = stats.ttest_ind(setosa, versicolor)
print(f"\nt = {t:.4f}, p = {p:.2e}")
print("Reject H0 - significantly different" if p < 0.05 else "Fail to reject H0")

# Evaluation:
# - Explanation was clear and well-structured
# - Code runs without errors and gives correct output
# - Used real dataset (Iris) which made it practical
# - Minor gap: didn't show manual formulas, just used library functions
