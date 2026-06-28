def f(x):
  return x**3 - 2*x + 2

x0=-2
x1=-1

tol=1e-6

error = x1-x0

while (error>tol):
  x2=x1-(f(x1)*(x1-x0))/(f(x1)-f(x0))
  error = x2-x1
  x0,x1=x1,x2
  print(x2)
