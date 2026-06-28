def f(x):
  return x**3 - 4*x**2 + 1

def df(x):
  return 3*x**2 - 8*x

x0 = 0.2
tol=1e-6

for i in range (0,100):
  x1=x0 - f(x0)/df(x0)
  if(abs(x1-x0)<tol):
    break
  x0=x1

print(x1)
