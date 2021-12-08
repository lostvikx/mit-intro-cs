colors = {
  "blue": "\033[94m",
  "green": "\033[92m",
  "warning": "\033[93m",
  "fail": "\033[91m",
  "bold": "\033[1m",
  "underline": "\033[4m",
  "end": "\033[0m"
}

test_str = "Vikram is a cool boi!"

for i in range(100):

  test_color = f"\033[{i}m"

  print(f"{test_color}{test_str}{colors['end']}  i = {i}")