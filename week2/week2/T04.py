from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
import numpy as np
import matplotlib.pyplot as plt

qc = QuantumCircuit(1)

qc.h(0)

error = np.random.uniform(-0.3, 0.3)

qc.p(error, 0)

state = Statevector.from_instruction(qc)

print("Random Phase:", error)
print(state)

plot_bloch_multivector(state)
plt.show()