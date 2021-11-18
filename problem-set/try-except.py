def sumDigits(s):
  """
  Assume s is a str
  
  Returns the sum of the numbers in s
  """

  total_sum = 0

  for char in s:
    try:
      char = int(char)
      total_sum += char
    except ValueError:
      pass

  return total_sum

print(sumDigits("shs2ksn5"))