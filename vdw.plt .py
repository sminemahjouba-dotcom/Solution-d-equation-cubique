import matplotlib.pyplot as plt
R=0.08134
n=2
V=1
a=3.658
b=0.04267
def vdw(T):
    P=(((n*R*T)/(V-(n*b))) - (((n**2)*(a))/(V**2)))
    return P
P=[]
t=[]
for i in range (300,321):
    P.append(vdw(i))
    t.append(i)
print(t,P)
plt.scatter(t,P)
plt.show()


