import math
import matplotlib.pyplot as plt

# String lengths
lengths = [2, 3, 4, 5, 6, 7, 8]

# Store query counts
classical_queries = []
simon_queries = []
speedup = []

for n in lengths:

    # Classical brute-force requires up to 2^(n-1) queries
    classical = 2 ** (n - 1)

    # Simon's algorithm needs approximately n-1 independent equations
    simon = n - 1

    classical_queries.append(classical)
    simon_queries.append(simon)

    speedup.append(classical / simon)

# Print results
print("Simon Algorithm vs Classical Brute Force")
print()

print("n\tClassical\tSimon\tSpeedup")

for i in range(len(lengths)):
    print(
        lengths[i],
        "\t",
        classical_queries[i],
        "\t\t",
        simon_queries[i],
        "\t",
        round(speedup[i], 2),
        "x"
    )

# Plot query comparison
plt.figure(figsize=(8, 5))

plt.plot(
    lengths,
    classical_queries,
    marker="o",
    label="Classical Brute Force"
)

plt.plot(
    lengths,
    simon_queries,
    marker="o",
    label="Simon's Algorithm"
)

plt.xlabel("String Length (n)")
plt.ylabel("Number of Oracle Queries")
plt.title("Simon Algorithm vs Classical Brute Force")
plt.legend()
plt.grid(True)

plt.show()

# Plot speedup
plt.figure(figsize=(8, 5))

plt.plot(
    lengths,
    speedup,
    marker="o"
)

plt.xlabel("String Length (n)")
plt.ylabel("Speedup")
plt.title("Speedup of Simon's Algorithm")

plt.grid(True)

plt.show()