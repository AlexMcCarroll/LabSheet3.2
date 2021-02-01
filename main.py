from DBOperations import DBOperations

# The main function will parse arguments. 
# These argument will be definded by the users on the console.
# The user will select a choice from the menu to interact with the database.

db_ops = DBOperations()
db_ops.drop_table()

while True:
  print ("\n Menu:")
  print ("**********")
  print (" 1. Create table EmployeeUoB")
  print (" 2. Insert Employee data into EmployeeUoB")
  print (" 3. Show all data in EmployeeUoB")
  print (" 4. Search an employee")
  print (" 5. Update Employee data")
  print (" 6. Delete Employee data")
  print (" 7. Delete all Employee data")
  print (" 8. Exit\n")

  __choose_menu = int(input("Enter your choice: "))
  if __choose_menu == 1:
    db_ops.create_table()
  elif __choose_menu == 2:
    db_ops.insert_data()
  elif __choose_menu == 3:
    db_ops.show_all()
  elif __choose_menu == 4:
    db_ops.search_data()
  elif __choose_menu == 5:
    db_ops.update_data()
  elif __choose_menu == 6:
    db_ops.delete_data()
  elif __choose_menu == 7:
    db_ops.delete_all()
  elif __choose_menu == 8:
    exit(0)
  else:
    print ("Invalid Choice")


