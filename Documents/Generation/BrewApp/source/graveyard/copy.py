import csv
import os
from source.Data.data_store import round_filepath, round_hist_filepath
import source.User.navigation as nav
import source.Persistence.mysql_connection as db_connect
import source.Formatting.tables as tab
import source.User.commands as com

#CONSTANTS
round_fieldnames = ["RoundID","Owner","Brewer","ActiveStatus"]
round_hist_fieldnames = ["RoundID","OrderID","Name","Drink"]


#creating Round class here
class Round_Handler:
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

#saving object list to csv through classes
#round_file.save_object_list_to_file(all_rounds_object_list)
#round_hist_file.save_round_history_to_file(all_rounds_object_list)


#creates a new round object using user input and to all_rounds_object_list
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
                                long_col1 = long_col1_round_history(obj.round_history)
                                long_col2 = long_col2_round_history(obj.round_history)
                                long_col3 = long_col3_round_history(obj.round_history)
                                width = round_history_table_width(f"{obj.owner}\'s round", "Order ID", "Name", "Drink", long_col1, long_col2, long_col3)
                                print_round_history(obj.round_history, width, f"{obj.owner}\'s round", "Order ID", "Name", "Drink", long_col1, long_col2, long_col3)
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
                                        #obj.add_to_round(order_id,name, drink)
                                        #print(f"The order has been added to {obj.owner}\'s round!")
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
                        long_col1 = long_col1_round_history(obj.round_history)
                        long_col2 = long_col2_round_history(obj.round_history)
                        long_col3 = long_col3_round_history(obj.round_history)
                        width = round_history_table_width(f"{obj.owner}\'s round", "Order ID", "Name", "Drink", long_col1, long_col2, long_col3)
                        print_round_history(obj.round_history, width, f"{obj.owner}\'s round", "Order ID", "Name", "Drink", long_col1, long_col2, long_col3)
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
                                com.remove_order_from_round(obj.owner, round_num, order_num)
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