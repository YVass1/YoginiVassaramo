import csv
import os
from source.Data.data_store import round_filepath, round_hist_filepath
import source.User.navigation as nav
import source.Persistence.sql_connection as sql
import source.Formatting.tables as tab

#CONSTANTS
round_fieldnames = ["RoundID","Owner","Brewer","ActiveStatus"]
round_hist_fieldnames = ["RoundID","OrderID","Name","Drink"]


#creating Round class here
class Round_Handler:
    #print round history function
    #print a round and all the drinks on it function
    #add to round function
    #create round - add to all_rounds
    
    def __init__(self,round_id, owner, brewer ,active_status):
        self.round_id = round_id
        self.brewer = brewer
        self.owner = owner
        self.active_status = active_status
        self.round_history = []

    def add_to_round(self,order_id,name,drink):
        self.round_history.append({"RoundID": self.round_id,"OrderID":order_id,"Name": name, "Drink": drink})
        #used with user_input function that chooses round id , and then adds order id if not already there and drink and name from lists only

#Takes existing rounds from csv file(path) to make list of OBJECTS
#where each object is a round

class File_store_round:
    def __init__(self, filepath):
        self.filepath = filepath
    def load_file_to_dict_round(self):
        with open(self.filepath, "r") as round_file:
            myreader = csv.DictReader(round_file,quoting =csv.QUOTE_ALL)
            all_rounds_list = []
            all_rounds_object_list =[]
            for row in myreader:
                if not row:
                    pass
                else:
                    all_rounds_list.append(row)

            for my_dict in all_rounds_list:
                round_id = my_dict[round_fieldnames[0]]
                owner_name = my_dict[round_fieldnames[1]]
                brewer_name = my_dict[round_fieldnames[2]]
                active = my_dict[round_fieldnames[3]]
                owner_name = Round_Handler(round_id, owner_name, brewer_name, active)
                all_rounds_object_list.append(owner_name)
        return all_rounds_object_list


    def save_object_list_to_file(self, object_dict_list):
        with open(self.filepath, "w", newline="") as round_file:
            writer = csv.writer(round_file)
            writer.writerow(round_fieldnames)
            for obj in object_dict_list:
                writer.writerow([obj.round_id, obj.owner,obj.brewer,obj.active_status])

class File_store_round_history:
    def __init__(self, filepath):
        self.filepath = filepath
    def load_file_to_object(self, object_list):
        with open(self.filepath, "r") as round_hist_file:
            myreader = csv.DictReader(round_hist_file,quoting =csv.QUOTE_ALL)
            all_orders_list = []
            for row in myreader:
                if not row:
                    pass
                else:
                    all_orders_list.append(row)

            for obj in object_list:
                for my_dict in all_orders_list:
                    if my_dict["RoundID"] == obj.round_id:
                        obj.round_history.append(my_dict)
        return obj.round_history

    def save_round_history_to_file(self, object_list):
        with open(self.filepath, "w", newline="") as round_hist_file:
            writer = csv.writer(round_hist_file)
            writer.writerow(round_hist_fieldnames)
            for obj in  object_list:
                for my_dict in obj.round_history:
                    writer.writerow([my_dict["RoundID"], my_dict["OrderID"],my_dict["Name"], my_dict["Drink"]])

        


#creates a new round object using user input and to all_rounds_object_list
def round_user_input(people_list, object_list):
    end_loop = False
    while not end_loop:
        try:
            os.system("clear")
            global round_id_list
            round_id_list = []
            for obj in object_list:
                round_id_list.append(obj.round_id)

            round_num = input("Enter a new Round ID number: ")
            #check if num already in all rounds
            if not round_num or round_num.isspace():
                print("You have not entered anything!")
                nav.try_again()
            elif round_num.isnumeric() == False:
                print("Please enter a number only.")
                nav.try_again()
            elif round_num in round_id_list:
                print("Round ID number already has been assigned.")
                nav.try_again()
            else:
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
                    #add can only be from user table constraint 
                    brewer_name =input("Enter Brewer's name: ").capitalize()
                    #anyone right now
                    active = input("Enter a round active status, Yes or No: ").capitalize()
                    #activation constraint of must be yes or no
                    confirmation = nav.confirm()
                    if confirmation:
                        owner_name = Round_Handler(round_num, owner_name, brewer_name, active)
                        object_list.append(owner_name)
                        print(f"{owner_name.owner}\'s new round has been successfully created!")
                    else:
                        print("No changes have been made.")
                        pass
                    end_loop = True
        except ValueError:
            print("No valid input.")
            nav.try_again()
    return object_list



