from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
import numpy as np
import matplotlib.pyplot as plt

theta = np.pi / 4
phi = np.pi / 6

qc = QuantumCircuit(1)

qc.ry(theta, 0)
qc.rz(phi, 0)

state = Statevector.from_instruction(qc)

manual = [
    np.cos(theta / 2),
    np.exp(1j * phi) * np.sin(theta / 2)
]

print("Qiskit State:")
print(state)

print("\nManual State:")
print(manual)

plot_bloch_multivector(state)
plt.show()