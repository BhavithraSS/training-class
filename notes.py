def no_notes(a):
  Q = [500, 200, 100, 50, 20, 10]
  x = 0
  for i in range(6):
    q = Q[i]
    x += int(a / q)
    a = int(a % q)
  if a > 0:
    x = -1
  return x
n=int(input("input your value"))
m=int(input("input your value"))
print(no_notes(n))
print(no_notes(m))def no_notes(a):
  Q = [500, 200, 100, 50, 20, 10]
  x = 0
  for i in range(6):
    q = Q[i]
    x += int(a / q)
    a = int(a % q)
  if a > 0:
    x = -1
  return x
n=int(input("input your value"))
m=int(input("input your value"))
print(no_notes(n))
print(no_notes(m))
