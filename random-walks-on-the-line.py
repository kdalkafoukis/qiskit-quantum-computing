from qiskit.providers.basic_provider import BasicSimulator
from qiskit import transpile, QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit.circuit.library import UnitaryGate
import matplotlib.pyplot as plt
import numpy as np

digits = "000"
size = 2 ** len(digits)


U1 = np.zeros((size, size), dtype=int)
U1[0][size - 1] = 1
U1[np.eye(size, k=-1, dtype='bool')] = 1

U2 = np.zeros((size, size), dtype=int)
U2[size - 1][0] = 1
U2[np.eye(size, k=1, dtype='bool')] = 1

num_of_qubits = len(digits) + 1
cr = ClassicalRegister(num_of_qubits)
qr = QuantumRegister(num_of_qubits)
qc = QuantumCircuit(qr, cr)

U1_op = UnitaryGate(U1)
U1_controlled = U1_op.control(1)

U2_op = UnitaryGate(U2)
U2_controlled = U2_op.control(1, ctrl_state=0)

for i, digit in enumerate(reversed(digits)):
    if digit == '1':
        qc.x(i + 1)

qubits = list(range(num_of_qubits))

steps = 1
for step in range(steps):
    qc.h(0)
    qc.append(U1_controlled, qubits)
    qc.append(U2_controlled, qubits)

cbit = list(range(num_of_qubits - 1))
cbit.insert(0, num_of_qubits - 1)

qc.measure(qubits, cbit)

qc.draw('mpl')
backend = BasicSimulator()
tqc = transpile(qc, backend)
counts = backend.run(tqc).result().get_counts()
print(counts)

plt.show()
