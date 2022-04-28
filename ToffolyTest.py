# Copyright (C) 2022 Andrey Abramov
# Apache License 2.0

from FastQubit import *

print("Toffoly tests")
tof = Register('Toffoly', 3)

Toffoly(tof[0], tof[1], tof[2])
print("000 == " + tof.printZ())

tof.reset()
tof[0].X()
Toffoly(tof[0], tof[1], tof[2])
print("100 == " + tof.printZ())

tof.reset()
tof[1].X()
Toffoly(tof[0], tof[1], tof[2])
print("010 == " + tof.printZ())

tof.reset()
tof[0].X()
tof[1].X()
Toffoly(tof[0], tof[1], tof[2])
print("111 == " + tof.printZ())

tof.reset()
tof[2].X()
Toffoly(tof[0], tof[1], tof[2])
print("001 == " + tof.printZ())

tof.reset()
tof[0].X()
tof[2].X()
Toffoly(tof[0], tof[1], tof[2])
print("101 == " + tof.printZ())

tof.reset()
tof[1].X()
tof[2].X()
Toffoly(tof[0], tof[1], tof[2])
print("011 == " + tof.printZ())

tof.reset()
tof[0].X()
tof[1].X()
tof[2].X()
Toffoly(tof[0], tof[1], tof[2])
print("110 == " + tof.printZ())

print("After H gate for 0 and 1")

for i in range(20):
    tof.reset()
    tof[0].H()
    tof[1].H()
    start = tof.printZ()
    Toffoly(tof[0], tof[1], tof[2])
    stop = tof.printZ()
    print("start: " + start + " stop: " + stop)

print("After H gate for all")

for i in range(20):
    tof.reset()
    tof[0].H()
    tof[1].H()
    tof[2].H()
    start = tof.printZ()
    Toffoly(tof[0], tof[1], tof[2])
    stop = tof.printZ()
    print("start: " + start + " stop: " + stop)


print("Before and after H gate for all")

for i in range(20):
    tof.reset()
    tof[0].H()
    tof[1].H()
    tof[2].X()
    tof[2].H()
    start = tof.printZ()
    Toffoly(tof[0], tof[1], tof[2])
    tof[0].H()
    tof[1].H()
    tof[2].H()
    stop = tof.printZ()
    print("start: " + start + " stop: " + stop)