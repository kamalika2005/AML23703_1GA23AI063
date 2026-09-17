import matplotlib.pyplot as plt

# Input sizes
n_values = list(range(2, 11))

# Classical worst-case query complexity
classical_queries = [
    2 ** (n - 1) + 1
    for n in n_values
]

# Deutsch-Jozsa always uses one query
quantum_queries = [
    1
    for n in n_values
]

# Print results
print("Deutsch-Jozsa Query Complexity")
print()

print("n\tClassical\tQuantum")

for i in range(len(n_values)):
    print(
        n_values[i],
        "\t",
        classical_queries[i],
        "\t\t",
        quantum_queries[i]
    )

# Plot
plt.figure(figsize=(8, 5))

plt.plot(
    n_values,
    classical_queries,
    marker="o",
    label="Classical Worst Case"
)

plt.plot(
    n_values,
    quantum_queries,
    marker="o",
    label="Deutsch-Jozsa"
)

plt.xlabel("Number of Input Qubits (n)")
plt.ylabel("Number of Oracle Queries")

plt.title(
    "Deutsch-Jozsa: Classical vs Quantum Query Complexity"
)

plt.legend()
plt.grid(True)

plt.show()