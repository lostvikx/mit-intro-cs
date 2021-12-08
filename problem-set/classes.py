import datetime

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

  def daysLived(self) -> int:
    """Returns person's days lived in percentage int"""
    return round((self.getAge() / Person.avg_life_days)*100, 2)


me = Person("Vikram Negi")
me.setBirthday(datetime.date(2000, 9, 29))
# my_current_age = f"{me.getName()} is {me.getAge()} days old!"
# print(my_current_age)
# my_life_lived = f"{me.getName()} has lived {me.lifeLived()}% of his life!"
# print(my_life_lived)

my_life = me.daysLived()

class colors:
  green = "\033[92m"
  end = "\033[0m"

# bar_len = 50
# half_life = round((my_life/2))
# bar_life = 50 - half_life
# bar_icon = "#"
# bar = f"{colors.green}{bar_icon*half_life}{colors.end}{bar_icon*bar_life}"
# life_loading_bar = f"[{bar}] -> {my_life}% Lived"
# print(life_loading_bar)

def createBar(days_lived, bar_len=50) -> str:
  # days_lived in percentage int
  divide = 100/bar_len
  life = round(days_lived/divide)
  life_left = bar_len - life
  bar_icon = "#"
  bar = f"{colors.green}{bar_icon*life}{colors.end}{bar_icon*life_left}"
  life_bar = f"[{bar}] -> {my_life}% Lived"
  return life_bar

print(createBar(me.daysLived()))