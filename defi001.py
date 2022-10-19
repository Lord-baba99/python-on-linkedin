a, b, c, k, n = 1, 4, 3, 1, 0

while k < 1000 - n:
  a = b
  b = c + a
  c = (-4)*c - 3*a - b
  n = a + b
  k += 1

print(a, b, c)