import numpy as np
import math
import matplotlib.pyplot as plt

print("==================================================")
print(" NUMERICAL ANALYSIS: 4th ORDER RUNGE-KUTTA (RK4)")
print("==================================================")

# --- 1. Define ODE and Exact Solution ---
# dy/dx = x + y
def f(x, y):
    return x + y

# Exact solution: y = 2*exp(x) - x - 1
def exact_solution(x):
    return 2 * math.exp(x) - x - 1

# --- 2. Configuration ---
N = 10           # Number of steps
x0 = 0.0         # Initial x
y0 = 1.0         # Initial y
h = 0.2          # Step size

y_numerical = [y0]
x_numerical = [x0]
y_exact = [exact_solution(x0)]

# --- 3. RK4 Implementation ---
for i in range(1, N + 1):
    k1 = f(x0, y0)
    k2 = f(x0 + h/2, y0 + h*k1/2)
    k3 = f(x0 + h/2, y0 + h*k2/2)
    k4 = f(x0 + h,   y0 + h*k3)
    
    # RK4 weighted average update
    y0 = y0 + (h/6) * (k1 + 2*k2 + 2*k3 + k4)
    x0 = x0 + h

    y_numerical.append(y0)
    x_numerical.append(x0)
    y_exact.append(exact_solution(x0))

# --- 4. Plotting ---
plt.figure(figsize=(10, 6))
plt.plot(x_numerical, y_numerical, label='Numerical (RK4)', color='green', linewidth=2)
plt.plot(x_numerical, y_exact, 'bo', label='Exact Solution', markersize=4)
plt.title('4th-Order Runge-Kutta vs Exact ODE Solution', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()
