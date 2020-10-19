import os
import csv
#allows you to enter arguments on command line
#import sys
#arguments = sys.argv

#import data file containing data file path
#load_file_into_list ,load_file_into_dict, save_dict, save_list,
#import functions
from source.Persistence.persistence import  File_Store, File_store_dict
from source.Formatting.tables import print_counter_var_table, print_table_dict, print_table_list, print_menu_options
from source.User.commands import add_list_element, remove_list_element,user_add_pref, user_remove_pref
from source.User.navigation import num_selection, hold, confirm
from source.Data.data_store import drinks_filepath, people_filepath, preferences_filepath, menu_options_filepath, round_filepath, round_hist_filepath
import source.round as rd 
import source.Persistence.sql_connection as sql
#import File_store_round, print_all_rounds_table
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
    #loading data from database
    sql.load_data_from_sql()
    people_list = sql.people_list
    drinks_list = sql.drinks_list

    #loading from CSV files using ClASS FUNCTIONS
    drinks_file = File_Store(drinks_filepath)
    #drinks_list = drinks_file.load_into_list()
    
    people_file = File_Store(people_filepath)
    #people_list = people_file.load_into_list()

    preferences_file = File_store_dict(preferences_filepath)
    preferences = preferences_file.load_into_dict()

    menu_options_file = File_Store(menu_options_filepath)
    menu_options_list = menu_options_file.load_into_list()

    round_file = rd.File_store_round(round_filepath)
    all_rounds_list = round_file.load_file_to_dict_round()

    end_loop =  False 
    while not end_loop:
        try :
            os.system("clear")
            print_counter_var_table("BrewCo Options Menu :)","number","options", menu_options_list)
            print(" Welcome to BrewCo!")
            choice = num_selection("Select an option by entering a number: ")
            if choice == 2:
                os.system("clear")
                print_table_list("Users", people_list)
                hold()
            elif choice == 3:
                os.system("clear")
                print_table_list("Drinks", drinks_list)
                hold()
            elif choice ==6:
                os.system("clear")
                print("Add a new User?")
                confirmation = confirm()
                if confirmation:
                    os.system("clear")
                    print_table_list("Users", people_list)
                    person = input("""Here are the users currently in our database.
Please use an unique name. Enter a new user's name: """)
                    confirmation = confirm()
                    if confirmation:
                        people_list = add_list_element(people_list, person)
                    else:
                        print("No changes have been made.")
                        pass
                else:
                    pass
                hold()
            elif choice == 10:
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
                            people_list = remove_list_element(people_list, name)
                            if name in preferences.keys():
                                preferences.pop(name)
                            else:
                                pass
                        else:
                            print("No changes have been made.")
                            pass
                    else:
                        print("Please enter a valid number. Try again.")
                else:
                    pass
                hold()
            elif choice ==7:
                os.system("clear")
                print("Add a new drink?")
                confirmation = confirm()
                if confirmation:
                    os.system("clear")
                    print_table_list("Drink Selection", drinks_list)
                    drink = input("""Here is the currently available drinks selection.
Enter a new drink option: """)
                    confirmation = confirm()
                    if confirmation:
                       drinks_list = add_list_element(drinks_list, drink)
                       for key,value in preferences.items():
                            if drink + " (discontinued)" == value:
                                preferences[key] = drink
                            else:
                                pass
                    else:
                        print("No changes have been made.")
                        pass
                else:
                    pass
                hold()
            elif choice == 11:
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
                            drinks_list = remove_list_element(drinks_list, drink_name)
                            for name, drink in preferences.items():
                                if drink_name == drink :
                                    preferences[name] = drink + " (discontinued)"
                                else:
                                    pass
                        else:
                            print("No changes have been made.")
                            pass
                    else:
                        print("Please enter a valid number. Try again.")
                else:
                    pass
                    pass
                hold()
            elif choice ==8:
                os.system("clear")
                print("Add a new User preference?")
                confirmation = confirm()
                if confirmation:
                    os.system("clear")
                    preferences = user_add_pref(people_list, drinks_list, preferences)
                else:
                    pass
                hold()
            elif choice == 12:
                os.system("clear")
                print("Remove an User preference?")
                confirmation = confirm()
                if confirmation:
                    os.system("clear")
                    user_remove_pref(preferences)
                else:
                    pass
                hold()
            elif choice == 4:
                os.system("clear")
                print_table_dict("User Preferences", "name", "favourite drink", preferences)
                hold()
            elif choice == 5:
                os.system("clear")
                rd.print_all_rounds_table(all_rounds_list,"All Rounds","Round ID","Owner","Brewer","Active Status")
                hold()
            elif choice == 9:
                os.system("clear")
                print("Begin a new round?")
                confirmation = confirm()
                if confirmation:
                    all_rounds_list = rd.round_user_input(people_list)
                else:
                    pass
                hold()
            elif choice == 1:
                drinks_file.save_list_to_file(drinks_list)
                people_file.save_list_to_file(people_list)
                preferences_file.save_dict_to_file(preferences)
                round_file.save_all_rounds_to_file(all_rounds_list)
                
                drinks_file = File_Store(drinks_filepath)
                people_file = File_Store(people_filepath)
                drinks_file.save_list_to_file(drinks_list)
                people_file.save_list_to_file(people_list)
                sql.load_from_csv_to_sql()
                
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


#user inputs for creating round and inserting round
#printing all rounds table
#print single round afterwards and when adding round