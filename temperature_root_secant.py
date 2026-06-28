def f(T):
  return T**3 - 6*T**2 + 4*T - 10

T0=5
T1=6

tol=1e-6

error = T1-T0

while (error>tol):
  T2=T1-(f(T1)*(T1-T0))/(f(T1)-f(T0))
  error = T2-T1
  T0,T1=T1,T2
  print(T2)
