# Newton-Raphson square root
# Also called successive approximation
# x^2 - k = 0, dy/dx = 2x
# First guess = x/2 = y
# Next guess = y - ((y^2 - k) / 2y)
x = int(input("Enter a number: "))
epsilon = 0.01
# Guess
g = x/2
num_iter = 0

while abs(g*g - x) >= epsilon:
  g = g - (((g**2) - x)/ (2 * g))
  num_iter += 1

print(f"Square root of {x} is about {round(g, 2)}")
print(f"Took {num_iter} guesses")

# Newton-Raphson is the most efficient algorithm for finding the square root.