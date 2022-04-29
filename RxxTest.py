# Copyright (C) 2022 Andrey Abramov
# Apache License 2.0

from FastQubit import *

Q = Register('Rxx', 2)

print("TEST 1: 0 - H")
Q[0].H()
print("Start: " + Q.printZ() + " " + Q.printX() + " Q0 ampl=" + str(Q[0].getTheta()) + " phase=" + str(Q[0].getPhi()) + " Q1 ampl=" + str(Q[1].getTheta()) + " phase=" + str(Q[1].getPhi()))
RXX_pi(Q[0], Q[1], 8)
print("End: " + Q.printZ() + " " + Q.printX() + " Q0 ampl=" + str(Q[0].getTheta()) + " phase=" + str(Q[0].getPhi()) + " Q1 ampl=" + str(Q[1].getTheta()) + " phase=" + str(Q[1].getPhi()))
#Q.show()
Q.reset()

print("TEST 2: 1 - H")
Q[1].H()
print("Start: " + Q.printZ() + " " + Q.printX() + " Q0 ampl=" + str(Q[0].getTheta()) + " phase=" + str(Q[0].getPhi()) + " Q1 ampl=" + str(Q[1].getTheta()) + " phase=" + str(Q[1].getPhi()))
RXX_pi(Q[0], Q[1], 8)
print("End: " + Q.printZ() + " " + Q.printX() + " Q0 ampl=" + str(Q[0].getTheta()) + " phase=" + str(Q[0].getPhi()) + " Q1 ampl=" + str(Q[1].getTheta()) + " phase=" + str(Q[1].getPhi()))
#Q.show()
Q.reset()

print("TEST 3: 0 - XH")
Q[0].X()
Q[0].H()
print("Start: " + Q.printZ() + " " + Q.printX() + " Q0 ampl=" + str(Q[0].getTheta()) + " phase=" + str(Q[0].getPhi()) + " Q1 ampl=" + str(Q[1].getTheta()) + " phase=" + str(Q[1].getPhi()))
RXX_pi(Q[0], Q[1], 8)
print("End: " + Q.printZ() + " " + Q.printX() + " Q0 ampl=" + str(Q[0].getTheta()) + " phase=" + str(Q[0].getPhi()) + " Q1 ampl=" + str(Q[1].getTheta()) + " phase=" + str(Q[1].getPhi()))
#Q.show()
Q.reset()

print("TEST 4: 1 - XH")
Q[1].X()
Q[1].H()
print("Start: " + Q.printZ() + " " + Q.printX() + " Q0 ampl=" + str(Q[0].getTheta()) + " phase=" + str(Q[0].getPhi()) + " Q1 ampl=" + str(Q[1].getTheta()) + " phase=" + str(Q[1].getPhi()))
RXX_pi(Q[0], Q[1], 8)
print("End: " + Q.printZ() + " " + Q.printX() + " Q0 ampl=" + str(Q[0].getTheta()) + " phase=" + str(Q[0].getPhi()) + " Q1 ampl=" + str(Q[1].getTheta()) + " phase=" + str(Q[1].getPhi()))
#Q.show()
Q.reset()

print("TEST 5: HH")
Q[0].H()
Q[1].H()
print("Start: " + Q.printZ() + " " + Q.printX() + " Q0 ampl=" + str(Q[0].getTheta()) + " phase=" + str(Q[0].getPhi()) + " Q1 ampl=" + str(Q[1].getTheta()) + " phase=" + str(Q[1].getPhi()))
RXX_pi(Q[0], Q[1], 8)
print("End: " + Q.printZ() + " " + Q.printX() + " Q0 ampl=" + str(Q[0].getTheta()) + " phase=" + str(Q[0].getPhi()) + " Q1 ampl=" + str(Q[1].getTheta()) + " phase=" + str(Q[1].getPhi()))
#Q.show()
Q.reset()

print("TEST 6: XH XH")
Q[0].X()
Q[0].H()
Q[1].X()
Q[1].H()
print("Start: " + Q.printZ() + " " + Q.printX() + " Q0 ampl=" + str(Q[0].getTheta()) + " phase=" + str(Q[0].getPhi()) + " Q1 ampl=" + str(Q[1].getTheta()) + " phase=" + str(Q[1].getPhi()))
RXX_pi(Q[0], Q[1], 8)
print("End: " + Q.printZ() + " " + Q.printX() + " Q0 ampl=" + str(Q[0].getTheta()) + " phase=" + str(Q[0].getPhi()) + " Q1 ampl=" + str(Q[1].getTheta()) + " phase=" + str(Q[1].getPhi()))
#Q.show()
Q.reset()

print("TEST 7: H XH")
Q[0].H()
Q[1].X()
Q[1].H()
print("Start: " + Q.printZ() + " " + Q.printX() + " Q0 ampl=" + str(Q[0].getTheta()) + " phase=" + str(Q[0].getPhi()) + " Q1 ampl=" + str(Q[1].getTheta()) + " phase=" + str(Q[1].getPhi()))
RXX_pi(Q[0], Q[1], 8)
print("End: " + Q.printZ() + " " + Q.printX() + " Q0 ampl=" + str(Q[0].getTheta()) + " phase=" + str(Q[0].getPhi()) + " Q1 ampl=" + str(Q[1].getTheta()) + " phase=" + str(Q[1].getPhi()))
#Q.show()
Q.reset()

print("TEST 8: XH H")
Q[0].X()
Q[0].H()
Q[1].H()
print("Start: " + Q.printZ() + " " + Q.printX() + " Q0 ampl=" + str(Q[0].getTheta()) + " phase=" + str(Q[0].getPhi()) + " Q1 ampl=" + str(Q[1].getTheta()) + " phase=" + str(Q[1].getPhi()))
RXX_pi(Q[0], Q[1], 8)
print("End: " + Q.printZ() + " " + Q.printX() + " Q0 ampl=" + str(Q[0].getTheta()) + " phase=" + str(Q[0].getPhi()) + " Q1 ampl=" + str(Q[1].getTheta()) + " phase=" + str(Q[1].getPhi()))
#Q.show()
Q.reset()

print("TEST 9: Ypi/8 Y-pi/8")
Q[0].rotateY_pi(8)
Q[1].rotateY_pi(-8)
print("Start: " + Q.printZ() + " " + Q.printX() + " Q0 ampl=" + str(Q[0].getTheta()) + " phase=" + str(Q[0].getPhi()) + " Q1 ampl=" + str(Q[1].getTheta()) + " phase=" + str(Q[1].getPhi()))
RXX_pi(Q[0], Q[1], 2)
print("End: " + Q.printZ() + " " + Q.printX() + " Q0 ampl=" + str(Q[0].getTheta()) + " phase=" + str(Q[0].getPhi()) + " Q1 ampl=" + str(Q[1].getTheta()) + " phase=" + str(Q[1].getPhi()))
Q.show()
Q.reset()






