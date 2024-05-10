'''
Same as random-walks-on-the-line.py
But we try to replace U1, U2 with quantum gates instead of matrices
'''
from qiskit.providers.basic_provider import BasicSimulator
from qiskit.circuit.library.standard_gates import XGate
from qiskit import transpile, QuantumRegister, ClassicalRegister, QuantumCircuit
import matplotlib.pyplot as plt


def initialize_state(qc, digits):
    for i, digit in enumerate(reversed(digits)):
        if digit == '1':
            qc.x(i + 1)


def transition_state(digits, ctrl_state=None):
    qr = QuantumRegister(len(digits))
    qc = QuantumCircuit(qr)

    for target_qubit in range(len(digits) - 1, 0, -1):
        qargs = [control_qubit for control_qubit in range(target_qubit)]
        qargs.append(target_qubit)
        cx_gate = XGate().control(target_qubit, ctrl_state=ctrl_state)
        qc.append(cx_gate, qargs)
    qc.x(0)

    qc.to_gate()
    return qc


def random_walk_on_the_line(steps=1):
    num = "000"

    num_of_qubits = len(num) + 1
    qubits = list(range(num_of_qubits))
    cbit = list(range(num_of_qubits - 1))
    cbit.insert(0, num_of_qubits - 1)

    cr = ClassicalRegister(num_of_qubits)
    qr = QuantumRegister(num_of_qubits)
    qc = QuantumCircuit(qr, cr)

    Uplus_op = transition_state(num)
    Uplus_controlled = Uplus_op.control(1)

    Uminus_op = transition_state(num, ctrl_state=0)
    Uminus_controlled = Uminus_op.control(1, ctrl_state=0)

    steps = 1
    initialize_state(qc, num)

    for _ in range(steps):
        qc.h(0)
        qc.append(Uplus_controlled, qubits)
        qc.append(Uminus_controlled, qubits)

    qc.decompose().draw('mpl')

    qc.measure(qubits, cbit)

    backend = BasicSimulator()
    tqc = transpile(qc, backend)
    counts = backend.run(tqc).result().get_counts()
    return counts

print(random_walk_on_the_line())


plt.show()
