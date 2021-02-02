from DBOperations import DBOperations
import Constants as constants

# The main function will parse arguments. 
# These argument will be definded by the users on the console.
# The user will select a choice from the menu to interact with the database.

while True:
  print (constants.menu_header)
  print (constants.menu_create_table)
  print (constants.menu_insert)
  print (constants.menu_show_all)
  print (constants.menu_search)
  print (constants.menu_update)
  print (constants.menu_delete)
  print (constants.menu_delete_all)
  print (constants.menu_exit)

  _db_ops = DBOperations()
  _choose_menu = int(input(constants.menu_enter_choice))
  if _choose_menu == 1:
    _db_ops.create_table()
  elif _choose_menu == 2:
    _db_ops.insert_data()
  elif _choose_menu == 3:
    _db_ops.show_all()
  elif _choose_menu == 4:
    _db_ops.search_data()
  elif _choose_menu == 5:
    _db_ops.update_data()
  elif _choose_menu == 6:
    _db_ops.delete_data()
  elif _choose_menu == 7:
    _db_ops.delete_all()
  elif _choose_menu == 8:
    exit(0)
  else:
    print ("Invalid Choice")


