from qiskit.providers.basic_provider import BasicSimulator
from qiskit import transpile, QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit.circuit.library import UnitaryGate
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

cr = ClassicalRegister(4)
qr = QuantumRegister(4)
qc = QuantumCircuit(qr, cr)

U1_op = UnitaryGate(U1)
U1_controlled = U1_op.control(1)

U2_op = UnitaryGate(U1)
U2_controlled = U2_op.control(1, ctrl_state=0)

steps = 3
# qc.x(1)
# qc.x(2)
# qc.x(3)

for step in range(steps):
    qc.h(0)
    qc.append(U1_controlled, [0, 1, 2, 3])
    qc.append(U2_controlled, [0, 1, 2, 3])


qc.measure([0, 1, 2, 3], [3, 0, 1, 2])

qc.draw('mpl')
backend = BasicSimulator()
tqc = transpile(qc, backend)
counts = backend.run(tqc).result().get_counts()
print(counts)

plt.show()
