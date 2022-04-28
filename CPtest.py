# Copyright (C) 2022 Andrey Abramov
# Apache License 2.0

from FastQubit import *

Q5 = Register('CP_H_up', 2)
Q5[0].H()
CP_pi(Q5[0], Q5[1], 4)
Q5.show()

Q4 = Register('CP_up_H', 2)
Q4[1].H()
CP_pi(Q4[0], Q4[1], 4)
Q4.show()

Q3 = Register('CP_down_up', 2)
Q3[0].X()
CP_pi(Q3[0], Q3[1], 4)
Q3.show()

Q2 = Register('CP_up_down', 2)
Q2[1].X()
CP_pi(Q2[0], Q2[1], 4)
Q2.show()

Q1 = Register('CP_up_up', 2)
CP_pi(Q1[0], Q1[1], 4)
Q1.show()




