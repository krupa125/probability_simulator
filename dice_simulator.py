import random
import matplotlib.pyplot as plt
import numpy as np

trials = int(input("Enter number of dice rolls: "))
rolls = []

for _ in range(trials):
    rolls.append(random.randint(1, 6))

plt.hist(rolls, bins=6)
plt.title("Dice Roll Simulation")
plt.xlabel("Dice Value")
plt.ylabel("Frequency")
plt.show()

print("\nStatistics:")
print("Mean:", np.mean(rolls))
print("Variance:", np.var(rolls))
print("Standard Deviation:", np.std(rolls))