from scipy.optimize import linprog
import sympy
import math

cmax = [15,20,13,20,22,20,15,17,15,10]
t0 = [5,6,2,4,3,6,2,3,6,3]
A=[[1,1,0,0,0,0,0,0,0,0],
   [1,0,-1,0,0,0,-1,0,0,0],
   [0,1,0,-1,0,0,0,-1,0,0],
   [0,0,1,0,-1,0,0,1,-1,0],
   [0,0,0,1,0,-1,1,0,0,-1],
   [0,0,0,0,1,0,0,0,0,1],
   [0,0,0,0,0,1,0,0,1,0]]
b=[80,0,0,0,0,40,40]
Random_Index=[1,0,1,0,1,0,1,0,1,0]
res=linprog(Random_Index,A_eq=A,b_eq=b)
Link_Flow_0=res.x
error_value=10
e=10**(-4)
lamda = sympy.Symbol('lamda')
while(error_value>e):
    Optimize_Index = []
    for i in range(0,len(cmax)):
        Optimize_Index.append(t0[i]*(1+0.15*(Link_Flow_0[i]/cmax[i])**4))
    res = linprog(Optimize_Index,A_eq=A,b_eq=b)
    Link_Flow_1=res.x
    Difference = Link_Flow_1-Link_Flow_0
    Link_Flow_2=Link_Flow_0+lamda*Difference
    Function=[]
    for i in range(0,len(cmax)):
        Function.append(Difference[i]*t0[i]*(1+0.15*(Link_Flow_2[i]/cmax[i])**4))
    possible_value=sympy.solve(sum(Function))
    lamda_value=[]
    for i in possible_value:
        try :
            i=float(i)
            if i>0 and i<1:
                lamda_value.append(i)
        except:
            continue
    Link_Flow_0=Link_Flow_0+lamda_value[0]*Difference
    error_value=math.sqrt(sum((lamda_value[0]*Difference)**2))/(Link_Flow_0).sum()
    print(error_value)
print(Link_Flow_0)
