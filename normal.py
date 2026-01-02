import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

mu = float(input("Enter mean (μ): "))
sigma = float(input("Enter standard deviation (σ): "))
samples = int(input("Enter number of samples: "))

data = np.random.normal(mu, sigma, samples)

x = np.linspace(mu - 4*sigma, mu + 4*sigma, 200)

plt.hist(data, bins=50, density=True, alpha=0.6, label="Simulation")
plt.plot(x, norm.pdf(x, mu, sigma), label="Theoretical")
plt.title("Normal Distribution")
plt.xlabel("Value")
plt.ylabel("Probability Density")
plt.legend()
plt.show()

print("\nStatistics:")
print("Mean:", np.mean(data))
print("Variance:", np.var(data))
print("Standard Deviation:", np.std(data))