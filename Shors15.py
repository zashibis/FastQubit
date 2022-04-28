# Copyright (C) 2022 Andrey Abramov
# Apache License 2.0

from FastQubit import *

print("Shor's algorithm for N=15, a=2")
print("Quantum part")

Q = Register('X', 8)
F = Register('F', 4)

print("Q-value         F-value      Q-phase        Q-QFT")

for step in range(20):
    Q.H()
    Q_start_bin = Q.printZ()
    Q_start_value = Q.measure()

    F[3].X()

    # Modular exponentiation
    for i in range(8):
        for j in range(2**i):
            Fredkin(Q[i], F[0], F[1])
            Fredkin(Q[i], F[1], F[2])
            Fredkin(Q[i], F[2], F[3])

            # for a = 7
            #Fredkin(Q[i], F[2], F[3])
            #Fredkin(Q[i], F[1], F[2])
            #Fredkin(Q[i], F[0], F[1])
            #CNOT(Q[i], F[0])
            #CNOT(Q[i], F[1])
            #CNOT(Q[i], F[2])
            #CNOT(Q[i], F[3])

    Q_mod_exp = Q.printX()

    # QFT
    Swap(Q[0], Q[7])
    Swap(Q[1], Q[6])
    Swap(Q[2], Q[5])
    Swap(Q[3], Q[4])

    for i in range(8):
        Q[i].H()



    print(Q_start_bin + " (" + str(Q_start_value) + ")  " + F.printZ() + " (" + str(F.measure("big")) + ")     " + Q_mod_exp)

    Q.reset()
    F.reset()










