# Part B - Simulate and Compare Distributions

import numpy as np
import matplotlib
matplotlib.use("Agg")  # remove this line if running locally with a display
import matplotlib.pyplot as plt

# Generate samples
normal  = np.random.normal(loc=0, scale=1, size=1000)
uniform = np.random.uniform(low=-3, high=3, size=1000)

# Compare stats
print("--- Normal Distribution ---")
print(f"Mean   : {normal.mean():.4f}")
print(f"Std Dev: {normal.std():.4f}")
print(f"Min/Max: {normal.min():.2f} / {normal.max():.2f}")

print("\n--- Uniform Distribution ---")
print(f"Mean   : {uniform.mean():.4f}")
print(f"Std Dev: {uniform.std():.4f}")
print(f"Min/Max: {uniform.min():.2f} / {uniform.max():.2f}")

# Plot both side by side
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

axes[0].hist(normal, bins=30, color='steelblue', edgecolor='black')
axes[0].set_title("Normal Distribution")
axes[0].set_xlabel("Value")

axes[1].hist(uniform, bins=30, color='coral', edgecolor='black')
axes[1].set_title("Uniform Distribution")
axes[1].set_xlabel("Value")

plt.tight_layout()
plt.savefig("b_distribution_comparison.png")
plt.show()

# Comparison notes (as comments):
# Shape   : Normal is bell-shaped, peaks at mean. Uniform is flat/rectangular.
# Spread  : Both cover similar range here, but normal has tails beyond 3 std devs.
# Central : Both have mean ~ 0, but normal has stronger pull toward center.

# When to use each:
# Normal   - heights, weights, test scores, measurement errors, anything that
#            results from many small random effects (Central Limit Theorem)
# Uniform  - random number generation, sampling, simulating dice rolls or
#            any scenario where all outcomes are equally likely
