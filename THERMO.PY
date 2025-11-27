import numpy as np



a =0.3658
b=4.267*10**-5
T=300
P=50*10**5
R=8.314
A=1
B=-(b+R*T/P)
C=a/P
D=a*b/P
coeffs=[A,B,C,D]
Racines=np.roots(coeffs)
print(Racines)