#***************************************************************************************************************************
#***************************************************************************************************************************
#***************************************************************************************************************************
#***************************************************************************************************************************

additional_char = 2

def line_divider(width):
    "Prints line of specified width."
    print( "+"+"="*width+"+")

def longest_word(sub_heading, col_list):
    longest_word = len(sub_heading)
    for item in col_list:
        if len(item) > longest_word:
            longest_word = len(item)
    return longest_word

def long_col1(all_rounds_object_list):
    col_list1 = [obj.round_id for obj in all_rounds_object_list]
    longest_col1 = longest_word("Round ID", col_list1)
    return longest_col1

def long_col2(all_rounds_object_list):
    col_list2 = [obj.owner for obj in all_rounds_object_list]
    longest_col2 = longest_word("Round ID", col_list2)
    return longest_col2

def long_col3(all_rounds_object_list):
    col_list3 = [obj.brewer for obj in all_rounds_object_list]
    longest_col3 = longest_word("Brewer", col_list3)
    return longest_col3

def long_col4(all_rounds_object_list):
    col_list4 = [obj.active_status for obj in all_rounds_object_list]
    longest_col4 = longest_word("Active Status", col_list4)
    return longest_col4


def all_rounds_table_width(heading, sub_head1, sub_head2, sub_head3, sub_head4, longest_col1,longest_col2, longest_col3, longest_col4):
    width = len(heading) 
    sub_head_width = len(sub_head1) + len(sub_head2) + len(sub_head3)+ len(sub_head4)+ 3*3
    if width < sub_head_width:
        width = sub_head_width
    if longest_col1 + longest_col2 + longest_col3 + longest_col4 + 3*3 > width:
        width = longest_col1 + longest_col2 + longest_col3 + longest_col4 + 3*3
    return width + additional_char

def print_all_rounds_table(object_list, heading, sub_head1, sub_head2, sub_head3, sub_head4, width, longest_col1, longest_col2, longest_col3, longest_col4):
    
    line_divider(width)
    print("|" + heading.upper().center(width) + "|")
    line_divider(width)
    print(f"|{sub_head1.upper().center(longest_col1+2)}" + "|" +
    f"{sub_head2.upper().center(longest_col2+2)}"+ "|" +
    f"{sub_head3.upper().center(longest_col3+2)}"+ "|" +
    f"{sub_head4.upper().center(longest_col4+2)}"
    + "|")
    line_divider(width)
    for obj in object_list:
        print(f"| " + obj.round_id.center(longest_col1) +
         " |" + obj.owner.center(longest_col2+2)
         + "|" + obj.brewer.center(longest_col3+2)
         + "|" + obj.active_status.center(longest_col4 +2)
         + "|")
    line_divider(width)



def long_col1_round_history(round_history_list):
    col_list1 = [my_dict["OrderID"] for my_dict in round_history_list]
    longest_col1 = longest_word("Order ID", col_list1)
    return longest_col1

def long_col2_round_history(round_history_list):
    col_list2 = [my_dict["Name"] for my_dict in round_history_list]
    longest_col2 = longest_word("Name", col_list2)
    return longest_col2

def long_col3_round_history(round_history_list):
    col_list3 = [my_dict["Drink"] for my_dict in round_history_list]
    longest_col3 = longest_word("Drink", col_list3)
    return longest_col3

def round_history_table_width(heading, sub_head1, sub_head2, sub_head3, longest_col1,longest_col2, longest_col3):
    width = len(heading) 
    sub_head_width = len(sub_head1) + len(sub_head2) + len(sub_head3)+ 3*2
    if width < sub_head_width:
        width = sub_head_width
    if longest_col1 + longest_col2 + longest_col3 + 3*2 > width:
        width = longest_col1 + longest_col2 + longest_col3  + 3*2
    return width + additional_char

def print_round_history(round_history_list, width, heading, sub_head1, sub_head2, sub_head3, long_col1, long_col2, long_col3):
    line_divider(width)
    print("|" + heading.upper().center(width) + "|")
    line_divider(width)
    print(f"|{sub_head1.upper().center(long_col1+2)}" + "|" +
    f"{sub_head2.upper().center(long_col2+2)}"+ "|" +
    f"{sub_head3.upper().center(long_col3+2)}"+ "|")
    line_divider(width)
    for my_dict in round_history_list:
        print(f"| " + my_dict["OrderID"].center(long_col1) +
        " |" + my_dict["Name"].center(long_col2+2)
        + "|" + my_dict["Drink"].center(long_col3+2)
        + "|")
    line_divider(width)

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
                        long_col1 = long_col1_round_history(obj.round_history)
                        long_col2 = long_col2_round_history(obj.round_history)
                        long_col3 = long_col3_round_history(obj.round_history)
                        width = round_history_table_width(f"{obj.owner}\'s round", "Order ID", "Name", "Drink", long_col1, long_col2, long_col3)
                        print_round_history(obj.round_history, width, f"{obj.owner}\'s round", "Order ID", "Name", "Drink", long_col1, long_col2, long_col3)
                end_loop = True
        except ValueError:
            print("No valid input.")
    

