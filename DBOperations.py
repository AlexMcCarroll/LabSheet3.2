import sqlite3
import pandas as pd
import constants as constants
from Employee import Employee

class DBOperations:
 
  def __init__(self):
    self.get_connection()

  def get_connection(self):
    self.conn = sqlite3.connect("mydb")
    self.cur = self.conn.cursor()

  # Drop table EmployeeUoB
  def drop_table(self):
    try:
      self.get_connection()
      self.conn.execute(constants.sql_drop_table)
      self.conn.commit()
      print(constants.table_dropped)
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  # Create Table
  def create_table(self):
    try:
      self.get_connection()
      self.cur.execute(constants.sql_create_table)
      self.conn.commit()
      print(constants.table_created)
    except Exception as e:
      if self._table_exists():
        print(constants.table_exists)
      else:
        print(e)
    finally:
      self.conn.close()

  # Insert Data
  def insert_data(self):
    try:
      if self._table_exists():
        self.get_connection()
        emp = Employee()
        _id = self._numeric_input(constants.enter_id)
        if self._search_data(_id) == False:
          emp.set_employee_id(_id)
          emp.set_employee_title(input(constants.enter_title))
          emp.set_forename(input(constants.enter_forename))
          emp.set_surname(input(constants.enter_surname))
          emp.set_email(input(constants.enter_email))
          emp.set_salary(self._numeric_input(constants.enter_salary))
          args = (emp.get_employee_id(), emp.get_employee_title(), emp.get_forename(), emp.get_surname(), emp.get_email(), emp.get_salary())
          self.cur.execute(constants.sql_insert, args)
          self.conn.commit()
          print(constants.data_added)
        else:
          print(constants.emp_id_exists)
      else:
        print(constants.table_not_exist)
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  # Show all data
  def show_all(self):
    try:
      if self._table_exists():
        self.get_connection()
        # Using Pandas to format table
        print(pd.read_sql_query(constants.sql_select_all, self.conn))
      else:
        print(constants.table_not_exist)
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  # Print data
  def print_data(self):
    try:
      if self._table_exists():
        self.get_connection()
        _id = self._numeric_input(constants.enter_id)
        _result = self._search_data(_id)
        if _result != False:
          for index, detail in enumerate(_result):
            if index == 0:
              print(constants.emp_id + str(detail))
            elif index == 1:
              print(constants.emp_title + detail)
            elif index == 2:
              print(constants.emp_forename + detail)
            elif index == 3:
              print(constants.emp_surname + detail)
            elif index == 4:
              print(constants.emp_email + detail)
            else:
              print(constants.emp_salary + str(detail))
        else:
          print (constants.record_not_found)
      else:
        print(constants.table_not_exist)
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  # Update data
  def update_data(self):
    try:
      if self._table_exists():
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
      else:
        print(constants.table_not_exist)
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  # Delete data
  def delete_data(self):
    try:
      if self._table_exists():
        self.get_connection()
        __choose_user = int(input(constants.enter_id_to_delete))
        if self._find_record(__choose_user):
          self.cur.execute(constants.sql_delete_data, (__choose_user,))
          self.conn.commit()
          if self._find_record(__choose_user):
            print(constants.record_not_deleted)
          else:
            print(constants.record_deleted)
        else:
          print(constants.record_not_found)
      else:
        print(constants.table_not_exist)
    except Exception as e:
      print(e)
    finally: 
      self.conn.close()
  
  # Delete all data
  def delete_all(self):
    try:
      if self._table_exists():
        self.get_connection()
        self.cur.execute(constants.sql_delete_all_data)
        self.conn.commit()
      else:
        print(constants.table_not_exist)
    except Exception as e:
      print(e)
    finally: 
      self.conn.close()

# Private methods

  # Check if EmployeeUoB table exists
  def _table_exists(self):
    try:
      self.get_connection()
      self.cur.execute(constants.sql_table_exists)
      _table = self.cur.fetchone()
      if _table[0] == 1:
        return True
      else:
        return False
      self.conn.commit()
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  # Find record with EmployeeID
  def _find_record(self, emp_id):
    self.cur.execute(constants.sql_count_by_id, (emp_id,))
    return self.cur.fetchone()

  # Search if data exists with EmployeeID
  def _search_data(self, id):
    _result = self._find_record(id)
    if type(_result) == type(tuple()):
      return _result
    else:
      return False
  
  # Check input is numeric
  def _numeric_input(self, constant):
    _arg = (input(constant))
    while _arg.isnumeric() == False:
      print(constants.entry_not_numeric)
      _arg = (input(constant))
    return int(_arg)
