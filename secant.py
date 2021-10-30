import numpy as np
import matplotlib.pyplot as plt
from math import e

def f(x):
    return e ** x - 8 * x ** 2
def secant(x0,x1,eps,N):
    step=1
    condition=True
    while condition:
        if f(x0)==f(x1):
            print('solusi tidak ditemukan')
            break
        x2=x1-((f(x1)*(x1-x0))/(f(x1)-f(x0)))
        print('iterasi-%d,x=%0.8f dan f(x)=%0.8f'%(step,x2,f(x2)))
        x0=x1
        x1=x2
        step=step+1
        if step>N:
            print('divergen')
            break

            condition=abs(f(x2))>eps
            print('\n akar persamaan tersebut:=%0,8f'%x2)

x0=float(input('x0:'))
x1 = float(input('x1:'))
N = int(input('max iter:'))
eps = float(input('epsilon:'))
secant(x0,x1,eps,N)




