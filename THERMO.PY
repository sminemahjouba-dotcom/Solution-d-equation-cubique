import numpy as np

A=1
B=-0.9775
C=0.1664
D=-0.003758 
coeffs=[A,B,C,D]
Racines=np.roots(coeffs)
print(Racines)
import thermo as thermo
print(thermo.__version__)

