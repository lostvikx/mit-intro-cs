import numpy as np

try:
  x = float(input("Enter number x: "))
except:
  print("NaN")
  exit()

try:
  y = float(input("Enter number y: "))
except:
  print("NaN")
  exit()

print("x**y =", x**y)

print("log(x) =", np.log2(x))