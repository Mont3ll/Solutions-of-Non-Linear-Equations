import math;
def f(x):
    return 5*x**4 + 3*x**2 - 2

x0=int(input("Enter initial guess: "))
print("Initial choice is ", x0)

x=x0
fx=f(x)
dfx=5*x**4 + 3*x**2 - 2
tolerance=1e-6
max_iterations=100

for i in range (max_iterations):
    x = x - fx/dfx
    if abs(f(x))<tolerance:
        print(f"proof found at x={c:.6f}")
        break
    else:
        print("Newton Raphson method failed to converge")
        x=x+1
