import datetime
# import try_except

# Person class inherits all the attributes of object class
class Person(object):

  # assumes avg life expectancy = 72 yrs
  # while converting to days, not accouting for leap years
  avg_life_days = 72*365 # class variable

  def __init__(self, name:str) -> None:
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
    """Assumes birthdate is of type datetime.date(year, month, date)"""
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


# me = Person("Vikram Negi")
# me.setBirthday(datetime.date(2000, 9, 29))
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
# print(type(me) == Person)

# testing = try_except.sumDigits("sk21")

# if __name__ == "__main__":
#   print(createBar(me.getPercentLived()))
#   print(f"main file = {__name__}")
# else:
#   print("not main file")

class ITMPerson(Person):

  # class variable, not unique to an instance
  idCount = 0

  def __init__(self, name:str) -> None:
    super().__init__(name)
    self.idNum = ITMPerson.idCount
    ITMPerson.idCount += 1

  def getIdNum(self) -> int:
    """Returns id"""
    return self.idNum

  def __lt__(self, other) -> bool:
    """Sort idNum in ascending order."""
    return self.idNum < other.idNum


# me2 = ITMPerson("Vikram Negi")
# print(type(me2) == Person)  # False
# print(isinstance(me2, Person))  # Person is a superclass of ITMPerson

# Subclass of ITMPerson
# Class hierarchy:
# object -> Person -> ITMPerson -> Student
class Student(ITMPerson):
  pass

class Grades(object):
  """Mapping from students type to a list of grades."""

  def __init__(self) -> None:
    """Create instance variable, an empty grade book."""
    self.students = []
    self.grades = {}
    self.isSorted = True

  def addStudent(self, student:Student) -> None:
    """Assumes student is of type Student.

       Add student to the grade book."""

    assert not student in self.students, "Student already in grade book"

    self.students.append(student)
    # Using idNum as keys with Values being the None initially
    self.grades[student.getIdNum()] = []

    if self.isSorted:
      self.isSorted = False

  def addGrade(self, student:Student, grade:float) -> None:
    """Append grade as the value of grades dict."""

    try:
      self.grades[student.getIdNum()].append(grade)
    except:
      raise ValueError("Add student to the grade book")

  def getGrades(self, student:Student) -> list:
    """Returns a copy of grades list."""

    try:
      return self.grades[student.getIdNum()][:]
    except:
      raise ValueError("Add student to the grade book")

  # def getStudents(self) -> list:
  #   """Returns a sorted list of students."""
    
  #   # With sorted we can get rid of the sorted array mutation problem, no side-effects (functional rocks!)
  #   # Using this method is inefficient, because a new list is created.
  #   return sorted(self.students)

  def getStudents(self):
    """Returns the students in the grade book one at a time."""

    # Sort list of students
    if not self.isSorted:
      self.students.sort()
      self.isSorted = True

    # Yields on stud at a time, as opposed to returning a list of students.
    for stud in self.students:
      yield stud

  

def gradeReport(subject:Grades) -> str:
  """Assumes subject as Grades type.
  
  Returns grade report as a string."""

  report = ""

  # Now, getStudents method doesn't return a list.
  # It yields one Student type at a time, making the computation faster.
  for stud in subject.getStudents():
    totalMarks = 0  # Total Marks
    nSubs = 0  # Total Subjects

    # For each student, loop over their grades
    for grade in subject.getGrades(stud):
      totalMarks += grade
      nSubs += 1

    try:
      avg = round(totalMarks / nSubs, 2)
    except:
      avg = float("NaN")

    report += f"{str(stud)}'s mean grade is {avg}\n"

  return report

# Tests
s1 = Student("Vikram Negi")
s2 = Student("Dale Carnegie")
s3 = Student("Cal Newport")

math = Grades()
math.addStudent(s1)
math.addStudent(s2)
math.addStudent(s3)

# Add 75 marks of all students
for stud in math.getStudents():
  math.addGrade(stud, 75)

math.addGrade(s1, 90)
math.addGrade(s2, 65)
math.addGrade(s3, 70)

# print(math.getStudents())  # ['Cal Newport', 'Dale Carnegie', 'Vikram Negi']
# print(math.getGrades(s1))

# print(type(s1) == Student)  # True
# print(isinstance(s1, Student))  # True

s4 = Student("Jordan Peterson")
math.addStudent(s4)
# print(math.grades)

print(gradeReport(math))
