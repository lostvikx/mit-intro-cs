# A cool mortgage calculator!

def findPayment(loan:float, rate:float, months:int) -> float:
  """Assumes loan and rate are floats, while months is int.

  Eg: rate = 7% = 0.07
  
  Returns the monthly payment required to pay."""

  return loan*((rate*(1+rate)**months)/((1+rate)**months - 1))

print(findPayment(112500.0, 0.14/12, 36))

class Mortgage(object):
  """Build different kinds of morgages."""

  def __init__(self, loan:float, months:int, anRate:float) -> None:
    """"Create a new mortgage."""
    self.loan = loan
    self.monRate:float = anRate/12
    self.months = months
    self.paid:list = [0.0]
    self.owed:list = [loan]
    self.payment = findPayment(loan, self.monRate, months)

  def makePayment(self):
    """Make a payment."""
    self.paid.append(self.payment)
    # reduction = 