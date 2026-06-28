import math

Is = 1e-12
Vt = 0.025
I = 1e-3

def f(v):
    # Fixed: Changed 'vt' to 'Vt'
    return Is*(math.exp(v/Vt)-1)-I

a = 0
b = 1
tolerance = 1e-6

def bisection(a, b, tolerance):
    if f(a) * f(b) >= 0:
        print("Invalid interval. Signs must be opposite.")
        return None

    c = a
    iteration = 1

    # Fixed: Moved error calculation inside the function
    error = b - a / 2

    while error >= tolerance:
        c = (a + b) / 2

        if f(c) == 0.0:
            break

        if f(c) * f(a) < 0:
            b = c
        else:
            a = c

        # Fixed: Update error inside the loop so it eventually stops!
        error = b - a

        iteration += 1

    return c

# Execute
voltage_root = bisection(a, b, tolerance)

if voltage_root is not None:
    print(f"Calculated Voltage (V) across the diode: {voltage_root:.6f} Volts")
