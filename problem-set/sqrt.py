# Square root algorithm
# x is the number to find the square root of
# g is the random guess, in this case I have taken the first guess as 1
def square_root(x, g=1):
  
  # Fist we square the guess number
  sq = float(g * g)

  # If square of g is equal to x or lies between the range of +- 0.05 of x, then we have found our answer.
  if sq == x or (x >= sq-0.05 and x <= sq+0.05):

    return f"Sqaure root of {int(x)} is {round(g, 2)}"

  else:
    # Else we take a new guess, this process takes us closer to the answer.
    new_g = (g + x/g)/2
    
    # Return the recurrsive function call. Don't forget the return statement.
    return square_root(x, new_g)


while True:
  try:
    num = float(input("Find square root of number: "))
    break
  except:
    print("NaN")

print(square_root(num))
