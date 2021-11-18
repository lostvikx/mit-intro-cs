# Curreny = US Dollar
while True:
  try:
    annual_salary = float(input("Enter your annual salary: "))
    break
  except:
    print("NaN")

while True:
  try:
    portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
    break
  except:
    print("NaN")

while True:
  try:
    total_cost = float(input("Enter the cost of your dream home: "))
    break
  except:
    print("NaN")

portion_down_payment = 0.25
current_savings = 0

# Assume my investments give me a return of 4% pa
r = 0.04
# Monthly income from investments on savings
# current_savings += current_savings * r/12

monthly_salary = annual_salary/12

months = 0

while current_savings < portion_down_payment * total_cost:

  months += 1
  current_savings += current_savings * r/12
  current_savings += monthly_salary * portion_saved
  current_savings = round(current_savings, 2)

print(f"Number of months: {months}")
