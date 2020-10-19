import csv
"""
#functions
def load_file_into_list(filepath):
    #Loads csv file and saves file data as a list.
    try: 
        with open(filepath, "r") as file_name:
            my_list = []
            myreader = csv.reader(file_name,quoting =csv.QUOTE_ALL)
            for row in myreader:
                for element in row:
                    my_list.append(element)
            return my_list
    except FileNotFoundError as e:
        print(f"File not found: " + str(e))
    except Exception as e:
        print("Error encountered: " + str(e))

def load_file_into_dict(filepath):
    #Loads csv file and saves file data as a dictionary.
    try:
        with open(filepath, "r") as file_data:
            global preferences
            preferences = dict(filter(None, csv.reader(file_data, quoting = csv.QUOTE_ALL)))
            return preferences
    except FileNotFoundError as e:
        print(f"File not found: " + str(e))
    except Exception as e:
        print("Error encountered: " + str(e))

def save_list(filepath, my_list):
    #Overwrites specified csv file with data from specified list.
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
    #Overwrites specified csv file with data from specified dictionary.
    try:
        with open(filepath, "w") as file_data:
            writer = csv.writer(file_data, quoting = csv.QUOTE_ALL)
            for key,value in my_dict.items():
                writer.writerow([key,value])
    except FileNotFoundError as e:
        print(f"File not found: " + str(e))
    except Exception as e:
        print("Error encountered: " + str(e))
"""
"****************************************************************************************"
"****************************************************************************************"
"****************************************************************************************"
"****************************************************************************************"

from source.Data.data_store import drinks_filepath, people_filepath, preferences_filepath, menu_options_filepath

class File_Store_list:
    def __init__(self, filepath):
        self.filepath = filepath

    def load_into_list(self):
        "Converts csv file data into a list."
        try: 
            with open(self.filepath, "r") as file_name:
                myreader = csv.reader(file_name,quoting =csv.QUOTE_ALL)
                my_list = []
                for row in myreader:
                    for element in row:
                        my_list.append(element)
        except FileNotFoundError as e:
            print(f"File not found: " + str(e))
        except Exception as e:
            print("Error encountered: " + str(e))
        return my_list

    def save_list_to_file(self, my_list):
        "Converts list into a csv file"
        try:    
            with open(self.filepath, "w") as file_data:
                writer = csv.writer(file_data, quoting = csv.QUOTE_ALL)
                for i in my_list:
                    writer.writerow([i])
        except FileNotFoundError as e:
            print(f"File not found: " + str(e))
        except Exception as e:
            print("Error encountered: " + str(e))

class File_store_dict:
    def __init__(self, filepath):
        self.filepath = filepath
    
    def load_into_dict(self):
        "Converts csv file data into a dictionary."
        try:
            with open(self.filepath, "r") as file_data:
                global preferences
                preferences = dict(filter(None, csv.reader(file_data, quoting = csv.QUOTE_ALL)))
                return preferences
        except FileNotFoundError as e:
            print(f"File not found: " + str(e))
        except Exception as e:
            print("Error encountered: " + str(e))
    
    def save_dict_to_file(self, my_dict):
        "Converts dictionary into a csv file"
        try:
            with open(self.filepath, "w") as file_data:
                writer = csv.writer(file_data, quoting = csv.QUOTE_ALL)
                for key,value in my_dict.items():
                    writer.writerow([key,value])
        except FileNotFoundError as e:
            print(f"File not found: " + str(e))
        except Exception as e:
            print("Error encountered: " + str(e))

#loading from CSV files using ClASS FUNCTIONS
#drinks_file = File_Store_list(drinks_filepath)
#drinks_list = drinks_file.load_into_list()
#people_file = File_Store_list(people_filepath)
#people_list = people_file.load_into_list()
#preferences_file = File_store_dict(preferences_filepath)
#preferences = preferences_file.load_into_dict()


#saving lists to csv through classes
#drinks_file = File_Store_list(drinks_filepath)
#people_file = File_Store_list(people_filepath)
#drinks_file.save_list_to_file(drinks_list)
#people_file.save_list_to_file(people_list)

#saving lists to csv through functions 
#drinks_file.save_list_to_file(drinks_list)
#people_file.save_list_to_file(people_list)

#saving dict to csv through functions
#preferences_file.save_dict_to_file(preferences)
