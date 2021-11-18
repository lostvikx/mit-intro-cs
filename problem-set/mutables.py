techs = ["MIT", "CalTech"]
ivys = ["Harvard", "Yale", "Brown"]

unis = [techs, ivys]
unis2 = [techs, ivys]

techs.append("IIT")

# print("unis =", unis)
# print("unis2 =", unis2)

mixed = [1, 2, "a", 3, 4.1]
square_ints = [x**2 for x in mixed if type(x) == int]
# print(square_ints)

# Map function
l1 = [1, 28, 36]
l2 = [2, 57, 9]
l3 = list(map(min, l1, l2))
print(l3)
