import numpy as np
import matplotlib.pyplot as plt
from math import e


def f(x):
    return e ** x - 8 * x ** 2
def df(x):
    return e ** x - 16 * x

def newtonraphson(x0,eps):
    step = 0
    print('n\n***------newton rapshon------****')
    xn=x0
    for n in range(0,100):
        fxn=f(xn)
        if abs(fxn)<eps:
            print('\n akar persamaan tersebut:%0.8f'%xn)
            return xn
        dfxn=df(xn)
        if df(xn)==0:
            print('solusi tidak di temukan')
            return None
        xn=xn-(fxn/dfxn)
        step=step+1
        print('iterasi-%d,x=%0.8f dan f(x)=%0.8f'%(step,xn,f(xn)))
    print('iteraksi maksimum tidak ditemukan')

x0=float (input('x0:'))
eps=float(input('epsilon:'))
newtonraphson(0,eps)
