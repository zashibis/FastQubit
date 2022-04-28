# Copyright (C) 2022 Andrey Abramov
# Apache License 2.0

from FastQubit import *

reg = Register("reg", 2)


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