import math
import matplotlib.pyplot as plt

print("==================================================")
print(" NUMERICAL ANALYSIS: EULER'S METHOD FOR ODEs")
print("==================================================")

# --- 1. Configuration ---
a = 0.0          # Start time
b = 4.0          # End time (extended to visualize convergence)
h = 0.2          # Step size
N = int((b - a) / h)
alpha = 1.0      # Initial condition y(0)

# --- 2. Setup Data Lists ---
t = a
y = alpha
T = [t]
Y_numerical = [y]
Y_exact = [1 + 0.5 * math.exp(-4 * t) - 0.5 * math.exp(-2 * t)]

# --- 3. Euler's Method Loop ---
for i in range(1, N + 1):
    # Differential equation: dy/dt = 2 - exp(-4t) - 2y
    f = 2 - math.exp(-4 * t) - 2 * y
    
    # Euler Update
    y = y + h * f
    t = a + i * h
    
    # Store results
    T.append(t)
    Y_numerical.append(y)
    Y_exact.append(1 + 0.5 * math.exp(-4 * t) - 0.5 * math.exp(-2 * t))

# --- 4. Plotting ---
plt.figure(figsize=(10, 6))
plt.plot(T, Y_numerical, label='Numerical (Euler)', color='green', marker='o', linestyle='--')
plt.plot(T, Y_exact, label='Exact Mathematical Solution', color='blue', linewidth=2)
plt.title('Euler\'s Method vs Exact ODE Solution', fontsize=14)
plt.xlabel('Time (t)', fontsize=12)
plt.ylabel('y(t)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()
