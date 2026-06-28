def f(x):
    return x ** 2  # Define the function x^2

x = 2
h = 0.00001  # A small step size for approximation

# Approximate the derivative using the difference quotient
approx_derivative = (f(x + h) - f(x)) / h

# Actual derivative of x^2 is 2x. At x=2, the exact value is 4.
exact_value = 2 * x

print(f"Approximated Derivative at x=2: {approx_derivative}")
print(f"Exact Derivative at x=2: {exact_value}")
