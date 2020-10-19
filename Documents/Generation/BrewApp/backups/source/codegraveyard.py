
"""def orders(arguments):
    if len(arguments) == 1:
        print("You did not input any commands")
        exit()
    for command in range(1,len(arguments)):#may change into for i in arguments rather
        if arguments[i] == "get-people":
            print_table_list("people", people_list)#generalise here through dict/tuples
        elif arguments[i] == "get-drinks":
            print_table_list("drinks", drinks_list)
        else:
            print("Please enter a valid command")"""



import csv
from source.Formatting.tables import print_table_list, line_divider, table_width_1_col, print_table_dict, print_counter_var_table
from source.Persistence.persistence import load_file_into_dict

class XRound():
    def __init__(self, round_id):
        self.round_id = round_id.capitalize() #this is a tuple maybe
        self.round_list = []
        self.round = {self.round_id: self.round_list}

    def xprint_round_history(self): #enumerate this
        my_tup_list =[]
        for tup in self.round_list:
            my_tup_list.append(f"{tup[0]} added {tup[1]}")
        print_counter_var_table(f"Round History for: {self.round_id}", "Number", "Person : Added Drink", my_tup_list)

    def xadd_to_round(self,name,drink):
        if name:
            self.round[self.round_id].append((name.capitalize(), drink.capitalize()))
            return 
        elif name.isspace() or drink.isspace():
            print("Both name and drink is required!")
        else:
            print("Both name and drink is required!")
        return self.round

    def xprint_round(self):
        val_list =[]
        for tup in self.round_list:
            val_list.append(tup[1])
        print_counter_var_table(f"{self.round_id}\'s round: All drinks", "Number", "Drink", val_list)
"""
Xround3 = XRound("John")
Xround3.xadd_to_round("Belle","Almdudler")
Xround3.xadd_to_round("Mia", "expresso")
Xround3.xadd_to_round("Mia", "tea")
Xround3.xprint_round()
Xround3.xprint_round_history()
"""
def load_file_into_dictlist(filepath):
    """Loads csv file and saves file data as a dictionary with list and tuples."""
    try:
        with open(filepath, "r") as file_data:
            global round_dict
            round_dict = {}
            smth =[]
            myreader = csv.reader(file_data, quoting = csv.QUOTE_ALL)
            for row in myreader:
                round_dict[row[0]] = []
        with open(filepath, "r") as file_data:
            print(round_dict)
            myreader1 = csv.reader(file_data, quoting = csv.QUOTE_ALL)
            for key, value in round_dict.items():
                print(key)
                for row in myreader1:
                    if key in row:
                        print("yeah")
                        print(round_dict[key][0])
                        round_dict[key][0].append(tuple(row[1]))
                        round_dict[key][0].append(tuple(row[2]))
                        print("nope")
            print(round_dict)
        
            
    except FileNotFoundError as e:
        print(f"File not found: " + str(e))
    except Exception as e:
        print("Error encountered: " + str(e))

load_file_into_dictlist("./source/Data/round.csv")
#load data in correct files/save data into files idk
# readd add round option to menu nope
#add drink updates discontinued ones later
# backup files/directory made
#write unit tests ideas:
#create file handling class


