# Copyright (C) 2022 Andrey Abramov
# Apache License 2.0

from FastQubit import *

reg = Register("reg", 2)

print("Statistical initialization test")
stat = [0,0,0,0]
for test in range(10000):
    phi = reg[0].getPhi()
    if phi>0 and phi < pi/2:
        stat[0] = stat[0] + 1
    if phi>pi/2 and phi < pi:
        stat[1] = stat[1] + 1
    if phi>pi and phi < 3*pi/2:
        stat[2] = stat[2] + 1
    if phi>3*pi/2 and phi < 2*pi:
        stat[3] = stat[3] + 1
    reg.reset()
print("States: {}, {}, {},{}", stat[0], stat[1], stat[2],stat[3])

print("First Bell State")
print("Z-measurement    X-measurement")
for i in range(10):
    reg[0].H()
    CNOT(reg[0], reg[1])
    print('{}{}               {}{}'.format(reg[0].measureZ(), reg[1].measureZ(), reg[0].measureX(), reg[1].measureX()))
    reg.reset()
    
print("Second Bell State")
print("Z-measurement    X-measurement")
for i in range(10):
    reg[0].X()
    reg[0].H()
    CNOT(reg[0], reg[1])
    print('{}{}               {}{}'.format(reg[0].measureZ(), reg[1].measureZ(), reg[0].measureX(), reg[1].measureX()))
    reg.reset()

print("Third Bell State")
print("Z-measurement    X-measurement")
for i in range(10):
    reg[0].H()
    reg[1].X()
    CNOT(reg[0], reg[1])
    print('{}{}               {}{}'.format(reg[0].measureZ(), reg[1].measureZ(), reg[0].measureX(), reg[1].measureX()))
    reg.reset()

print("Fourth Bell State")
print("Z-measurement    X-measurement")
for i in range(10):
    reg[0].H()
    reg[0].Z()
    reg[1].X()
    reg[1].Z()
    CNOT(reg[0], reg[1])
    print('{}{}               {}{}'.format(reg[0].measureZ(), reg[1].measureZ(), reg[0].measureX(), reg[1].measureX()))
    reg.reset()