import numpy as np

A = np.array([[5.0, 2.0],
              [1.0, 7.0]])

b = np.array([13.0, 11.0])

x = np.array([1.0, 1.0])

N = 15

n = len(b)
x_new = np.zeros(n)
print(f"Initial guess:  {x}")

for k in range(N):
    for i in range(n):
        sum_ax = 0.0
        for j in range(n):
            if i != j:
                sum_ax += A[i, j] * x[j]

        x_new[i] = (b[i] - sum_ax) / A[i, i]

    x = x_new.copy()

    print(f"Iteration {k+1:<2}: x = {np.round(x, 4)}")
