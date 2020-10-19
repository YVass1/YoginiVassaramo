#old code to save to database from app using slow method truncate
"""
def save_to_db(people_list, drinks_list, preferences):
    connection = pymysql.connect(
        host = "localhost",
        port = 33066,
        user = "root",
        password = "password123",
        db = "brew_app",
        autocommit=True
        #read_timeout = 60
    )
    cursor = connection.cursor()

    cursor.execute("TRUNCATE TABLE drinks")
    for drink in drinks_list:
        cursor.execute("INSERT INTO drinks (Drink_Name) VALUES (%s)", drink)

    cursor.execute("TRUNCATE TABLE users ")
    for person in people_list:
        cursor.execute("INSERT INTO users (Person_first_name) VALUES (%s)", person)
    
    cursor.execute("TRUNCATE TABLE preferences")
    for key,value in preferences.items():
        cursor.execute("INSERT INTO preferences (user_name, fav_drink) VALUES (%s, %s)", [key, value])

    cursor.close()
    connection.close()
"""

#old code to save to database from csvfiles 

""" 
def load_from_csv_to_sql():
    connection = pymysql.connect(
        host = "localhost",
        port = 33066,
        user = "root",
        password = "password123",
        db = "brew_app",
        autocommit=True
        #read_timeout = 60
    )
    cursor = connection.cursor()

    with open(d.drinks_filepath, 'r')  as file_name:
        #next(ex_file)
        cursor.execute("TRUNCATE TABLE drinks")
        reader = csv.reader(file_name)
        for row in reader:
            args = row[0]
            cursor.execute("INSERT INTO drinks (Drink_Name) VALUES (%s)", args)
    
    with open(d.people_filepath, 'r')  as file_name:
        #next(ex_file)
        reader = csv.reader(file_name)
        cursor.execute("TRUNCATE TABLE users ")
        for row in reader:
            args = row[0]
            cursor.execute("INSERT INTO users (Person_first_name) VALUES (%s)", args)
    
    cursor.close()
    connection.close()


"""