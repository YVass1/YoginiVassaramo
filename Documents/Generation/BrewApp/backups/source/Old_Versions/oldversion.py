import sys
import os
import csv
#allows you to enter arguments on command line
arguments = sys.argv

#variables
additional_char= 2
intro = """ 
    Welcome to BrewCo!
    Choose an option by selecting a number
        
    [1] See All Users
    [2] See All Drinks
    [3] Add User
    [4] Remove User
    [5] Add Drink
    [6] Remove Drink 
    [7] Add User Preference
    [8] Remove User Preference
    [9] See Preferences 
    [0] Exit
"""
#functions
def loading_files(filepath):
    try: 
        with open(filepath, "r") as file_name:
            my_list = []
            myreader = csv.reader(file_name,quoting =csv.QUOTE_ALL)
            for row in myreader:
                for element in row:
                    my_list.append(element)
            print(my_list)
            return my_list
    except FileNotFoundError as e:
        print(f"File not found: " + str(e))
    except Exception as e:
        print("Error encountered: " + str(e))

def load_file_into_dict(filepath):
    try:
        with open(filepath, "r") as file_data:
            global preferences
            preferences = dict(filter(None, csv.reader(file_data, quoting = csv.QUOTE_ALL)))
            print(preferences)
            return preferences
    except FileNotFoundError as e:
        print(f"File not found: " + str(e))
    except Exception as e:
        print("Error encountered: " + str(e))

def save_list(filepath, my_list):
    try:    
        with open(filepath, "w") as file_data:
            writer = csv.writer(file_data, quoting = csv.QUOTE_ALL)
            for i in my_list:
                writer.writerow([i])
    except FileNotFoundError as e:
        print(f"File not found: " + str(e))
    except Exception as e:
        print("Error encountered: " + str(e))
            
def save_dict(filepath, my_dict):
    try:
        with open(filepath, "w") as file_data:
            writer = csv.writer(file_data, quoting = csv.QUOTE_ALL)
            for key,value in my_dict.items():
                writer.writerow([key,value])
    except FileNotFoundError as e:
        print(f"File not found: " + str(e))
    except Exception as e:
        print("Error encountered: " + str(e))

def table_width_1_col(heading, my_list):
    width = len(heading)
    limit = 30 + len(heading)
    for item in my_list:
        if limit > len(item) > width:
            width = len(item)
        elif len(item) >= limit: 
            my_list.remove(item)
            print(f"""{item} is too large for the menu.
It has been removed from menu.""")
    return width + additional_char

def line_divider(width):
    print( "+"+"="*width+"+")

def print_table_list(heading, my_list):
    width = table_width_1_col(heading, my_list)
    line_divider(width)
    #condition to check if heading is a string
    print("| " + heading.upper()+ " "*(width-1 - len(heading)) +"|") #uppercase heading
    line_divider(width)
    #if no menu items there or no menu heading
    for item in my_list:
        print(f"| {item.capitalize()}" + " "*(width-1 - len(item)) +"|")
    line_divider(width)

def num_selection(message):
    return int(input(f"{message}\n"))

def add_list_element(lists, *args):
    for element in args:
        if not element or element.isspace():
            print("You have not entered anything!")
        elif any(num in element for num in "0123456789"):
            print("No numbers can be included in the name.")
        elif element.capitalize() not in lists:
            lists.append(element.capitalize())
            print("Your choice was successfully added!")
        else:
            print("Already on the list. Try a different option.")
    return lists

def remove_list_element(my_list, element):
    if not element or element.isspace():
        print("You have not entered anything!")
    elif any(num in element for num in "0123456789"):
        print("No numbers can be included in the name.")
    elif element.capitalize() in my_list:
            my_list.remove(element.capitalize())
            print("Your choice was successfully removed!")
    else:
        print(f"There is no {element.capiltalize()} in the list already.")
    return my_list

