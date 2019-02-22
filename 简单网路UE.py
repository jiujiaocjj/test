from scipy.optimize import linprog
import sympy
import math

cmax = [500,700,800,600,700]
t0 = [5,9,6,7,1]
A = [[1,1,0,0,0],
     [1,0,-1,-1,0],
     [0,1,1,0,-1],
     [0,0,0,1,1]]
b = [3000,0,0,3000]
Random_Index = [1,0,1,0,1]
res = linprog(Random_Index,A_eq=A,b_eq=b)
Link_Flow_0 = res.x
error_value=10
e=10**(-3)
lamda = sympy.Symbol('lamda')
while(error_value>e):
    Optimize_Index =  []
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
