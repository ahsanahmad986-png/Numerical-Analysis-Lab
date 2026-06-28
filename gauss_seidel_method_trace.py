import numpy as np
A = np.array([[26.0, 2.0, 2.0],
              [3.0, 27.0, 1.0],
              [2.0, 3.0, 17.0]])
b = np.array([12.6, -14.3, 6.0])
N = 10
n = len(b)
x = np.zeros(n)
indicator = 1
for i in range(n):
    if A[i][i] == 0:
        print("Gauss-Seidel Method Failed: Zero on the main diagonal.")
        indicator = 0
        break
if indicator:
    print(f"Iteration  0: {x}")
    for k in range(N):
        # We create a copy of x to cleanly separate old and new values during calculation
        x_new = np.copy(x)
        for i in range(n):
            sum1 = 0.0
            sum2 = 0.0
            for j in range(n):
                if j < i:
                    # Uses the most recently updated values (Gauss-Seidel magic)
                    sum1 += A[i][j] * x_new[j]
                elif j > i:
                    # Uses the values from the previous iteration
                    sum2 += A[i][j] * x[j]
            # The crucial missing formula to update x
            x_new[i] = (b[i] - sum1 - sum2) / A[i][i]
        x = np.copy(x_new)
        # Print the rounded results for this iteration
        print(f"Iteration {k+1:2}: {np.round(x, 4)}")
