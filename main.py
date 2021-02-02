from DBOperations import DBOperations
import constants as constants

# main.py will handle the menu and user input

while True:
  print (constants.menu_header)
  print (constants.menu_create_table)
  print (constants.menu_insert)
  print (constants.menu_show_all)
  print (constants.menu_search)
  print (constants.menu_update)
  print (constants.menu_delete)
  print (constants.menu_delete_all)
  print (constants.menu_drop_table)
  print (constants.menu_exit)

  _db_ops = DBOperations()
  _choose_menu = input(constants.menu_enter_choice)

  if _choose_menu.isnumeric():
    _choose_menu = int(_choose_menu)
    if _choose_menu == 1:
      _db_ops.create_table()
    elif _choose_menu == 2:
      _db_ops.insert_data()
    elif _choose_menu == 3:
      _db_ops.show_all()
    elif _choose_menu == 4:
      _db_ops.print_data()
    elif _choose_menu == 5:
      _db_ops.update_data()
    elif _choose_menu == 6:
      _db_ops.delete_data()
    elif _choose_menu == 7:
      _db_ops.delete_all()
    elif _choose_menu == 8:
      _db_ops.drop_table()
    elif _choose_menu == 9:
      exit(0)
    else:
      print (constants.menu_invalid)
  else:
   print(constants.menu_invalid)