from qiskit.providers.basic_provider import BasicSimulator
from qiskit import transpile, QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit.quantum_info.operators import Operator
import matplotlib.pyplot as plt
import numpy as np

U1 = np.array([[0, 0, 0, 0, 0, 0, 0, 1],
               [1, 0, 0, 0, 0, 0, 0, 0],
               [0, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 1, 0]], dtype=int)

U2 = np.array([[0, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 0, 0, 0, 1],
               [1, 0, 0, 0, 0, 0, 0, 0]], dtype=int)


U1 = Operator(U1)
U2 = Operator(U1)

qr = QuantumRegister(3)
cr = ClassicalRegister(3)
qc = QuantumCircuit(qr, cr)

# qc.x(0)
# qc.x(1)
# qc.x(2)

qc.append(U1, [0, 1, 2])
# qc.append(U2, [0, 1, 2])

qc.measure([0, 1, 2], [0, 1, 2])

# qc.draw('mpl')

backend = BasicSimulator()
tqc = transpile(qc, backend)
counts = backend.run(tqc).result().get_counts()
print(counts)

plt.show()
