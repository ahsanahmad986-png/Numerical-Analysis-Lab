import math

print("==================================================")
print(" NUMERICAL ANALYSIS: TAYLOR SERIES APPROXIMATION")
print("==================================================")

# --- 1. Configuration ---
x = 0.1
n_terms = 10  # Number of terms to include in the series
approx_e = 0

# --- 2. Calculate Taylor Series Sum ---
# Taylor Series for e^x: 1 + x + x^2/2! + x^3/3! + ... + x^n/n!
for n in range(n_terms):
    approx_e += (x ** n) / math.factorial(n)

# --- 3. Compute Actual Value ---
# Get the true value using Python's built-in math module
actual_e = math.exp(x)

# --- 4. Output Results ---
print(f"Approximated value of e^{x} ({n_terms} terms): {approx_e:.10f}")
print(f"Actual value using math.exp({x}):     {actual_e:.10f}")
print(f"Absolute Error (Difference):          {abs(actual_e - approx_e):.10e}")
