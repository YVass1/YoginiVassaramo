import source.Persistence.mysql_connection as db_connect
import source.Classes.round_class as rd

sql_db = db_connect.SQL_database()

def load_data_from_sql():
    connection = sql_db.make_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT users.Person_first_name FROM users")
            people_tuple = cursor.fetchall()
            cursor.execute("SELECT drinks.Drink_Name FROM drinks")
            drinks_tuple = cursor.fetchall()
            cursor.execute("SELECT user_name, fav_drink FROM preferences")
            preferences_tuple = cursor.fetchall()
            cursor.execute("SELECT round_id, owner, brewer, active_status FROM rounds")
            rounds_tuple = cursor.fetchall()
            cursor.execute("SELECT round_id, order_id, name, drink FROM orders")
            orders_tuple = cursor.fetchall()
    except:
        print("ahhh error")
    finally:
        connection.close()

    people_list =[]
    drinks_list = []
    all_rounds_list = []
    all_orders_list = []
    preferences = dict(preferences_tuple)

    if not people_tuple:
        pass
    else:
        for tup in people_tuple:
            people_list.append(tup[0])
    if not drinks_tuple:
        pass
    else:
        for tup in drinks_tuple:
            drinks_list.append(tup[0])
    if not rounds_tuple:
        pass
    else:
        for tup in rounds_tuple:
            all_rounds_list.append(rd.Round_Handler(str(tup[0]), tup[1], tup[2], tup[3]))
    if not orders_tuple:
        pass
    else:
        for tup in orders_tuple:
            for obj in all_rounds_list:
                if obj.round_id == str(tup[0]):
                    obj.add_to_round(str(tup[1]),tup[2],tup[3])
    if not all_rounds_list:
        pass
    else:
        for obj in all_rounds_list:
            for order in obj.round_history:
                all_orders_list.append(order)
    
    return people_list, drinks_list, preferences, all_rounds_list