#printing out all rounds table +  single round table
#***************************************************************************************************************************
#***************************************************************************************************************************
#***************************************************************************************************************************
#***************************************************************************************************************************

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
            owner = ""
            for obj in object_list:
                if obj.round_id == round_num:
                    owner = obj.owner
                    order_id_list = []
                    for my_order in obj.round_history:
                        order_id_list.append(my_order["OrderID"])
            end_loop = True
            end_loop2 = False
            os.system("clear")
            for obj in object_list:
                    if obj.round_id == round_num:
                        long_col1 = long_col1_round_history(obj.round_history)
                        long_col2 = long_col2_round_history(obj.round_history)
                        long_col3 = long_col3_round_history(obj.round_history)
                        width = round_history_table_width(f"{obj.owner}\'s round", "Order ID", "Name", "Drink", long_col1, long_col2, long_col3)
                        print_round_history(obj.round_history, width, f"{obj.owner}\'s round", "Order ID", "Name", "Drink", long_col1, long_col2, long_col3)  
            while not end_loop2:
                order_id = input("To add a new order, enter a new order id: ")
                if not order_id or order_id.isspace():
                    print("You have not entered anything!")
                    nav.try_again()
                elif order_id.isnumeric() == False:
                    print("Enter only a positive whole number.")
                    nav.try_again()
                elif int(order_id) < 1:
                    print("Please choose a positive whole number for order id.")
                    nav.try_again()
                elif isinstance(int(order_id), float) == True:
                    print("Please choose only a whole number for order id.")
                    nav.try_again()
                elif order_id in order_id_list:
                    print("Order id number already assigned. Please choose another id number.")
                    nav.try_again()
                else:
                    end_loop2 =True
                    end_loop = True
                    end_loop3 = False
                    os.system("clear")
                    tab.print_table_list("Users", people_list)
                    print("Here all the existing users.")
                    while not end_loop3:
                        name = input("Enter the name of the person adding the order: ").capitalize()
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
                            end_loop2 = True
                            end_loop = True
                            end_loop4 = False
                            os.system("clear")
                            tab.print_table_list("Drinks", drinks_list)
                            print("Here are all the drinks that are available.")
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
                                    end_loop2 = True
                                    end_loop = True
                                    os.system("clear")
                                    print(f"Add {drink} order to {owner}\'s round?")
                                    confirmation = nav.confirm()
                                    if confirmation:
                                        for obj in object_list:
                                            if obj.round_id == round_num:
                                                #add to orders table so order id created there
                                                obj.add_to_round(order_id,name, drink)
                                                print(f"The order has been added to {obj.owner}\'s round!")
                                    else:
                                        print("No changes have been made.")
                                    end_loop = True


#NEXT: #create add to round class function

#function that grabs round id, all name/drinks, owner name so we can print in 
# single round tables
#create print menu functions for them
#add to round option + so first see/print a single round_history
#drink can only be chosen from drinks list and people from users
#drink cant be discontinued
#option to add someone's fav drink drink
#print/see single round menu function (count drinks) + add as menu option
#delete rounds and round_history
#sorts according to active status maybe?


#TO DO LIST:
#create csv files/ save and load function for adding to rounds info
#add to round function in class + constraint of who and which drink
#create functions to print menus, of single round
#add to menu option : add to round + user inputs
#unit testing


#makes a round but what if no drinks added :deal with this when printing menu for single rounds
#check if brewer name, owner name, name , drink are not unique
#file empty exceptions

"""
RoundID,Owner,Brewer,ActiveStatus
1,Aria,Khalid,Yes
2,John,Khalid,Yes
3,John,Joe,Yes
4,Suman,Joe,Yes
5,Joe,Will,No
6,Maria,Will,Yes


RoundID,OrderID,Name,Drink
1,1,"Aria","Tea"
1,2,"Aria","Tea"
1,3,"Joe","Coffee"
2,4,"Joe","Coffee"
3,5,"Maria","Water"
"""