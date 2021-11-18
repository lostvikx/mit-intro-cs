def findAnEven(l):
  """
  Assumes l is a list of ints

  Returns the first even num in l
  
  Raises ValueError if l doesn't contain an even num
  """

  first_even_n = 0

  for num in l:
    if num % 2 == 0:
      first_even_n = num
      break
  
  if first_even_n == 0:
    raise ValueError("l doesn't contain an even number")
  else:
    return first_even_n

# print(findAnEven([1, 4, 3, 7])) # Works fine!

def getRatios(vect1, vect2):
  """
  Assumes: vect1 and vect2 are lists of equal length.

  Returns: a list containing ratios.
  """

  ratios = []

  for num1, num2 in zip(vect1, vect2):
    try:
      ratios.append(num1/num2)
    except ZeroDivisionError:
      ratios.append(float("nan")) # Not a number
    except:
      raise ValueError("getRatios called with bad args")

  return ratios

# print(getRatios([1, 2, 4], [2, 5, 0]))  # [0.5, 0.4, nan]