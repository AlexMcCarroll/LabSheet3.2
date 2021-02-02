import sqlite3
import pandas as pd
import Constants as constants
from Employee import Employee

class DBOperations:
 
  def __init__(self):
    self.get_connection()

  def get_connection(self):
    self.conn = sqlite3.connect("mydb")
    self.cur = self.conn.cursor()

  def drop_table(self):
    self.conn.execute(constants.sql_drop_table)

  # Create Table
  def create_table(self):
    try:
      self.get_connection()
      self.cur.execute(constants.sql_create_table)
      self.conn.commit()
      print(constants.table_created)
    except Exception as e:
      if "table EmployeeUoB already exists":
        print(constants.table_exists)
      else:
        print(type(e))
    finally:
      self.conn.close()

  # Insert Data
  def insert_data(self):
    try:
      self.get_connection()
      emp = Employee()
      emp.set_employee_id(int(input(constants.enter_id)))
      emp.set_employee_title(input(constants.enter_title))
      emp.set_forename(input(constants.enter_forename))
      emp.set_surname(input(constants.enter_surname))
      emp.set_email(input(constants.enter_email))
      emp.set_salary(int(input(constants.enter_salary)))
      args = (emp.get_employee_id(), emp.get_employee_title(), emp.get_forename(), emp.get_surname(), emp.get_email(), emp.get_salary())
      self.cur.execute(constants.sql_insert, args)
      self.conn.commit()
      print(constants.data_added)
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  # Show all data
  def show_all(self):
    try:
      self.get_connection()
      print(pd.read_sql_query(constants.sql_select_all, self.conn))
    except Exception as e:
      print(e)
    finally:
      self.conn.close()
    
  # Search for data
  def search_data(self):
    try:
      self.get_connection()
      __choose_user = int(input(constants.enter_id))
      result = self.find_record(__choose_user)
      if type(result) == type(tuple()):
        for index, detail in enumerate(result):
          if index == 0:
            print("Employee ID: " + str(detail))
          elif index == 1:
            print("Employee Title: " + detail)
          elif index == 2:
            print("Employee Name: " + detail)
          elif index == 3:
            print("Employee Surname: " + detail)
          elif index == 4:
            print("Employee Email: " + detail)
          else:
            print("Salary: "+ str(detail))
      else:
        print ("No Record")
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  # Update data
  def update_data(self):
    try:
      self.get_connection()
      __choose_user = int(input(constants.enter_id_to_update))
      __choose_column = int(input(constants.column_update_command))
      __update_info = input(constants.update)
      __args = (__update_info, __choose_user)
    
      if __choose_column == 1:
        self.cur.execute(constants.sql_update_title_data, __args)
      elif __choose_column == 2:
        self.cur.execute(constants.sql_update_title_data, __args)
      elif __choose_column == 3:
        self.cur.execute(constants.sql_update_title_data, __args)
      elif __choose_column == 4:
        self.cur.execute(constants.sql_update_title_data, __args)
      elif __choose_column == 5:
        self.cur.execute(constants.sql_update_title_data, __args)

      self.conn.commit()
      print(constants.data_added)
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  # Delete data
  def delete_data(self):
    try:
      self.get_connection()
      __choose_user = int(input(constants.enter_id_to_delete))
      if self.find_record(__choose_user):
        self.cur.execute(constants.sql_delete_data, (__choose_user,))
        self.conn.commit()
        if self.find_record(__choose_user):
          print(constants.record_not_deleted)
        else:
          print(constants.record_deleted)
      else:
        print(constants.record_not_found)
    except Exception as e:
      print(e)
    finally: 
      self.conn.close()
  
  # Delete all data
  def delete_all(self):
    try:
      self.get_connection()
      self.cur.execute(constants.sql_delete_all_data)
      self.conn.commit()
    except Exception as e:
      print(e)
    finally: 
      self.conn.close()

  def find_record(self, emp_id):
    self.cur.execute(constants.sql_count_by_id, (emp_id,))
    return self.cur.fetchone()