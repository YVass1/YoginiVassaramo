import csv
import os
round_filepath = './source/Data/round.csv'
round_hist_filepath = './source/Data/round_history.csv'
round_fieldnames = ["RoundID","Owner","Brewer","ActiveStatus"]
round_hist_fieldnames = ["RoundID","OrderID","Name","Drink"]
import source.User.navigation as nav
import source.Persistence.sql_connection as sql


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
        round_history.append({"RoundID": self.round_id, "OrderID": order_id,"Name": name, "Drink": drink})
        #method adds to round-history list variable of the round object
        #adds to a dict like before BUT USEES OBJECT ROUND ID

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
                for my_dict in obj.round_history:
                #print([obj.round_id, obj.owner,obj.brewer,obj.active_status])
                    writer.writerow([my_dict["RoundID"],my_dict["OrderID"],my_dict["Name"], my_dict["Drink"]])

#create round object list from csv
round_file = File_store_round(round_filepath)
all_rounds_object_list = round_file.load_file_to_dict_round()

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
                print(obj.round_history)

    def save_round_history_to_file(self, object_list):
        with open(self.filepath, "w", newline="") as round_hist_file:
            writer = csv.writer(round_hist_file)
            writer.writerow(round_hist_fieldnames)
            for obj in  object_list:
                #print([obj.round_id, obj.owner,obj.brewer,obj.active_status])
                writer.writerow([obj.round_id, obj.owner,obj.brewer,obj.active_status])
        

round_hist_file = File_store_round_history(round_hist_filepath)
round_hist_file.load_file_to_object(all_rounds_object_list)

round_hist_file.save_round_history_to_file(all_rounds_object_list)

#save list of objects to csv file
round_file.save_object_list_to_file(all_rounds_object_list)

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