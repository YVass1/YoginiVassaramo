import os
from source.User.navigation import try_again, confirm, num_selection
import source.User.navigation as nav
import source.Formatting.tables as tab
import source.User.commands as com
import source.Persistence.mysql_connection as db_connect
#functions

sql_db = db_connect.SQL_database()
def add_person(new_person):
    connection = sql_db.make_connection()
    try:
        with connection.cursor() as cursor:
            command = f'INSERT INTO users (Person_first_name) values("{new_person}") ON DUPLICATE KEY UPDATE Person_first_name = "{new_person}";'
            cursor.execute(command)
    except:
        print("ahhh error")
    finally:
        connection.close()

def remove_person(person):
    connection = sql_db.make_connection()
    try:
        with connection.cursor() as cursor:
            command = f'DELETE FROM users WHERE Person_first_name = "{person}";'
            cursor.execute(command)
            command2 =  f'DELETE FROM preferences WHERE user_name = "{person}";'
            cursor.execute(command2)
            print(f"{person} has been removed!")
    except:
        print("ahhh error")
    finally:
        connection.close()


def add_drink(new_drink):
    connection = sql_db.make_connection()
    try:
        with connection.cursor() as cursor:
            command = f'UPDATE preferences SET fav_drink = "{new_drink}" WHERE fav_drink = "{new_drink} (discontinued)";'
            command2 = f'INSERT INTO drinks (Drink_Name) values("{new_drink}") ON DUPLICATE KEY UPDATE Drink_Name = "{new_drink}";'
            cursor.execute(command)
            cursor.execute(command2)
            print(f'{new_drink} has been added to the drink selection!')
    except:
        print("ahhh error")
    finally:
        connection.close()


def remove_drink(drink):
    connection = sql_db.make_connection()
    try:
        with connection.cursor() as cursor:
            command = f'UPDATE preferences SET fav_drink = "{drink} (discontinued)" WHERE fav_drink = "{drink}";'
            command2 = f'DELETE FROM drinks WHERE Drink_Name = "{drink}";'
            cursor.execute(command)
            cursor.execute(command2)
    except:
        print("ahhh error")
    finally:
        connection.close()


def remove_pref(name):
    connection = sql_db.make_connection()
    try:
        with connection.cursor() as cursor:
            command = f'DELETE FROM preferences WHERE user_name = "{name}";'
            cursor.execute(command)
    except:
        print("ahhh error")
    finally:
        connection.close()

def add_pref(name,drink):
    connection = sql_db.make_connection()
    try:
        with connection.cursor() as cursor:
            command = f'INSERT INTO preferences (user_name, fav_drink) VALUES ("{name}","{drink}") ON DUPLICATE KEY UPDATE user_name  = "{name}", fav_drink = "{drink}";'
            cursor.execute(command)
            print(f'{drink} has been added as {name}\'s favourite drink!')
    except:
        print("ahhh error")
    finally:
        connection.close()


def add_round(owner, brewer, active_status):
    connection = sql_db.make_connection()
    try:
        with connection.cursor() as cursor:
            command = f'INSERT INTO rounds (owner,brewer,active_status) VALUES ("{owner}","{brewer}","{active_status}") ON DUPLICATE KEY UPDATE owner = "{owner}", brewer = "{brewer}", active_status = "{active_status}";'
            cursor.execute(command)
            print(f'A round has been created for {owner}!')
    except:
        print("ahhh error")
    finally:
        connection.close()

def add_order_to_round(round_num, owner, name,drink):
    connection = sql_db.make_connection()
    try:
        with connection.cursor() as cursor:
            command = f'INSERT INTO orders (round_id, name,drink) VALUES ({round_num},"{name}","{drink}");'
            cursor.execute(command)
            print(f'A new order of {drink} by {name} has been added to {owner}\'s round!')
    except:
        print("ahhh error")
    finally:
        connection.close()
    pass

def remove_round(owner, round_num):
    connection = sql_db.make_connection()
    try:
        with connection.cursor() as cursor:
            command = f'DELETE FROM rounds WHERE round_id = {round_num};'
            command2 = f'DELETE FROM orders WHERE round_id = {round_num};'
            cursor.execute(command)
            cursor.execute(command2)
            print(f'{owner}\'s round and history has been removed.')
    except:
        print("ahhh error")
    finally:
        connection.close()

def remove_order_from_round_db(owner, round_num, order_num):
    connection = sql_db.make_connection()
    try:
        with connection.cursor() as cursor:
            command = f'DELETE FROM orders WHERE round_id = {round_num} and order_id = {order_num};'
            cursor.execute(command)
            print(f'Order {order_num} in {owner}\'s round has been removed!')
    except:
        print("ahhh error")
    finally:
        connection.close()


