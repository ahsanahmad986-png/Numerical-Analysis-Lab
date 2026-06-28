import matplotlib.pyplot as plt

print("==================================================")
print(" NUMERICAL ANALYSIS: FIXED-POINT STABILITY")
print("==================================================")

# --- 1. Define Functions ---
# Rearrangements of f(x) = x^3 + x - 1 = 0
def g1(x):
    return 1 - x**3  # Divergent case

def g2(x):
    return (1 - x)**(1/3)  # Convergent case

# --- 2. Simulation Setup ---
N = 100
x_start = 0.5
toler = 1e-6

g1_history = [x_start]
g2_history = [x_start]

# --- 3. Run Iterations ---
print("--- Testing g1(x) = 1 - x^3 (Oscillatory/Divergent) ---")
x = x_start
for i in range(1, N + 1):
    x_new = g1(x)
    g1_history.append(x_new)
    if abs(x_new - x) < toler:
        print(f"Converged after {i} iterations.")
        break
    x = x_new
else:
    print("DIVERGENT: Failed to converge within 100 iterations.\n")

print("--- Testing g2(x) = (1 - x)^(1/3) (Convergent) ---")
x = x_start
for i in range(1, N + 1):
    x_new = g2(x)
    g2_history.append(x_new)
    if abs(x_new - x) < toler:
        print(f"Converged to {x_new:.6f} after {i} iterations.")
        break
    x = x_new

# --- 4. Plotting Stability ---
plt.figure(figsize=(10, 6))
plt.plot(g1_history, label='g1 (Oscillates/Diverges)', color='green', marker='o')
plt.plot(g2_history, label='g2 (Converges)', color='blue', marker='x')
plt.title("Fixed-Point Iteration Stability Comparison", fontsize=14)
plt.xlabel("Iteration Number", fontsize=12)
plt.ylabel("Value of x", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()
