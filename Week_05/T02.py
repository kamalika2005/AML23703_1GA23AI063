from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

simulator = AerSimulator()

# Prepare |+> state
qc_plus = QuantumCircuit(1, 1)

qc_plus.h(0)       # |0> -> |+>
qc_plus.h(0)       # H before measurement: X-basis
qc_plus.measure(0, 0)

result_plus = simulator.run(qc_plus, shots=1000).result()
counts_plus = result_plus.get_counts()


# Prepare |-> state
qc_minus = QuantumCircuit(1, 1)

qc_minus.x(0)      # |0> -> |1>
qc_minus.h(0)      # |1> -> |->
qc_minus.h(0)      # H before measurement: X-basis
qc_minus.measure(0, 0)

result_minus = simulator.run(qc_minus, shots=1000).result()
counts_minus = result_minus.get_counts()


print("Measurement of |+> in X-basis:")
print(counts_plus)

print("\nMeasurement of |-> in X-basis:")
print(counts_minus)