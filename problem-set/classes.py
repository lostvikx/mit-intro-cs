import datetime
# import try_except

# Person class inherits all the attributes of object class
class Person(object):

  # assumes avg life expectancy = 72 yrs
  # while converting to days, not accouting for leap years
  avg_life_days = 72*365 # class variable

  def __init__(self, name) -> None:
    """Create a person"""

    self.name = name
    space_index = name.find(" ")

    if space_index > 0:
      self.lastName = name[space_index+1:]
    else:
      self.lastName = None
      
    self.birthday = None

  def getName(self) -> str:
    """Returns person's full name"""
    return self.name

  def getLastName(self) -> str:
    """Returns person's last name"""
    return self.lastName

  def setBirthday(self, birthdate) -> None:
    """Assumes birthdate is of type datetime.date, {year, month, date}"""
    self.birthday = birthdate

  def getAge(self) -> int:
    """Returns person's current age in years"""
    assert self.birthday != None, "Birthday not mentioned"

    return (datetime.date.today() - self.birthday).days

  def __str__(self) -> str:
    """Returns self's name"""
    return self.name

  def getDaysLeft(self) -> int:
    """Returns person's number of days left to live, according to the average life expectancy"""
    return Person.avg_life_days - self.getAge()

  def getPercentLived(self) -> int:
    """Returns person's days lived in float percentage"""
    return round((self.getAge() / Person.avg_life_days)*100, 2)

  def getLifeBar(self, bar_len=50) -> str:
    """
    Returns a string, a life bar to represent the percentage lived by a person.
    Assumes that bar_len >= 10
    """
    assert bar_len >= 10, "Bar lenght should be atleast 10"

    # self.getPercentLived() is float {percentage}
    divide = 100/bar_len

    # Round float (0 decimal) & divide to match ratio of the barLen
    life = round(self.getPercentLived()/divide)
    life_left = bar_len - life

    # The LifeBar
    bar_icon = "#"
    # Format the bar
    bar = f"{Colors.fail}{bar_icon*life}{Colors.end}{Colors.green}{bar_icon*life_left}{Colors.end}"

    life_bar = f"[{bar}] -> {self.getPercentLived()}% Lived"

    return f"{life_bar}, {Colors.warning}{self.getDaysLeft()}{Colors.end} days left!"


me = Person("Vikram Negi")
me.setBirthday(datetime.date(2000, 9, 29))
# my_current_age = f"{me.getName()} is {me.getAge()} days old!"
# print(my_current_age)
# my_life_lived = f"{me.getName()} has lived {me.lifeLived()}% of his life!"
# print(my_life_lived)

class Colors:
  blue = "\033[94m"
  green = "\033[92m"
  warning = "\033[93m"
  fail = "\033[91m"
  bold = "\033[1m"
  underline = "\033[4m"
  end = "\033[0m"

# print(me.getLifeBar())

# testing = try_except.sumDigits("sk21")

# if __name__ == "__main__":
#   print(createBar(me.getPercentLived()))
#   print(f"main file = {__name__}")
# else:
#   print("not main file")

class ITMPerson(Person):

  # class variable, not unique to an instance
  idCount = 0

  def __init__(self, name) -> None:
    super().__init__(name)
    self.idNum = 0
    ITMPerson.idCount += 1

  def getIdNum(self) -> int:
    """Returns id"""
    return self.idNum


me2 = ITMPerson("Vikram Negi")
print(me.getLifeBar())
