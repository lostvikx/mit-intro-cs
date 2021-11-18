import string

def isIn(a:str, b:str):
  if a in b or b in a:
    return True
  else:
    return False

# print(isIn("vikram", "vik"))

# A really efficient fibonacci function.
# A Fibonaccci sequence starts with 0, 1
def fib(n, d={0:1, 1:1}):
  """
  Assume n is int >= 0
  
  Returns Fibonacci number at postion n + 2
  """

  if n in d:
    return d[n]
  else:
    ans = fib(n-1) + fib(n-2)
    d[n] = ans
    return ans

# print(fib(11))  # 8

# Fibonacci poem {feeling especially geeky}
def get_fib_poem():
  with open("fibonacci_poem.txt", "r") as file_hand:

    for line in file_hand:
      if line != "":
        line = line.strip()
      # print(len(line))  # Used to know the line length
      print(line)

# get_fib_poem()

# This is a great example of divide and conquer problem solving principle.
def isPalindrome(s: str) -> bool:
  """
  s = string
  Ignore string cases & non-letters.

  Returns True if all letters in s form a palindrome, otherwise returns False.
  """

  s = s.lower()
  letters = ""
  for char in s:
    if char in string.ascii_lowercase:
      letters += char

  def isPal(s: str) -> bool:
    if len(s) <= 1:
      return True
    else:
      return s[0] == s[-1] and isPal(s[1:-1])

  return isPal(letters)


# First ever test function in python!
def test_isPalindrome():
  print(f"Is \"Mr. Owl ate my metal worm\" a palindrome?", end=" ")
  print(isPalindrome("Mr. Owl ate my metal worm"))  # True
  print(f"Is \"Was it a car or a cat I saw?\" a palindrome?", end=" ")
  print(isPalindrome("Was it a car or a cat I saw?"))  # True

# test_isPalindrome()
