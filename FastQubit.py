# Copyright (C) 2022 Andrey Abramov
# Apache License 2.0

import numpy as np
from numpy import pi
import math
from qiskit.visualization import plot_bloch_vector, plot_bloch_multivector
import matplotlib.pyplot as plt
import random

def rotation_matrix(axis, angle):
    axis = np.asarray(axis)
    axis = axis / math.sqrt(np.dot(axis, axis))
    a = math.cos(angle / 2.0)
    b, c, d = -axis * math.sin(angle / 2.0)
    aa, bb, cc, dd = a * a, b * b, c * c, d * d
    bc, ad, ac, ab, bd, cd = b * c, a * d, a * c, a * b, b * d, c * d
    
    return np.array([[aa + bb - cc - dd, 2 * (bc + ad), 2 * (bd - ac)], [2 * (bc - ad), aa + cc - bb - dd, 2 * (cd + ab)], [2 * (bd + ac), 2 * (cd - ab), aa + dd - bb - cc]])

X_rotation_matrix = []
Xdg_rotation_matrix = []
for power in range(11):
    X_rotation_matrix.append(rotation_matrix([1, 0, 0], pi/(2**power)))
    Xdg_rotation_matrix.append(rotation_matrix([1, 0, 0], -pi/(2**power)))

Y_rotation_matrix = []
Ydg_rotation_matrix = []
for power in range(11):
    Y_rotation_matrix.append(rotation_matrix([0, 1, 0], pi/(2**power)))
    Ydg_rotation_matrix.append(rotation_matrix([0, 1, 0], -pi/(2**power)))

Z_rotation_matrix = []
Zdg_rotation_matrix = []
for power in range(11):
    Z_rotation_matrix.append(rotation_matrix([0, 0, 1], pi/(2**power)))
    Zdg_rotation_matrix.append(rotation_matrix([0, 0, 1], -pi/(2**power)))

class Qubit:
    name = ''
    
    state = [0, 0, 1]
    defect = 0

    def __init__(self, name, defect=0.000000001):
        self.name = name
        self.defect = defect;
        if(random.randint(0,1) == 0):
            self.rotateY(defect)
        else:
            self.rotateY(-defect)

    def show(self):
        plot_bloch_vector(self.state, title=self.name, figsize=(5,6), coord_type='Cartesian')
        plt.show()

    def reset(self):
        self.state = [0, 0, 1]
        if(random.randint(0,1) == 0):
            self.rotateY(self.defect)
        else:
            self.rotateY(-self.defect)

    def measureX(self):
        if (self.state[0] > 0):
            return "+"
            #return 0
        elif (self.state[0] < 0):
            return "-"
            #return 1
        else:
            raise Exception('Unknown value')
        
    def measureY(self):
        if (self.state[1] > 0):
            return 0
        elif (self.state[1] < 0):
            return 1
        else:
            raise Exception('Unknown value')

    def measureZ(self):
        if (self.state[2] > 0):
            return 0
        elif (self.state[2] < 0):
            return 1
        else:
            raise Exception('Unknown value')

    def getTheta(self):
        #TODO not like in Bloch Sphere
        return np.arctan2(self.state[2], np.hypot(self.state[0], self.state[1]))

    def getPhi(self):
        return np.arctan2(self.state[1], self.state[0])


###########################################################
# Base rotations

    def rotateX(self, angle):
        self.state = np.dot(rotation_matrix([1, 0, 0], angle), self.state)

    def rotateY(self, angle):
        self.state = np.dot(rotation_matrix([0, 1, 0], angle), self.state)

    def rotateZ(self, angle):
        self.state = np.dot(rotation_matrix([0, 0, 1], angle), self.state)

###########################################################
# Single Qubit Gates

    def X(self):
        self.state = np.dot(X_rotation_matrix[0], self.state)
        #self.rotateX(pi)

    def Y(self):
        self.state = np.dot(Y_rotation_matrix[0], self.state)
        #self.rotateY(pi)

    def Z(self):
        self.state = np.dot(Z_rotation_matrix[0], self.state)
        #self.rotateZ(pi)

    def H(self):
        self.state = np.dot(Y_rotation_matrix[1], self.state)
        self.X()

    def P_pi(self, divider):
        if divider > 0:
            self.state = np.dot(Z_rotation_matrix[int(math.log2(divider))], self.state)
        else:
            self.state = np.dot(Zdg_rotation_matrix[int(math.log2(-divider))], self.state)

    def T(self):
        self.state = np.dot(Z_rotation_matrix[2], self.state)
        #self.rotateZ(pi/4)

    def Tdg(self):
        self.state = np.dot(Zdg_rotation_matrix[2], self.state)
        #self.rotateZ(-pi/4)

class Register:
    
    name = ''
    size = 0
    qubits = []

    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.qubits = [ Qubit(name+str(i)) for i in range(size) ]

    def __getitem__(self, index):
        return self.qubits[index]

    def measure(self, endianness="little"):
        out = 0

        if endianness=="big":
            i = self.size - 1
            for q in self.qubits:
                out = out + q.measureZ()*(2**i)
                i = i - 1
            return out
        else:
            i = 0
            for q in self.qubits:
                out = out + q.measureZ()*(2**i)
                i = i + 1
            return out

    def show(self, start=0, stop=None):
        if stop is None:
            stop = self.size - 1
        
        width, height = plt.figaspect(1 / self.size)
        fig = plt.figure(figsize=(width, height))
            
        for i in range(start, stop+1):
            ax = fig.add_subplot(1, self.size, i + 1, projection="3d")
            plot_bloch_vector(self.qubits[i].state, title=self.qubits[i].name, ax=ax, coord_type='Cartesian')
        
        plt.show()

    def H(self):
        for q in self.qubits:
            q.H()

    def reset(self):
        for q in self.qubits:
            q.reset()

    def printX(self):
        out_string = ""
        for q in self.qubits:
            out_string = out_string + q.measureX()
        return out_string

    def printZ(self):
        out_string = ""
        for q in self.qubits:
            out_string = out_string + str(q.measureZ())
        return out_string


###########################################################
# Multi-Qubit Gates

def CNOT(control, controlled):
# TODO: CNOT should consists of rotations only
    controlled_phase = controlled.measureX()

    if(control.measureZ() > 0):
        controlled.X()
    if (controlled_phase == "-"):
        control.Z()

def CP_pi(control, controlled, pi_divider):
    control.P_pi(pi_divider*2)
    controlled.P_pi(pi_divider*2)
    CNOT(control, controlled)
    controlled.P_pi(-pi_divider*2)
    CNOT(control, controlled)
    


def Swap(a, b):
    CNOT(a, b)
    CNOT(b, a)
    CNOT(a, b)

# CCNOT
def Toffoly(control1, control2, controlled):
    controlled.H()
    CNOT(control2, controlled)
    controlled.Tdg()
    CNOT(control1, controlled)
    controlled.T()
    CNOT(control2, controlled)
    controlled.Tdg()
    CNOT(control1, controlled)
    control2.T()
    controlled.T()
    CNOT(control1, control2)
    controlled.H()
    control1.T()
    control2.Tdg()
    CNOT(control1, control2)

# CSWAP
def Fredkin(control, swap1, swap2):
    CNOT(swap2, swap1)
    Toffoly(control, swap1, swap2)
    CNOT(swap2, swap1)







