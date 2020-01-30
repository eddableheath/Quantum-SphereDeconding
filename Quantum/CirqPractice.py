# Cirq practices
# Author: Edmund Dable-Heath
# Getting to grips with the quantum computing python package cirq

import cirq


#circuit = cirq.Circuit()
#(q0, q1) = cirq.LineQubit.range(2)

#circuit.append([cirq.H(q0), cirq.CNOT(q0, q1)])
#circuit.append([cirq.measure(q0), cirq.measure(q1)])

#sim = cirq.Simulator()
#results = sim.run(circuit, repetitions=10)

#print(cirq.google.Sycamore23)


device = cirq.google.Bristlecone

circuit = cirq.Circuit(device=device)
a0, a1 = cirq.GridQubit(5, 5), cirq.GridQubit(5, 6)
b0, b1 = cirq.GridQubit(6, 5), cirq.GridQubit(6, 6)
circuit.append([cirq.CZ(a0 ,a1), cirq.CZ(b0, b1)])

print(circuit)