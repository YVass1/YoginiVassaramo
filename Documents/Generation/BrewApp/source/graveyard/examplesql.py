import pymysql
import csv

def load_data_from_csv_to_sql():
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
    cursor.execute("CREATE TABLE giles (person_id INTEGER AUTO_INCREMENT PRIMARY KEY, User_name VARCHAR(100),first_name VARCHAR(100),surname VARCHAR(100),Mobile_Phone VARCHAR(30),ZIP_or_PostCode VARCHAR(20));")

    with open("./source/example.csv", 'r')  as ex_file:
        next(ex_file)
        reader = csv.reader(ex_file)
        for row in reader:
            username = row[0]
            full_name = row[1].split()
            first_name = full_name[0].capitalize()
            surname = full_name[1].capitalize()
            phone = row[7]
            postcode = row[12]
            args = [username, first_name, surname, phone, postcode]
            cursor.execute("INSERT INTO giles (User_name, first_name,surname,Mobile_Phone,ZIP_or_PostCode ) VALUES (%s, %s, %s, %s, %s)", args)
    cursor.close()
    connection.close()
 

if __name__ == "__main__":
    load_data_from_csv_to_sql()
