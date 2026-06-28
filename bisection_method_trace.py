def f(x):
    return x**3 - x - 2

a = 1
b = 2
error = b - a / 2
tolerance = 1e-6

def bisection_method(a, b, tolerance):
    if f(a) * f(b) >= 0:
        print("Bisection method fails. No root found in the given interval.")
        return None

    c = a
    iteration = 1

    while error >= tolerance:
        c = (a + b) / 2

        # Check if we found the exact root
        if f(c) == 0.0:
            break

        # Decide which sub-interval to choose
        if f(c) * f(a) < 0:
            b = c  # Root is in the left half
        else:
            a = c  # Root is in the right half

        print(f"Iteration {iteration}: Approximate Root = {c:.6f}")
        iteration += 1

    return c

# Execute
root = bisection_method(a, b, tolerance)
print(f"\nFinal Root found: {root:.6f}")
