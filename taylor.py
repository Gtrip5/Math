import sympy as sp
import numpy as np
import matplotlib.pyplot as mp
import math

def eval_func(r, func, symbol):
    y = [func.subs(symbol, xx) for xx in r]
    return y

def taylor_func(func, symbol, pos, num_terms):
    p_terms = []
    for n in range(num_terms): 
        fnx = sp.diff(func, symbol, n)
        deriv = fnx.subs(symbol, pos)
        p_terms.append(deriv/math.factorial(n)*sp.Pow(symbol-pos, n))
        
    return p_terms
        
symx = sp.Symbol('x')
func = sp.sin(symx)

approx_point = 0.0

r = np.linspace(approx_point-1, approx_point+1, 301)
dfunc = sp.diff(func, symx)

y = eval_func(r, func, symx)
y_d = eval_func(r, dfunc, symx)
n_terms = 6
series_terms = taylor_func(func, symx, approx_point, n_terms)
tt = [eval_func(r, t, symx) for t in series_terms]
rr = r*0.0
for i, t in enumerate(tt):
    rr = rr + t
    mp.plot(r, rr, label=str(i))
    print(series_terms[i])
    
mp.plot(r, y, label='y(x)')
#mp.plot(r, y_d, label='dy/dx(x)')
mp.legend()
mp.show()
    #print(sinx(r))
    
    
