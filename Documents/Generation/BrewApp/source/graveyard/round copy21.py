import csv
import os
round_filepath = './source/Data/round.csv'
round_hist_filepath = './source/Data/round_history.csv'
import source.User.navigation as nav

#TO DO LIST:
#create csv files/ save and load function for adding to rounds info
#add to round function in class + constraint of who and which drink
#create functions to print menus, of single round
#add to menu option : add to round + user inputs
#unit testing


#makes a round but what if no drinks added :deal with this when printing menu for single rounds
#check if brewer name, owner name, name , drink are not unique
#file empty exceptions

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

    def add_to_round(self,name,drink):
        round_history.append({"RoundID": self.round_id,"Name": name, "Drink": drink})

        #adds to a dict like before BUT USEES OBJECT ROUND ID

class File_store_round:
    def __init__(self, filepath):
        self.filepath = filepath
    def load_file_to_dict_round(self):
        with open(self.filepath, "r") as round_file:
            myreader = csv.DictReader(round_file,quoting =csv.QUOTE_ALL)
            all_rounds_list = []
            for row in myreader:
                if not row:
                    pass
                else:
                    all_rounds_list.append(row)
            return all_rounds_list

    def save_all_rounds_to_file(self, round_dict):
        fieldnames = round_dict[0].keys()
        with open(self.filepath, "w", newline="") as round_file:
            dict_writer = csv.DictWriter(round_file,fieldnames)
            dict_writer.writeheader()
            dict_writer.writerows(round_dict)

round_file = File_store_round(round_filepath)
all_rounds_list = round_file.load_file_to_dict_round()

#loading and saving round info
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

col_list1 = [my_dict["RoundID"] for my_dict in all_rounds_list]
longest_col1 = longest_word("Round ID", col_list1)
col_list2 = [my_dict["Owner"] for my_dict in all_rounds_list]
longest_col2 = longest_word("Owner", col_list2)
col_list3 = [my_dict["Brewer"] for my_dict in all_rounds_list]
longest_col3 = longest_word("Brewer", col_list3)
col_list4 = [my_dict["ActiveStatus"] for my_dict in all_rounds_list]
longest_col4 = longest_word("Active Status", col_list4)

def all_rounds_table_width(my_list, heading, sub_head1, sub_head2, sub_head3, sub_head4):
    width = len(heading) 
    sub_head_width = len(sub_head1) + len(sub_head2) + len(sub_head3)+ len(sub_head4)+ 3*3
    if width < sub_head_width:
        width = sub_head_width
    if longest_col1 + longest_col2 + longest_col3 + longest_col4 + 3*3 > width:
        width = longest_col1 + longest_col2 + longest_col3 + longest_col4 + 3*3
    return width + additional_char

def print_all_rounds_table(my_list, heading, sub_head1, sub_head2, sub_head3, sub_head4):
    width = all_rounds_table_width(my_list, heading, sub_head1, sub_head2, sub_head3, sub_head4)
    line_divider(width)
    print("|" + heading.upper().center(width) + "|")
    line_divider(width)
    print(f"|{sub_head1.upper().center(longest_col1+2)}" + "|" +
    f"{sub_head2.upper().center(longest_col2+2)}"+ "|" +
    f"{sub_head3.upper().center(longest_col3+2)}"+ "|" +
    f"{sub_head4.upper().center(longest_col4+2)}"
    + "|")
    line_divider(width)
    for round_dict in my_list:
        print(f"| " + round_dict["RoundID"].center(longest_col1) +
         " |" + round_dict[sub_head2].center(longest_col2+2)
         + "|" + round_dict[sub_head3].center(longest_col3+2)
         + "|" + round_dict["ActiveStatus"].center(longest_col4 +2)
         + "|")
    line_divider(width)

#printing out all rounds
#***************************************************************************************************************************
#***************************************************************************************************************************
#***************************************************************************************************************************
#***************************************************************************************************************************


def round_user_input(people_list):
    end_loop = False
    while not end_loop:
        try:
            os.system("clear")
            global round_id_list
            round_id_list = []
            for my_dict in all_rounds_list:
                round_id_list.append(my_dict["RoundID"])

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
                owner = input("Enter Round Owner's name: ").capitalize()
                if not owner or owner.isspace():
                    print("You have entered nothing!")
                    nav.try_again()
                elif any(num in owner for num in "0123456789"):
                    print("No numbers can be included in name.")
                    nav.try_again()
                elif owner not in people_list:
                    print("Only an User can be the owner of a round.")
                    nav.try_again()
                else:
                    #add can only be from user table constraint 
                    brewer =input("Enter Brewer's name: ").capitalize()
                    #anyone right now
                    active = input("Enter a round active status, Yes or No: ").capitalize()
                    #activation constraint of must be yes or no
                    confirmation = nav.confirm()
                    if confirmation:
                        owner = Round_Handler(round_num, owner, brewer, active)
                        round_dict = {'RoundID': owner.round_id, 'Owner': owner.owner,
                        'Brewer': owner.brewer,'ActiveStatus': owner.active_status}
                        all_rounds_list.append(round_dict)
                        print(f"{owner.owner}\'s new round has been successfully created!")
                    else:
                        print("No changes have been made.")
                        pass
                    end_loop = True
        except ValueError:
            print("No valid input.")
            nav.try_again()
    return all_rounds_list

#created round_handler class and function to take in user input
# to then create a new round 
#***************************************************************************************************************************
#***************************************************************************************************************************
#***************************************************************************************************************************
#***************************************************************************************************************************

#load and save csv files
round_hist_file = File_store_round(round_hist_filepath)
round_hist = round_hist_file.load_file_to_dict_round()
print(round_hist)



"""
1,"Aria","Tea"
1,"Aria","Tea"
1,"Joe","Coffee"
2,"Joe","Coffee"
3,"Maria","Water"

"""
#create 2 new rounds
#add to round
#see if adding order connected to correct round
#add 2 order to it
#see if its round history is okay

# create function : needs to ask for orderid and then
# asks user input twice with constraints
#and puts input into add_to_round class, with order ID

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