def round_user_input(people_list):
    end_loop = False
    while not end_loop:
        try:
            os.system("clear")
            tab.print_table_list("Users", people_list)
            owner_name = input("Enter Round Owner's name: ").capitalize()
            if not owner_name or owner_name.isspace():
                print("You have entered nothing!")
                nav.try_again()
            elif any(num in owner_name for num in "0123456789"):
                print("No numbers can be included in name.")
                nav.try_again()
            elif owner_name not in people_list:
                print("Only an existing user can be the owner of a round.")
                nav.try_again()
            else:
                end_loop = True
                end_loop2 = False
                brewer_name =input("Enter Brewer's name: ").capitalize()
                if not brewer_name or brewer_name.isspace():
                    print("You have not entered anything!")
                    nav.try_again()
                elif any(num in brewer_name for num in "0123456789"):
                    print("No numbers can be included in name.")
                    nav.try_again()
                else:
                    end_loop2 = True
                    end_loop3 = False
                    active = input("""Enter a round active status.
[1] No or [2] Yes
Please enter a number: """)
                    if not active or active.isspace():
                        print("You have not entered anything!")
                        nav.try_again()
                    elif active.isnumeric() == True:
                        if 0 < int(active) < 3:
                            if int(active) == 1:
                                active = "No"
                            else:
                                active = "Yes"
                            confirmation = nav.confirm()
                            if confirmation:
                                com.add_round(owner_name, brewer_name, active)
                            else:
                                print("No changes have been made.")
                            end_loop3 = True
                        else:
                            print("You have not entered a valid number. Please enter a number between 1 or 2.")
                            nav.try_again()
                    else:
                        print("Please enter a number only.")
                        nav.try_again()
        except ValueError:
            print("No valid input.")
            nav.try_again()


def user_see_round_history(object_list):
    print("Here are all the rounds in our database.")
    end_loop = False
    while not end_loop:
        try:
            global round_id_list
            round_id_list = []
            for obj in object_list:
                round_id_list.append(obj.round_id)
            round_num = input("""Enter the round id number of the round's whose 
history you would like to see: """)
            if not round_num or round_num.isspace():
                print("You have not entered anything!")
                nav.try_again()
            elif round_num.isnumeric() == False:
                print("Please enter a number only.")
                nav.try_again()
            elif round_num not in round_id_list:
                print("Please enter round id number of an existing round.")
                nav.try_again()
            else:
                for obj in object_list:
                    if obj.round_id == round_num:
                        os.system("clear")
                        long_col1 = tab.long_col1_round_history(obj.round_history)
                        long_col2 = tab.long_col2_round_history(obj.round_history)
                        long_col3 = tab.long_col3_round_history(obj.round_history)
                        width = tab.round_history_table_width(f"{obj.owner}\'s round", "Order ID", "Name", "Drink", long_col1, long_col2, long_col3)
                        tab.print_round_history(obj.round_history, width, f"{obj.owner}\'s round", "Order ID", "Name", "Drink", long_col1, long_col2, long_col3)
                end_loop = True
        except ValueError:
            print("No valid input.")

