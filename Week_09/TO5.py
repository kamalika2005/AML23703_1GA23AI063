from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator

simulator = AerSimulator()

# ==========================================
# GHZ STATE
# (|000> + |111>) / sqrt(2)
# ==========================================

ghz = QuantumCircuit(3, 3)

ghz.h(0)
ghz.cx(0, 1)
ghz.cx(1, 2)

ghz.measure([0, 1, 2], [0, 1, 2])

result_ghz = simulator.run(
    ghz,
    shots=1024
).result()

ghz_counts = result_ghz.get_counts()

print("GHZ STATE")
print("=========")
print(ghz_counts)


# ==========================================
# W STATE
# (|001> + |010> + |100>) / sqrt(3)
# ==========================================

w_state = Statevector([
    0,
    1 / (3 ** 0.5),
    1 / (3 ** 0.5),
    0,
    1 / (3 ** 0.5),
    0,
    0,
    0
])

w = QuantumCircuit(3, 3)

w.initialize(w_state.data, [0, 1, 2])

w.measure([0, 1, 2], [0, 1, 2])

result_w = simulator.run(
    w,
    shots=1024
).result()

w_counts = result_w.get_counts()

print("\nW STATE")
print("=======")
print(w_counts)