"""
def print_table_dict_3_col(heading, sub_head1, sub_head2, sub_head3, my_dict):
    #Prints 3-column table containing specified dictionary
#counter,keys and values in the columns.
    width = len(heading)
    longest_col1 = len(sub_head1)
    longest_col2 = len(sub_head2)
    longest_col3 = len(sub_head3)
    for key,value in my_dict.items():
        if len(key) > longest_col2:
            longest_col2 = len(key)
        if len(value) == None:
            pass
        elif len(value)> longest_col3:
            longest_col3 = len(value)
    for counter, (key,value) in enumerate(my_dict.items(), 1):
        if len(str(counter)) > longest_col1:
            longest_col1 = len(str(counter))
        else:
            pass
    width = longest_col2 + longest_col1 + 8 + longest_col3
    line_divider(width)
    print("|" + heading.upper().center(width) + "|")
    line_divider(width)
    print(f"|{sub_head1.upper().center(longest_col1 + 2 )}" + "|" +
    f"{sub_head2.upper().center(longest_col2 + 2 )}" + "|" + f"{sub_head3.upper().center(longest_col3 +2)}"+"|")
    line_divider(width)
    counter = 1
    for counter, (key,value) in enumerate(my_dict.items(), counter):
        print( f"|" + f"{str(counter).center(longest_col1 + 2 )}"+ f"|" + f"{key.center(longest_col2 + 2 )}" + "|" + value.center(longest_col3 + 2 ) + "|")
    line_divider(width)

def print_table_dict_var_val(heading, sub_head1, sub_head2, my_dict):
    #Prints 2-column table containing specified dictionary
#counter and values in the columns.
    width = len(heading) + 2
    longest_col1 = len(sub_head1)
    longest_col2 = len(sub_head2)
    if longest_col1 + longest_col2 + 3+2 > width:
        width = longest_col1 + longest_col2 + 3
    for counter, (key,value) in enumerate(my_dict.items(), 1):
        if not counter:
            pass
        elif len(str(counter)) > len(sub_head1):
            longest_col1 = len(str(counter))
        if len(value) == None:
            pass
        elif len(value)> longest_col2:
            longest_col2 = len(value)
    line_divider(width)
    print("|" + heading.upper().center(width) + "|")
    line_divider(width)
    print(f"|{sub_head1.upper().center(longest_col1+2)}" + "|" +
    f"{sub_head2.upper().center(width- longest_col1-3)}" + "|")
    line_divider(width)
    counter = 1
    for counter, (key,value) in enumerate(my_dict.items(), counter):
        print(f"| {str(counter).center(longest_col1)}" + " | " + value + " "*(width - longest_col1 -4 - len(value)) + "|")
    line_divider(width)

def print_table_dict_var_val(heading, sub_head1, sub_head2, my_dict):
    #Prints 2-column table containing specified dictionary
#counter and values in the columns.
    width = len(heading) + 2
    longest_col1 = len(sub_head1)
    longest_col2 = len(sub_head2)
    if longest_col1 + longest_col2 + 3+2 > width:
        width = longest_col1 + longest_col2 + 3
    for counter, (key,value) in enumerate(my_dict.items(), 1):
        if not counter:
            pass
        elif len(str(counter)) > len(sub_head1):
            longest_col1 = len(str(counter))
        if len(value) == None:
            pass
        elif len(value)> longest_col2:
            longest_col2 = len(value)
    line_divider(width)
    print("|" + heading.upper().center(width) + "|")
    line_divider(width)
    print(f"|{sub_head1.upper().center(longest_col1+2)}" + "|" +
    f"{sub_head2.upper().center(width- longest_col1-3)}" + "|")
    line_divider(width)
    counter = 1
    for counter, (key,value) in enumerate(my_dict.items(), counter):
        print(f"| {str(counter).center(longest_col1)}" + " | " + value + " "*(width - longest_col1 -4 - len(value)) + "|")
    line_divider(width)

class XRound():
    def __init__(self, round_id):
        self.round_id = round_id.capitalize() #this is a tuple maybe
        self.round_history = {}
        self.round = {self.round_id: self.round_history}

    def xprint_round_history(self): #enumerate this
        print_table_dict_3_col(f"Round History for: {self.round_id}", "Number", "Person", "Added Drink", self.round_history)

    def xadd_to_round(self,name,drink):
        if name:
            self.round_history[name.capitalize()] = drink.capitalize()
            self.round[self.round_id] = self.round_history
            return 
        elif name.isspace() or drink.isspace():
            print("Both name and drink is required!")
        else:
            print("Both name and drink is required!")
        return self.round
        return self.round_history

    def xprint_round(self):
        print_table_dict_var_val(f"{self.round_id}\'s round: All drinks", "Number", "Drink", self.round_history)
        """

"""
class Round:
    def __init__(self, round_id):
        self.round_id = round_id.capitalize() #this is a tuple maybe
        self.round_history = {}
        self.round = {self.round_id: []}
    
    def add_to_round(self,name,drink):
        if name:
            self.round_history[name.capitalize()] = drink.capitalize()
            self.round[self.round_id].append(drink.capitalize())
            return 
        elif name.isspace() or drink.isspace():
            print("Both name and drink is required!")
        else:
            print("Both name and drink is required!")
        return self.round
        return self.round_history
    

    def print_round_history(self): 
        print_table_dict_3_col(f"Round History for: {self.round_id}", "Number", "Person", "Added Drink", self.round_history)
    
    def print_round(self):
        for key, value in self.round.items():
            print_counter_var_table(f"{self.round_id}\'s round: All drinks","Number"," Drink",value)
    
    

round1 = Round("Matt")
round1.add_to_round("john","coffee")
round1.add_to_round("matt","tea")
round1.print_round_history()
round1.print_round()

print(round1.round_id)
print(round1.round) 
print(round1.round_history)
"""