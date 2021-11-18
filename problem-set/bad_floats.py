# Computers can't compute floats!
x = 0.0

for i in range(10):
  x += 0.1

if x == 1.0:
  print(x, "= 1.0")
else:
  print(x, "!= 1.0")