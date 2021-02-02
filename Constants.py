# Strings
column_update_command = "\n Choose column to update:\n ********** \n 1.Title \n 2. Forename \n 3. Surname \n 4. Email \n 5. Salary \n Enter your choice: "
data_added = "Inserted data successfully"
enter_id = "Enter Employee ID: "
enter_id_to_update = "Enter EmployeeID of user to update: "
enter_id_to_delete = "Enter EmployeeID of user to delete: "
enter_title = "Enter Employee Title: "
enter_forename = "Enter Employee Forename: "
enter_surname = "Enter Employee Surname: "
enter_email = "Enter Employee Email: "
enter_salary = "Enter Employee Salary: "
record_not_deleted = "Record not deleted"
record_not_found = "Record not found"
record_deleted = "Record successfully deleted!"
table_created = "Table created successfully"
table_exists = "This table is already created"
update = "Update to: "

# Menu options
menu_header = "\n Menu \n **********"
menu_create_table = " 1. Create table EmployeeUoB"
menu_insert = " 2. Insert Employee data into table EmployeeUoB"
menu_show_all = " 3. Show all data in table EmployeeUoB"
menu_search = " 4. Search an employee by EmployeeID"
menu_update = " 5. Update Employee data by EmployeeID"
menu_delete = " 6. Delete Employee data by EmployeeID"
menu_delete_all = " 7. Delete all Employee data from table EmployeeUoB"
menu_exit = " 8. Exit\n"
menu_enter_choice = "Enter your choice: "

# SQL Commands
sql_drop_table = '''DROP TABLE EmployeeUoB'''
sql_create_table = '''CREATE TABLE EmployeeUoB (
      EmployeeID INTEGER,
      Title TEXT,
      Forename TEXT,
      Surname TEXT,
      Email TEXT,
      Salary INTEGER,
      PRIMARY KEY (EmployeeID)
    )'''
sql_insert = '''INSERT INTO EmployeeUoB (EmployeeID, Title, Forename, Surname, Email, Salary) VALUES (?, ?, ?, ?, ?, ?);'''

sql_select_all = "SELECT * FROM EmployeeUoB"
sql_select_by_id = "SELECT * FROM EmployeeUoB WHERE EmployeeID = ?"
sql_count_by_id = "SELECT * FROM EmployeeUoB WHERE EXISTS (SELECT 1 FROM EmployeeUoB WHERE EmployeeID = ?)"
sql_search = "select * from TableName where EmployeeID = ?"
sql_update_title_data = '''UPDATE EmployeeUoB SET Title = ? WHERE EmployeeID = ?'''
sql_update_forename_data = '''UPDATE EmployeeUoB SET Forename = ? WHERE EmployeeID = ?'''
sql_update_surname_data = '''UPDATE EmployeeUoB SET Surname = ? WHERE EmployeeID = ?'''
sql_update_email_data = '''UPDATE EmployeeUoB SET Email = ? WHERE EmployeeID = ?'''
sql_update_salary_data = '''UPDATE EmployeeUoB SET Salary = ? WHERE EmployeeID = ?'''
sql_delete_data = '''DELETE FROM EmployeeUoB WHERE EmployeeID = ?'''
sql_delete_all_data = '''DELETE FROM EmployeeUoB'''
sql_drop_table = ""

