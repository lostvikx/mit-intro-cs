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


# print(sumDigits("shs2ksn5"))
# print(f"try file = {__name__}")

if __name__ != "__main__":
  print(f"not main file, being imported as {__name__}")
else:
  print("__main__ file")