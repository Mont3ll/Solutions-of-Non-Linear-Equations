import math;
def f(x):
    return x**3-2*x-5

a=2
b=3
tolerance=1e-6
max_iterations=100

for i in range (max_iterations):
    c=(a+b)/2
    if abs(f(c))<tolerance:
        print(f"proof found at x={c:.6f}")
        break
    elif f(c)*f(a)<0:
        max_iterations=100
        b=c;
    else:
         a=c