def user_add_order_to_round(object_list, people_list, drinks_list):
    round_id_list = []
    for obj in object_list:
        round_id_list.append(obj.round_id)
    
    end_loop = False
    while not end_loop:
        round_num = input("Choose whose round would you like to add a new order to. Enter their round id: ")
        if not round_num or round_num.isspace():
            print("You have not entered anything!")
            nav.try_again()
        elif round_num.isnumeric() == False:
            print("Enter only a positive whole number.")
            nav.try_again()
        elif round_num not in round_id_list:
            print("Please enter a valid round id number.")
            nav.try_again()
        else:
            end_loop = True
            end_loop3 = False
            os.system("clear")
            owner = ""
            for obj in object_list:
                if obj.round_id == round_num:
                    owner = obj.owner
            print(f"Adding to {owner}\'s round. \n")
            tab.print_table_list("Users", people_list)
            print("Here are all the existing users: ")
            while not end_loop3:
                name = input("Enter the name of the person adding the order from existing users: ").capitalize()
                if not name or name.isspace():
                    print("You have not entered anything!")
                    nav.try_again()
                elif any(num in name for num in "0123456789") :
                    print("Names can not contain any numbers.")
                    nav.try_again()
                elif name not in people_list:
                    print("Sorry, only an existing user can add an order to a round.")
                    nav.try_again()
                else:
                    end_loop3 = True
                    end_loop = True
                    end_loop4 = False
                    os.system("clear")
                    for obj in object_list:
                            if obj.round_id == round_num:
                                long_col1 = tab.long_col1_round_history(obj.round_history)
                                long_col2 = tab.long_col2_round_history(obj.round_history)
                                long_col3 = tab.long_col3_round_history(obj.round_history)
                                width = tab.round_history_table_width(f"{obj.owner}\'s round", "Order ID", "Name", "Drink", long_col1, long_col2, long_col3)
                                tab.print_round_history(obj.round_history, width, f"{obj.owner}\'s round", "Order ID", "Name", "Drink", long_col1, long_col2, long_col3)
                                print(f"Here is {owner}\'s current round histroy.")
                                tab.print_table_list("Drinks", drinks_list)
                    print("Here are the available drinks.")
                    while not end_loop4:
                        drink = input("Choose a drink to add to the round: ").capitalize()
                        if not drink or drink.isspace():
                            print("You have not entered anything!")
                            nav.try_again()
                        elif any(num in drink for num in "0123456789"):
                            print("Drink names can not contain numbers.")
                            nav.try_again()
                        elif drink not in drinks_list:
                            print("Sorry this drink is not available. Please choose from the available drinks.")
                            nav.try_again()
                        else:
                            end_loop4 = True
                            end_loop3 = True
                            end_loop = True
                            os.system("clear")
                            print(f"Add {drink} order to {owner}\'s round?")
                            confirmation = nav.confirm()
                            if confirmation:
                                for obj in object_list:
                                    if obj.round_id == round_num:
                                        com.add_order_to_round(round_num,owner,name, drink)
                            else:
                                print("No changes have been made.")
                            end_loop = True
def remove_order_from_round(object_list):
    print("Here are all the rounds in our database.")
    end_loop = False
    while not end_loop:
        try:
            global round_id_list
            round_id_list = []
            for obj in object_list:
                round_id_list.append(obj.round_id)
            round_num = input("""Enter the round id number of the round, whose order history
 you would like to see and remove an order from: """)
            if not round_num or round_num.isspace():
                print("You have not entered anything!")
                nav.try_again()
            elif round_num.isnumeric() == False:
                print("Please enter a number only.")
                nav.try_again()
            elif round_num not in round_id_list:
                print("Please enter round id number of an existing round.")
                nav.try_again()
            else:
                for obj in object_list:
                    if obj.round_id == round_num:
                        global order_id_list
                        order_id_list = []
                        for order in obj.round_history:
                            order_id_list.append(order["OrderID"])
                        os.system("clear")
                        long_col1 = tab.long_col1_round_history(obj.round_history)
                        long_col2 = tab.long_col2_round_history(obj.round_history)
                        long_col3 = tab.long_col3_round_history(obj.round_history)
                        width = tab.round_history_table_width(f"{obj.owner}\'s round", "Order ID", "Name", "Drink", long_col1, long_col2, long_col3)
                        tab.print_round_history(obj.round_history, width, f"{obj.owner}\'s round", "Order ID", "Name", "Drink", long_col1, long_col2, long_col3)
                        order_num = input("Enter the order id number of the order you want to remove:  ")
                        if not order_num or order_num.isspace():
                            print("You have not entered anything!")
                            nav.try_again()
                        elif order_num.isnumeric() == False:
                            print("Please enter a number only.")
                            nav.try_again()
                        elif order_num not in order_id_list:
                            print("Please enter order id number of an existing order.")
                            nav.try_again()
                        else:
                            confirmation = nav.confirm()
                            if confirmation:
                                remove_order_from_round_db(obj.owner, round_num, order_num)
                            else:
                                print("No changes have been made.")
                            end_loop = True
        except ValueError:
            print("No valid input.")


def user_remove_round(object_list):
    print("Here are all the rounds in our database.")
    end_loop = False
    while not end_loop:
        try:
            global round_id_list
            round_id_list = []
            for obj in object_list:
                round_id_list.append(obj.round_id)
            round_num = input("""Enter the round id number of the round you want to remove: """)
            if not round_num or round_num.isspace():
                print("You have not entered anything!")
                nav.try_again()
            elif round_num.isnumeric() == False:
                print("Please enter a number only.")
                nav.try_again()
            elif round_num not in round_id_list:
                print("Please enter round id number of an existing round.")
                nav.try_again()
            else:
                for obj in object_list:
                    if obj.round_id == round_num:
                        confirmation = nav.confirm()
                        if confirmation:
                            com.remove_round(obj.owner, round_num)
                        else:
                            print("No changes have been made.")
                        end_loop = True
        except ValueError:
            print("No valid input.")
            
