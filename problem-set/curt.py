# Guess & Check
# Simple
# cube = int(input("Enter a cubic number: "))

# for guess in range(cube+1):
#   if guess**3 == cube:
#     print(f"Cube root of {cube} is {guess}")

# Complex
# num = int(input("Enter a number: "))

# for guess in range(abs(num)+1):
#   if guess**3 >= abs(num):
#     break

# if guess**3 != abs(num):
#   print("is not a perfect cube")
# else:
#   if num < 0:
#     guess = -guess
  
#   print(f"Cube root of {num} is {guess}")

# Approximation
# cube = int(input("Enter a number: "))
# # The accuracy
# epsilon = 0.01
# guess = 0.0
# increment = 0.0001
# num_guess = 0

# # The second conditional is important as the epsilon range can be skipped.
# while abs(guess**3 - cube) >= epsilon and guess <= cube:
#   guess += increment
#   num_guess += 1

# print("Guesses:", num_guess)

# if abs(guess**3 - cube) >= epsilon:
#   print("Failed to find the cube root")
# else:
#   print(f"{guess} is a close approximate")

# Bisection
cube = float(input("Enter a number: "))
epsilon = 0.01
num_guesses = 0

# If the values are less than 1 {can include negative}
if cube < 1:
  low = cube
  high = 1
else:
  low = 0
  high = cube

guess = low + ((high - low) / 2)

while abs(guess**3 - cube) >= epsilon:

  if guess **3 < cube:
    low = guess
  else:
    high = guess

  guess = low + ((high - low) / 2)
  num_guesses += 1

print("Guesses:", num_guesses)
print(f"{round(guess, 4)} is the cube root of {cube}")