def table_width_2_col(heading, sub_head1, sub_head2, my_list):
    width = len(heading) 
    sub_head_width = len(sub_head1) + len(sub_head2) + 3
    if width < sub_head_width:
        width = sub_head_width
    limit = 30 + width
    for value in my_list:
        if limit > len(value) + 4 + len(sub_head1) > width:
            width = len(value) + 4 + len(sub_head1)
        elif len(value) + 4 + len(sub_head1)>= limit: 
            my_dict.pop(value)
            print(f"""{value} is too large for the menu.
It has been removed from menu.""")
    return width + additional_char

def print_counter_var_table(heading, sub_head1, sub_head2, my_list):
    width = table_width_2_col(heading,sub_head1, sub_head2, my_list)
    line_divider(width)
    #condition to check if heading is a string
    print("|" + heading.upper().center(width) +  "|")
    line_divider(width)
    print(f"| {sub_head1.upper()} | " + f"{sub_head2.upper()}" + " "*(width -4 - len(sub_head1) - len(sub_head2) ) + "|")
    line_divider(width)
    counter = 1
    for counter, value in enumerate(my_list, counter):
        print(f"| {counter}" + " "*(len(sub_head1)-1) + f" | {value.capitalize()}" + " "*(width -4 -len(sub_head1) - len(value)) + "|")
    line_divider(width)
   
def try_again():
    input("Enter any key to try again: ")

def user_add_pref(my_list):
    end_loop = False
    while not end_loop > 0: 
        print_counter_var_table("Preferences", "id_number" ,"names", my_list)   
        try:
            person_id = num_selection("""Here are the available people on our list.
Choose the person whose preference you want to change/add.
Enter their id number please: """)
            if person_id > len(my_list):# TODO: width to people list.
                print("Not a valid id number.")
                try_again()
            else:
                try:
                    name = my_list[person_id-1]
                    fav_drink = input("What is their favourite drink? ")
                    fav_drink = fav_drink.capitalize()
                    if not fav_drink or fav_drink.isspace():
                        print("You have not entered anything!")
                        try_again()
                    elif any(num in fav_drink for num in "01234567890"):
                        print(f"No numbers can be included.")
                        try_again()
                    else:
                        preferences[name] = fav_drink.capitalize()
                        #save_dict("preferences.csv", preferences)
                        print(f"Your requested change has been completed. {fav_drink} has been added.")
                        end_loop = True
                except ValueError:
                    print("Not a valid input!")
                    try_again()
        except ValueError:
            print(" You have not entered a number. Try again.")
            try_again()
    return preferences

def user_remove_pref(preferences):
    #end_loop = False
   # while not end_loop > 0: 
    fav_drink_table("Preferences", "names", "favourite drink", preferences)  
    try:
        person_name = input("""Here are the available people on our list.
Choose the person whose preference you want to remove.
Enter their name please: """)
        if not person_name or person_name.isspace():
            print("You have not entered in anything!")
        elif person_name not in preferences.keys():
            print(f"{person_name} does not have a preference already.")  
        elif any(num in person_name for num in "01234567890"):
                    print(f"No numbers can be included. Try again.")
        elif person_name in preferences.keys():
            preferences.pop(person_name)
            #save_dict("preferences.csv", preferences)
            print(f"Your requested change has been completed. {person_name} has been removed.")
                #end_loop = True
    except ValueError:
        print("Not a valid input!")
        input("Enter any key to try again: ")
    return preferences

def fav_drink_table(heading, sub_head1, sub_head2, lists):
    width = len(heading)
    longest_col1 = len(sub_head1)
    longest_col2 = len(sub_head2)
    for key,value in lists.items():
        if len(key) > longest_col1:
            longest_col1 = len(key)
        if len(value) == None:
            pass
        elif len(value)> longest_col2:
            longest_col2 = len(value)
    width = longest_col2 + longest_col1 + additional_char + 3
    line_divider(width)
    print("|" + heading.upper().center(width) + "|")
    line_divider(width)
    print(f"| {sub_head1.upper()}" + " "*(longest_col1- len(sub_head1)) + " | " +
    f"{sub_head2.upper()}" + " "*(width - longest_col1 -4 - len(sub_head2)) + "|")
    line_divider(width)
    counter = 1
    for counter, (key,value) in enumerate(lists.items(), counter):
        print(f"| {key}" + " "*(longest_col1-len(key)) + f" | {value.capitalize()}" +
        " "*(width - longest_col1 -4 - len(value)) + "|")
    line_divider(width)

