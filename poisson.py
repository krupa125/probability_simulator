import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

lam = float(input("Enter average rate (lambda): "))
experiments = int(input("Enter number of experiments: "))

data = np.random.poisson(lam, experiments)

x = range(0, max(data) + 1)

plt.hist(data, bins=20, density=True, alpha=0.6, label="Simulation")
plt.plot(x, poisson.pmf(x, lam), label="Theoretical")
plt.title("Poisson Distribution")
plt.xlabel("Number of Events")
plt.ylabel("Probability")
plt.legend()
plt.show()

print("\nStatistics:")
print("Mean:", np.mean(data))
print("Variance:", np.var(data))
print("Standard Deviation:", np.std(data))