# Copyright (C) 2022 Andrey Abramov
# Apache License 2.0

from FastQubit import *

Q = Register('CNOT', 2)

print("TEST 1: Amplitude tests")
CNOT(Q[0], Q[1])
print("00 = " + Q.printZ())

Q.reset()
Q[0].X()
CNOT(Q[0], Q[1])
print("11 = " + Q.printZ())

Q.reset()
Q[1].X()
CNOT(Q[0], Q[1])
print("01 = " + Q.printZ())

Q.reset()
Q[0].X()
Q[1].X()
CNOT(Q[0], Q[1])
print("10 = " + Q.printZ())

print("TEST 2: Amplitude with double CNOT")
Q.reset()
CNOT(Q[0], Q[1])
CNOT(Q[0], Q[1])
print("00 = " + Q.printZ())

Q.reset()
Q[0].X()
CNOT(Q[0], Q[1])
CNOT(Q[0], Q[1])
print("10 = " + Q.printZ())

Q.reset()
Q[1].X()
CNOT(Q[0], Q[1])
CNOT(Q[0], Q[1])
print("01 = " + Q.printZ())

Q.reset()
Q[0].X()
Q[1].X()
CNOT(Q[0], Q[1])
CNOT(Q[0], Q[1])
print("11 = " + Q.printZ())

print("Phase tests")
print("TEST 3: Both after H")
for test in range(5):
    Q.reset()
    Q[0].H()
    Q[1].H()
    start_phase = Q.printX()
    start_ampl = Q.printZ()
    CNOT(Q[0], Q[1])
    print("Start phase: " + start_phase + " Start ampl: " + start_ampl + " End phase: " + Q.printX() + " End ampl: " + Q.printZ())

print("TEST 4: Q0 = H, Q1 = XH")
for test in range(5):
    Q.reset()
    Q[0].H()
    Q[1].X()
    Q[1].H()
    start_phase = Q.printX()
    start_ampl = Q.printZ()
    CNOT(Q[0], Q[1])
    print("Start phase: " + start_phase + " Start ampl: " + start_ampl + " End phase: " + Q.printX() + " End ampl: " + Q.printZ())

print("TEST 5: Q0 = XH, Q1 = H")
for test in range(5):
    Q.reset()
    Q[0].X()
    Q[0].H()
    Q[1].H()
    start_phase = Q.printX()
    start_ampl = Q.printZ()
    CNOT(Q[0], Q[1])
    print("Start phase: " + start_phase + " Start ampl: " + start_ampl + " End phase: " + Q.printX() + " End ampl: " + Q.printZ())

print("TEST 6: Q0 = XH, Q1 = XH")
for test in range(5):
    Q.reset()
    Q[0].X()
    Q[0].H()
    Q[1].X()
    Q[1].H()
    start_phase = Q.printX()
    start_ampl = Q.printZ()
    CNOT(Q[0], Q[1])
    print("Start phase: " + start_phase + " Start ampl: " + start_ampl + " End phase: " + Q.printX() + " End ampl: " + Q.printZ())

print("TEST 7: CP(pi/4)")
Q.reset()
Q[0].H()
Q[1].X()
Q[0].P_pi(8)
Q[1].P_pi(8)
CNOT(Q[0], Q[1])
Q[1].P_pi(-8)
CNOT(Q[0], Q[1])
Q.show()


print("TEST 8: Q0 = H, Q1 = H+P(pi/8)")
for test in range(5):
    Q.reset()
    Q[0].H()
    Q[1].H()
    Q[1].P_pi(8)
    print("Start: ampl=" + Q.printZ() + " Q0phase=" + str(Q[0].getPhi()) + " Q1phase=" + str(Q[1].getPhi()))
    CNOT(Q[0], Q[1])
    print("End: ampl=" + Q.printZ() + " Q0phase=" + str(Q[0].getPhi()) + " Q1phase=" + str(Q[1].getPhi()))