def hold():
    input("Enter any key to return to main menu: ")


#loading data
people_list = loading_files("people_list.csv")
drinks_list = loading_files("drinks_list.csv")
load_file_into_dict("preferences.csv")

#user interaction section

end_loop =  False 
while not end_loop:
    try :
        print(intro)
        choice = num_selection("Enter a number: ")
        if choice == 1:
            os.system("clear")
            print_table_list("People", people_list)
            hold()
        elif choice == 2:
            os.system("clear")
            print_table_list("Drinks", drinks_list)
            hold()
        elif choice ==3:
            print_table_list("People", people_list)
            person = input("Enter a new person name: ")
            people_list = add_list_element(people_list, person)
            #save_list("people_list.txt",people_list)
            hold()
        elif choice == 4:
            os.system("clear")
            print_table_list("People", people_list)
            name = input("""Here are the people in our database.
Enter whose name do you want to remove: """)
            people_list = remove_list_element(people_list, name)
            #save_list("people_list.txt", people_list)
            if name in preferences.keys():
                preferences.pop(name)
            else:
                pass
            #save_dict("preferences.csv", preferences)
            hold()
        elif choice ==5:
            os.system("clear")
            print_table_list("Drinks", drinks_list)
            drink = input("Enter a new drink: ")
            drinks_list = add_list_element(drinks_list, drink)
            #save_list("drinks_list.txt", drinks_list)
            hold()
        elif choice == 6:
            os.system("clear")
            print_table_list("Drinks", drinks_list)
            drink = input("""Here are the drinks in our database.
Enter which drink do you want to remove: """)
            drinks_list = remove_list_element(drinks_list, drink)
            #save_list("drinks_list.txt", drinks_list)
            hold()
        elif choice ==7:
            os.system("clear")
            preferences = user_add_pref(people_list)
            hold()
        elif choice == 8:
            os.system("clear")
            user_remove_pref(preferences)
            fav_drink_table("Preferences", "names", "favourite drink", preferences)
            hold()
        elif choice == 9:
            os.system("clear")
            fav_drink_table("Preferences", "names", "favourite drink", preferences)
            hold()
        elif choice == 0:
            save_list("drinks_list.csv", drinks_list)
            save_list("people_list.csv", people_list)
            save_dict("preferences.csv", preferences)
            print("Thanks for using the app!")
            end_loop = True #while loop termination condition or exit()
        elif choice > 9 : 
            print("Not a valid number. Try again")
            input("Enter any key to return to main menu: ")
    except ValueError:
        print("Please enter a number. Try again")
        input("Enter any key to return to main menu: ")
        


'''
class Drink:
    def __init__(self, name, drink_type):
        self.name = name
        self.drink_type =drink_type

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age =age

'''
'''
class Order:
    def __init__(self, table_num):
        self.table_num = table_num
        #self.order_id = order_id
        self.active = "yes"
        self.order = {}

class Order_Manager(Order):
    def __init__(self, table_num, preferences):
        super().__init__(table_num)
        self.preferences = preferences
    def add_to_order(self):
        for self.person, self.drink in self.preferences.items():
            self.order[self.person] = self.drink
    def total_order(self):#order_id as an argument
        print(self.order)
        #print order 
        #print total cost so far

preferences = {"Joe":"Yorkshire tea", "Kate": "coffee", "Tim": "Water"}

person = Order_Manager("001", preferences)
person.add_to_order()
person.total_order()


class PeopleManger:
    def __init__(self, filename):
        self.filename = filename
        self.people_list = []

    def load_data(self):
        try:
            with open(self.filename, "r") as people_data:
                for line in people_data.readlines():
                    self.people_list.append(line.rstrip('\n'))
            return self.people_list
        except:
            print("No data loaded. ERROR. ")

    def add_person(self, name):
        self.people_list.append(self.name)

    def remove_person(self, name):
        self.people_list.pop(self.name)


my_people = PeopleManger("people_list.txt")
print(my_people.load_data())
'''
