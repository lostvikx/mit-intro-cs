# Print largest old number, taking 10 input numbers
# num_inputs = []
# n = 10
# largest = None

# while n > 0:

#   try:
#     num_inputs.append(int(input("Enter a number: ")))
#   except:
#     print("NaN")
#     continue

#   n -= 1

# for num in num_inputs:

#   if largest == None or num > largest:
    
#     if num % 2 != 0:
#       largest = num

# if largest is None:
#   print("No odd numbers.")
# else:
#   print(f"Largest odd number is {largest}")

# Solution without using the list data structure, it looks much cooler in my opinion.
n = 10
largest = None

while n > 0:

  try:
    num = int(input("Enter a number: "))

    if largest == None or num > largest:

      if num % 2 != 0:
        largest = num

  except:
    print("NaN")
    continue

  n -= 1

if largest is None:
  print("No odd numbers.")
else:
  print(f"Largest odd number is {largest}")
