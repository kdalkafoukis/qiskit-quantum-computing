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

U1 = Operator(U1)

U2 = np.array([[0, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 1, 0, 0, 0, 0],
               [0, 0, 0, 0, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 0, 0, 0, 1],
               [1, 0, 0, 0, 0, 0, 0, 0]], dtype=int)

U2 = Operator(U2)

cr = ClassicalRegister(4)
qr = QuantumRegister(4)
qc = QuantumCircuit(qr, cr)


qc.h(0)
# qc.x(1)
# qc.x(2)
# qc.x(3)

U1_op = U1.to_instruction()
U1_controlled = U1_op.control(1)
qc.append(U1_controlled, [0, 1, 2, 3])


U2_op = U2.to_instruction()
U2_controlled = U2_op.control(1, ctrl_state=0)
qc.append(U2_controlled, [0, 1, 2, 3])


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
