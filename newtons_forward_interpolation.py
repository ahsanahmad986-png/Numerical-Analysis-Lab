import numpy as np

print("==================================================")
print(" NUMERICAL ANALYSIS: NEWTON'S FORWARD DIFFERENCE")
print("==================================================")

# --- 1. Define Data Points ---
x = np.array([1.0, 2.0, 3.0, 4.0])
y = np.array([1.0, 8.0, 27.0, 64.0])
x_target = 2.5

n = len(x)
h = x[1] - x[0]  # Assuming equal spacing
p = (x_target - x[0]) / h

# --- 2. Construct Forward Difference Table ---
dif_t = np.zeros((n, n))
dif_t[:, 0] = y

for j in range(1, n):
    for i in range(0, n - j):
        dif_t[i, j] = dif_t[i + 1, j - 1] - dif_t[i, j - 1]

# --- 3. Compute Newton's Forward Interpolation ---
result = y[0]
fact = 1.0
p_term = 1.0

for i in range(1, n):
    fact *= i
    p_term *= (p - (i - 1))
    result += (p_term * dif_t[0, i]) / fact

print(f"Interpolating at x = {x_target}")
print(f"Newton's Forward Difference Result: {result:.6f}")
