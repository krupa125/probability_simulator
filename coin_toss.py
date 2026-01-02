import random
import matplotlib.pyplot as plt
import numpy as np

trials = int(input("Enter number of coin tosses: "))
results = []

for _ in range(trials):
    results.append(random.choice(['Heads', 'Tails']))

heads = results.count('Heads')
tails = results.count('Tails')

plt.bar(['Heads', 'Tails'], [heads, tails])
plt.title("Coin Toss Simulation")
plt.ylabel("Frequency")
plt.show()

values = [1 if x == 'Heads' else 0 for x in results]

print("\nStatistics:")
print("Mean:", np.mean(values))
print("Variance:", np.var(values))
print("Standard Deviation:", np.std(values))