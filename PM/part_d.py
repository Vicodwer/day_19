# Part D - AI Augmented Task

# Prompt used:
# "Explain probability distributions (normal, uniform, binomial) with Python visualizations."

# AI Output Summary:
# - Normal: bell curve, defined by mean and std dev, used for natural phenomena
# - Uniform: flat distribution, all values equally likely between a and b
# - Binomial: discrete, models number of successes in n trials with prob p
# - AI provided code using numpy + matplotlib to visualise all three

# Code based on AI output (tested and verified):

import numpy as np
import matplotlib
matplotlib.use("Agg")  # remove this line if running locally with a display
import matplotlib.pyplot as plt
from scipy.stats import binom

fig, axes = plt.subplots(1, 3, figsize=(14, 4))

# Normal
normal = np.random.normal(0, 1, 1000)
axes[0].hist(normal, bins=30, color='steelblue', edgecolor='black', density=True)
axes[0].set_title("Normal Distribution\nμ=0, σ=1")
axes[0].set_xlabel("Value")

# Uniform
uniform = np.random.uniform(-3, 3, 1000)
axes[1].hist(uniform, bins=30, color='coral', edgecolor='black', density=True)
axes[1].set_title("Uniform Distribution\nlow=-3, high=3")
axes[1].set_xlabel("Value")

# Binomial
k = np.arange(0, 21)
pmf = binom.pmf(k, n=20, p=0.5)
axes[2].bar(k, pmf, color='mediumseagreen', edgecolor='black')
axes[2].set_title("Binomial Distribution\nn=20, p=0.5")
axes[2].set_xlabel("k (successes)")

plt.tight_layout()
plt.savefig("d_distributions.png")
plt.show()

# Evaluation:
# - Explanations were accurate and easy to follow
# - Visualisations clearly showed the shape difference between all 3
# - Code was clean, ran without errors
# - One gap: AI didn't explain when NOT to use each distribution,
#   which is equally important in practice
