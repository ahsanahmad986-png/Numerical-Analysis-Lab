import math

iterations = 100000  # Leibniz formula converges slowly, so we need many iterations
pi_approx = 0

# Calculate the sum using a loop
for n in range(iterations):
    term = (-1)**n / (2*n + 1)
    pi_approx += term

pi_approx *= 4  # Multiply by 4 to get pi

actual_pi = math.pi

print(f"Approximated value of Pi (Leibniz): {pi_approx}")
print(f"Actual value of Pi (math.pi): {actual_pi}")
print(f"Difference: {abs(actual_pi - pi_approx)}")