#***************************************************************************************************************************
#***************************************************************************************************************************
#***************************************************************************************************************************
#***************************************************************************************************************************


def add_to_dict(my_dict, my_key, my_value):
    my_dict[my_key.capitalize()] = my_value.capitalize()
    print(f"Your requested change has been completed. {my_value.capitalize()} has been added as {my_key.capitalize()}'s favourite drink.")
    return my_dict

def user_add_pref(my_list1, my_list2, my_dict):
    """ Appends to the specified dictionary, through user inputs, a chosen element from each list
as a key and value respectively. """
    end_loop = False
    while not end_loop: 
        try:
            tab.print_counter_var_table("Preferences", "id_number" ,"names", my_list1)   
            person_id = num_selection("""Here are the available people on our list.
Choose the person whose preference you want to change/add.
Enter their id number please: """)
            if 0 < person_id <= len(my_list1):
                try:
                    name = my_list1[person_id-1]
                    tab.print_counter_var_table("Available Drink Selection","Number","Drink", my_list2)
                    fav_drink_num = input(f"""Great! What is {name}\'s favourite drink? 
Select only from the available drinks menu. Enter a number: """)
                    if not fav_drink_num or fav_drink_num.isspace():
                        print("You have not entered anything!")
                        try_again()
                    elif fav_drink_num.isnumeric() == True:
                        if 0 < int(fav_drink_num) <= len(my_list2):
                            fav_drink = my_list2[int(fav_drink_num)-1]
                            print(f"""{fav_drink.capitalize()} will be added as {name.capitalize()}'s favourite drink! """)
                            confirmation = confirm()
                            if confirmation:
                                add_pref(name, fav_drink)
                            else:
                                print("No changes have been made.")
                                pass
                            end_loop = True
                        else:
                            print("Please enter a valid number.")
                            try_again()
                    else:
                        print(f"Please enter only a number.")
                        try_again()
                except ValueError:
                    print("Not a valid input!")
                    try_again()
            else:
                print("Not a valid id number.")
                try_again()
        except ValueError:
            print("You have not entered a number. Try again.")
            try_again()
    return my_dict

def remove_from_dict(my_dict, my_key):
    my_dict.pop(my_key.capitalize())
    print(f"Your requested change has been completed. {my_key.capitalize()}'s drink preference has been removed.")
    return my_dict

def user_remove_pref(my_dict):
    """Removes key:value pair, specified through user input, from specified dictionary."""
    tab.print_table_dict("Preferences", "names", "favourite drink", my_dict)  
    try:
        person_name = input("""Here are the available people on our list.
Choose the person whose preference you want to remove.
Enter their name please: """).capitalize()
        if not person_name or person_name.isspace():
            print("You have not entered in anything!")
        elif person_name not in my_dict.keys():
            print(f"{person_name} does not have a preference already.")  
        elif any(num in person_name for num in "01234567890"):
                    print(f"No numbers can be included. Try again.")
        elif person_name in my_dict.keys():
            print(f"""{person_name}'s drink preference will be removed.""")
            confirmation = confirm()
            if confirmation:
                remove_pref(person_name)
                print(f'{person_name}\'s preferences has been removed!')
            else:
                print("No changes have been made.")
                pass
    except ValueError:
        print("Not a valid input!")
        input("Enter any key to try again: ")
    return my_dict


def add_list_element(my_list, element):
    """Appends specified element to specified list,
IF the element is a string that contains only characters, and can not be
empty, have all the characters be spaces, contain any numbers or be already in the list. """
    if not element or element.isspace():
        print("You have not entered anything!")
    elif any(num in element for num in "0123456789"):
        print("No numbers can be included in the name.")
    elif element.capitalize() not in my_list:
        my_list.append(element.capitalize())
        print(f"Your choice: {element.capitalize()} was successfully added!")
    else:
        print("Already on the list. Try a different option.")
    return my_list

def remove_list_element(my_list, element):
    """Removes specified element from specified list,
IF the element is a string that contains only characters, and can not be
empty, have all the characters be spaces, contain any numbers or be already not in the list. """
    if not element or element.isspace():
        print("You have not entered anything!")
    elif any(num in element for num in "0123456789"):
        print("No numbers can be included in the name.")
    elif element.capitalize() in my_list:
            my_list.remove(element.capitalize())
            print(f"Your choice: {element.capitalize()} was successfully removed!")
    else:
        print(f"{element.capiltalize()} is not in the list already.")
    return my_list