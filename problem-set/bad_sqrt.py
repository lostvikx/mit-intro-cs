num = int(input("Enter a number: "))

iter_num = 0
pwr = 0

if num == 0:
  root = 0
else:
  root = 1

while root**pwr != num and root < num:

  while pwr < 6:
    iter_num += 1
    if root**pwr == num:
      print(root, "^", pwr, sep="")
      break
    pwr += 1

  if root**pwr == num:
    break
  else:
    pwr = 0

  root += 1

if root**pwr != num:
  print("Not found")

print("Iterations:", iter_num)