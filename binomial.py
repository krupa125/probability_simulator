import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

n = int(input("Enter number of trials (n): "))
p = float(input("Enter probability of success (p): "))
experiments = int(input("Enter number of experiments: "))

data = np.random.binomial(n, p, experiments)

x = range(0, n + 1)

plt.hist(data, bins=n + 1, density=True, alpha=0.6, label="Simulation")
plt.plot(x, binom.pmf(x, n, p), label="Theoretical")
plt.title("Binomial Distribution")
plt.xlabel("Number of Successes")
plt.ylabel("Probability")
plt.legend()
plt.show()

print("\nStatistics:")
print("Mean:", np.mean(data))
print("Variance:", np.var(data))
print("Standard Deviation:", np.std(data))