# Absolute crap.

def findPayment(loan:float, rate:float, months:int) -> float:
  """Assumes loan and rate are floats, while months is int.

  Eg: rate = 0.07
  
  Returns the monthly payment required to pay."""

  return loan*((rate*(1+rate)**months)/((1+rate)**months - 1))

# print(findPayment(112500.0, 0.14/12, 36))

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
    self.legend = None

  def makePayment(self):
    """Make a payment."""
    self.paid.append(self.payment)
    # Interpret them as mathematical equations (not assignment statements):
    # self.payment = payment_to_reduce + interest_due
    # payment_to_reduce = payment - interest_due
    reduction = self.payment - self.owed[-1]*self.monRate
    self.owed.append(self.owed[-1]-reduction)
  
  def getTotalPaid(self):
    """Return total money paid."""
    return sum(self.paid)

  def __str__(self) -> str:
      return self.legend

# Types of Mortgage
class Fixed(Mortgage):
  """Default mortgage scheme."""
  def __init__(self, loan: float, months: int, anRate: float) -> None:
    super().__init__(loan, months, anRate)
    self.legend = f"Fixed: {anRate*100}%"

class FixedWithPts(Mortgage):
  """Use points first."""
  def __init__(self, loan: float, months: int, anRate: float, pts:int) -> None:
    super().__init__(loan, months, anRate)
    self.pts = pts
    self.pain = [loan*(pts/100)]
    self.legend = f"Fixed: {anRate}% & {pts} Points"

