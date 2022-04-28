# Copyright (C) 2022 Andrey Abramov
# Apache License 2.0

from FastQubit import *

print("Fredkin tests")
fr = Register('Fredkin', 3)

Fredkin(fr[0], fr[1], fr[2])
print("000 == " + fr.printZ())

fr.reset()
fr[0].X()
Fredkin(fr[0], fr[1], fr[2])
print("100 == " + fr.printZ())

fr.reset()
fr[1].X()
Fredkin(fr[0], fr[1], fr[2])
print("010 == " + fr.printZ())

fr.reset()
fr[2].X()
Fredkin(fr[0], fr[1], fr[2])
print("001 == " + fr.printZ())

fr.reset()
fr[0].X()
fr[2].X()
Fredkin(fr[0], fr[1], fr[2])
print("110 == " + fr.printZ())

fr.reset()
fr[0].X()
fr[1].X()
Fredkin(fr[0], fr[1], fr[2])
print("101 == " + fr.printZ())

fr.reset()
fr[0].X()
fr[1].X()
fr[2].X()
Fredkin(fr[0], fr[1], fr[2])
print("111 == " + fr.printZ())

fr.reset()
fr[1].X()
fr[2].X()
Fredkin(fr[0], fr[1], fr[2])
print("011 == " + fr.printZ())

print("After H gate for 0 and 1")

for i in range(20):
    fr.reset()
    fr[0].H()
    fr[1].H()
    start = fr.printZ()
    Fredkin(fr[0], fr[1], fr[2])
    stop = fr.printZ()
    print("start: " + start + " stop: " + stop)

print("After H gate for all")

for i in range(20):
    fr.reset()
    fr[0].H()
    fr[1].H()
    fr[2].H()
    start = fr.printZ()
    Fredkin(fr[0], fr[1], fr[2])
    stop = fr.printZ()
    print("start: " + start + " stop: " + stop)

print("Multiple run test 1")
for test in range(20):
    fr.reset()
    fr.H()
    start = fr.printZ()
    for i in range(200):
        Fredkin(fr[0], fr[1], fr[2])
    stop = fr.printZ()
    print("start: " + start + " stop: " + stop)

print("Multiple run test 2")
for test in range(20):
    fr.reset()
    fr.H()
    start = fr.printZ()
    for i in range(199):
        Fredkin(fr[0], fr[1], fr[2])
    stop = fr.printZ()
    print("start: " + start + " stop: " + stop)






