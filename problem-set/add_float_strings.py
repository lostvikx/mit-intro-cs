s = "1.23,2.4,3.123"
total, i = 0, 0

if s[0] == ",":
  s = s[1:]
elif s[-1] == ",":
  s = s[:-1]

while i < len(s):

  if s[i] == ",":
    total += float(s[:i])
    s = s[i+1:]
    i = -1

  if i == len(s) - 1 and s != "":
    total += float(s)
    break

  i += 1

print(total)
