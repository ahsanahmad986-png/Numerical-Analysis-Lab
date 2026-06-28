import numpy as np
from scipy.interpolate import lagrange

print("==================================================")
print(" NUMERICAL ANALYSIS: LAGRANGE INTERPOLATION")
print("==================================================")

# --- 1. Define Data Points ---
x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 3.0, 5.0])
x_target = 2.5

# --- 2. Lagrange Interpolation Function ---
def lagrange_interpolate(x_vals, y_vals, x_not):
    n = len(x_vals)
    result = 0.0
    
    for k in range(n):
        # Calculate the Lagrange basis polynomial L_k(x)
        term = y_vals[k]
        for i in range(n):
            if i != k:
                term *= (x_not - x_vals[i]) / (x_vals[k] - x_vals[i])
        result += term
    return result

# --- 3. Execute ---
interpolated_val = lagrange_interpolate(x, y, x_target)

# Verify with SciPy
poly = lagrange(x, y)
scipy_val = poly(x_target)

print(f"Interpolating at x = {x_target}")
print(f"Manual Lagrange Result: {interpolated_val:.6f}")
print(f"SciPy Verification:     {scipy_val:.6f}")
