# Curreny = US Dollar
while True:
  try:
    annual_salary = float(input("Enter your annual salary: "))
    break
  except:
    print("NaN")

semi_annual_raise = 0.07
total_cost = 1000000.00
portion_down_payment = 0.25
total_dp = portion_down_payment * total_cost

# Assume my investments give me a return of 4% pa
r = 0.04
# My take on the question, keeping epsilon as 1000, will provide much better results when comparing to the $100 range provided in the question.
epsilon = 1000
high = 10000
low = 0
portion_saved = None
current_savings = 0
num_bisection = 0

while int(abs(current_savings - total_dp)) > epsilon:

  months = 0
  possible = True
  mid = int(low + ((high - low)/2))
  # print("mid:", mid)
  portion_saved = mid/10000
  # print("saved:", portion_saved)
  test_cur_sav = 0
  test_ann_sal = annual_salary
  monthly_salary = test_ann_sal/12

  while test_cur_sav < total_dp and months < 36:

    if months != 0 and months % 6 == 0:
      test_ann_sal += (test_ann_sal * semi_annual_raise)
      # This is an important step
      monthly_salary = test_ann_sal/12

    months += 1
    test_cur_sav += test_cur_sav * r/12
    test_cur_sav += monthly_salary * portion_saved
    test_cur_sav = round(test_cur_sav, 2)


  if test_cur_sav < total_dp:
    low = mid
    if low == 9999:
      print("It is not possible to pay the down payment in three years.")
      break
  else:
    high = mid
    # print("can save")
    current_savings = test_cur_sav

  # print("high:", high)
  # print("low:", low)
  # print("test_cur:", test_cur_sav)
  num_bisection += 1
  

if portion_saved < 0.9999:
  print("Best savings rate:", portion_saved)
  print("Steps in bisection search:", num_bisection)
