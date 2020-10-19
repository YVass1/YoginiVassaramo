import os
import csv

#allows you to enter arguments on command line
#import sys
#arguments = sys.argv

#import
from source.Persistence.persistence_csv import  File_Store_list, File_store_dict
from source.Formatting.tables import print_counter_var_table, print_table_dict, print_table_list, print_menu_options
import source.Formatting.tables as tab
from source.User.navigation import num_selection, hold, confirm
from source.Data.data_store import  menu_options_filepath
import source.Classes.round_class as rd 
import source.Persistence.mysql_connection as db_connect
import source.Persistence.persistence_db as db_persist
import source.User.commands as com
cat = """
             .       .         
             \`-"'"-'/
              } ^ ^ {    
             =.  w  .=     ;)(;
               /^^^\  .   :----:
              /     \  ) C|====|
             (  )-(  )/   |    | 
              ""   ""     `----' 
  ___   __    __  ____  ____  _  _  ____  _   
 / __) /  \  /  \(    \(  _ \( \/ )(  __)/ \  
( (_ \(  O )(  O )) D ( ) _ ( )  /  ) _) \_/  
 \___/ \__/  \__/(____/(____/(__/  (____)(_)  
"""
#loading data
#user interaction section


def user_input():
    "User input interface for menu."
    
    end_loop =  False 
    while not end_loop:
        try :
            #loading data from database
            people_list, drinks_list, preferences, all_rounds_object_list = db_persist.load_data_from_sql()
            menu_options_file = File_Store_list(menu_options_filepath)
            menu_options_list = menu_options_file.load_into_list()

            os.system("clear")
            print_menu_options( menu_options_list)
            print("Welcome to BrewCo!")
            choice = num_selection("Select an option by entering a number: ")
            if choice == 2:
                os.system("clear")
                print_table_list("Users", people_list)
                hold()
            elif choice == 3:
                os.system("clear")
                print_table_list("Drinks", drinks_list)
                hold()
            elif choice ==7:
                os.system("clear")
                print("Add a new User?")
                confirmation = confirm()
                if confirmation:
                    os.system("clear")
                    print_table_list("Users", people_list)
                    person = input("""Here are the users currently in our database.
Please use an unique name. Enter a new user's name: """).capitalize()
                    confirmation = confirm()
                    if confirmation:
                        #people_list = add_list_element(people_list, person)
                        com.add_person(person)
                        print(f"{person} has been added as an user!")
                    else:
                        print("No changes have been made.")
                        pass
                else:
                    pass
                hold()
            elif choice == 12:
                os.system("clear")
                print("Remove an User?")
                confirmation = confirm()
                if confirmation:
                    os.system("clear")
                    print_counter_var_table("User database","id","name", people_list)
                    person_id = num_selection("""Here are the people in our database.
Note: Both the user and their preference (if one exists) will be removed.
Enter user's I.D. number to remove them: """)
                    if 0 < person_id <= len(people_list):
                        name = people_list[person_id-1]
                        print(f"{name} will be removed from the database.")
                        confirmation = confirm()
                        if confirmation:
                            com.remove_person(name)
                        else:
                            print("No changes have been made.")
                            pass
                    else:
                        print("Please enter a valid number. Try again.")
                else:
                    pass
                hold()
            elif choice ==8:
                os.system("clear")
                print("Add a new drink?")
                confirmation = confirm()
                if confirmation:
                    os.system("clear")
                    print_table_list("Drink Selection", drinks_list)
                    drink = input("""Here is the currently available drinks selection.
Enter a new drink option: """).capitalize()
                    confirmation = confirm()
                    if confirmation:
                       com.add_drink(drink)
                    else:
                        print("No changes have been made.")
                        pass
                else:
                    pass
                hold()
            elif choice == 13:
                os.system("clear")
                print("Remove a drink?")
                confirmation = confirm()
                if confirmation:
                    os.system("clear")
                    print_counter_var_table("Available Drinks Selection", "i.d.", "drink",drinks_list)
                    drink_id = num_selection("""Here are all the drinks available currently.
Enter the drink's I.D. number to remove it: """)
                    if 0 < drink_id <= len(drinks_list):
                        drink_name = drinks_list[drink_id-1]
                        print(f"{drink_name} will be removed from the database and no longer available.")
                        confirmation = confirm()
                        if confirmation:
                            com.remove_drink(drink_name)
                            print(f'{drink_name} has been removed from the drinks selection!')
                        else:
                            print("No changes have been made.")
                            pass
                    else:
                        print("Please enter a valid number. Try again.")
                else:
                    pass
                    pass
                hold()
            elif choice ==9:
                os.system("clear")
                print("Add a new User preference?")
                confirmation = confirm()
                if confirmation:
                    os.system("clear")
                    com.user_add_pref(people_list, drinks_list, preferences)
                else:
                    pass
                hold()
            elif choice == 14:
                os.system("clear")
                print("Remove an User preference?")
                confirmation = confirm()
                if confirmation:
                    os.system("clear")
                    com.user_remove_pref(preferences)
                else:
                    pass
                hold()
            elif choice == 4:
                os.system("clear")
                print_table_dict("User Preferences", "name", "favourite drink", preferences)
                hold()
            elif choice == 5:
                os.system("clear")
                longest_col1 = tab.long_col1(all_rounds_object_list)
                longest_col2 = tab.long_col2(all_rounds_object_list)
                longest_col3 = tab.long_col3(all_rounds_object_list)
                longest_col4 = tab.long_col4(all_rounds_object_list)
                width = tab.all_rounds_table_width("All Rounds","Round ID","Owner","Brewer","Active Status", longest_col1, longest_col2, longest_col3, longest_col4)
                tab.print_all_rounds_table(all_rounds_object_list,"All Rounds","Round ID","Owner","Brewer","Active Status", width, longest_col1, longest_col2, longest_col3, longest_col4)
                hold()
            elif choice == 10:
                os.system("clear")
                print("Begin a new round?")
                confirmation = confirm()
                if confirmation:
                    com.round_user_input(people_list)
                else:
                    pass
                hold()
            elif choice ==6:
                os.system("clear")
                print("See a round's order history?")
                confirmation = confirm()
                if confirmation:
                    os.system("clear")
                    longest_col1 = tab.long_col1(all_rounds_object_list)
                    longest_col2 = tab.long_col2(all_rounds_object_list)
                    longest_col3 = tab.long_col3(all_rounds_object_list)
                    longest_col4 = tab.long_col4(all_rounds_object_list)
                    width = tab.all_rounds_table_width("All Rounds","Round ID","Owner","Brewer","Active Status", longest_col1, longest_col2, longest_col3, longest_col4)
                    tab.print_all_rounds_table(all_rounds_object_list,"All Rounds","Round ID","Owner","Brewer","Active Status", width, longest_col1, longest_col2, longest_col3, longest_col4)
                    com.user_see_round_history( all_rounds_object_list)
                else:
                    pass
                hold()
            elif choice == 11:
                os.system("clear")
                print("Add an order to a round?")
                confirmation = confirm()
                if confirmation:
                    longest_col1 = tab.long_col1(all_rounds_object_list)
                    longest_col2 = tab.long_col2(all_rounds_object_list)
                    longest_col3 = tab.long_col3(all_rounds_object_list)
                    longest_col4 = tab.long_col4(all_rounds_object_list)
                    width = tab.all_rounds_table_width("All Rounds","Round ID","Owner","Brewer","Active Status", longest_col1, longest_col2, longest_col3, longest_col4)
                    tab.print_all_rounds_table(all_rounds_object_list,"All Rounds","Round ID","Owner","Brewer","Active Status", width, longest_col1, longest_col2, longest_col3, longest_col4)
                    com.user_add_order_to_round(all_rounds_object_list, people_list, drinks_list)
                else:
                    pass
                hold()
            elif choice == 15:
                os.system("clear")
                print("Remove a round?")
                confirmation = confirm()
                if confirmation:
                    os.system("clear")
                    longest_col1 = tab.long_col1(all_rounds_object_list)
                    longest_col2 = tab.long_col2(all_rounds_object_list)
                    longest_col3 = tab.long_col3(all_rounds_object_list)
                    longest_col4 = tab.long_col4(all_rounds_object_list)
                    width = tab.all_rounds_table_width("All Rounds","Round ID","Owner","Brewer","Active Status", longest_col1, longest_col2, longest_col3, longest_col4)
                    tab.print_all_rounds_table(all_rounds_object_list,"All Rounds","Round ID","Owner","Brewer","Active Status", width, longest_col1, longest_col2, longest_col3, longest_col4)
                    com.user_remove_round(all_rounds_object_list)
                else:
                    pass
                hold()
            elif choice ==16:
                os.system("clear")
                print("Remove an order from round?")
                confirmation = confirm()
                if confirmation:
                    os.system("clear")
                    longest_col1 = tab.long_col1(all_rounds_object_list)
                    longest_col2 = tab.long_col2(all_rounds_object_list)
                    longest_col3 = tab.long_col3(all_rounds_object_list)
                    longest_col4 = tab.long_col4(all_rounds_object_list)
                    width = tab.all_rounds_table_width("All Rounds","Round ID","Owner","Brewer","Active Status", longest_col1, longest_col2, longest_col3, longest_col4)
                    tab.print_all_rounds_table(all_rounds_object_list,"All Rounds","Round ID","Owner","Brewer","Active Status", width, longest_col1, longest_col2, longest_col3, longest_col4)
                    com.remove_order_from_round(all_rounds_object_list)                
                else:
                    pass
                hold()
            elif choice == 1:
                os.system("clear")
                print(f"Thanks for using the app!{cat}")
                end_loop = True #while loop termination condition or exit()
            elif choice > len(menu_options_list) or choice < 1: 
                print("Not a valid number. Try again")
                hold()
        except ValueError:
            print("Please enter a number. Try again")
            hold()

def main():
    user_input()

if __name__ =="__main__":
    main()
