
#functions for lists/dicts

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