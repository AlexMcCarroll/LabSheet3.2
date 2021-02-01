class Employee:
  def __init__(self):
    self._employeeID = 0
    self.empTitle = ''
    self.forename = ''
    self.surname = ''
    self.email = ''
    self.salary = 0

  def get_employee_id(self):
    return self._employeeID

  def set_employee_id(self, value):
    self._employeeID = value

  def set_employee_title(self, empTitle):
    self.empTitle = empTitle

  def set_forename(self, forename):
   self.forename = forename
  
  def set_surname(self,surname):
    self.surname = surname

  def set_email(self,email):
    self.email = email
  
  def set_salary(self,salary):
    self.salary = salary
  
  # def get_employee_id(self):
  #   return self.employeeId

  def get_employee_title(self):
    return self.empTitle
  
  def get_forename(self):
    return self.forename
  
  def get_surname(self):
    return self.surname
  
  def get_email(self):
    return self.email
  
  def get_salary(self):
    return self.salary

  def __str__(self):
    return str(self.employeeID)+"\n"+self.empTitle+"\n"+ self.forename+"\n"+self.surname+"\n"+self.email+"\n"+str(self.salary)