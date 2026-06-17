import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="airline_reservation_2"
)
cursor = conn.cursor()


def login_admin(login_details):
    try:
        cursor.execute("SELECT * FROM `admin` WHERE `username`=%s and `password`=%s", login_details)
        return cursor.fetchone()
    except:
        return False


# -------------------------------------------------------------------------------------------------------------------
# MANAGERS CRUD
def add_manager_data(manager_details):
    print("Database->manager_data:-", manager_details)
    try:
        cursor.execute(
            "INSERT INTO `manager` (`name`,`phone_number`,`email`,`password`,`address`) VALUES(%s,%s,%s,%s,%s)",
            manager_details)
        conn.commit()
        return True
    except mysql.connector.Error as error:
        print("MySQL error :- ", error)
        return False


def get_managers():
    try:
        cursor.execute("SELECT * FROM `manager`")
        return cursor.fetchall()
    except:
        return False


def delete_manager(manager_details):
    print("Database->Arg:", manager_details)
    cursor.execute("DELETE FROM `manager` WHERE `id`=%s", manager_details)
    conn.commit()
    return True


def update_manager_data(manager_details):
    try:
        cursor.execute(
            "UPDATE `manager` SET `name`=%s,`phone_number`=%s,`email`=%s,`password`=%s,`address`=%s WHERE `id`=%s",
            manager_details)
        conn.commit()
        return True
    except mysql.connector.Error as error:
        print("MYSql error:-", error)
        return False


# ---------------------------------------------------------------------------------------------------------
# AIRLINE CRUD

def add_airline_data(airline_details):
    print("Database->airline_data:-", airline_details)
    try:
        cursor.execute(
            "INSERT INTO `airlines`(`airline_id`,`airline_name`,`founded_year`,`country`,`headquarters`) VALUES(%s,%s,%s,%s,%s)",
            airline_details)
        conn.commit()
        return True
    except mysql.connector.Error as error:
        print("MySQL error :-", error)
        return False


def get_airlines():
    try:
        cursor.execute("SELECT * FROM `airlines`")
        return cursor.fetchall()
    except mysql.connector.Error as error:
        print("MySQL error :-", error)
        return False


def delete_data(airline_details):
    print("Database->Arg:", airline_details)
    cursor.execute("DELETE FROM `airlines` WHERE `id`=%s", airline_details)
    conn.commit()
    return True


def update_airline_data(airline_details):
    try:
        cursor.execute(
            "UPDATE `airlines` SET `airline_id`=%s, `airline_name`=%s, `founded_year`=%s, `country`=%s, `headquarters`=%s WHERE `id`=%s",
            airline_details)
        conn.commit()
        return True
    except mysql.connector.Error as error:
        print("MySQL error:-", error)
        return False


# -------------------------------------------------------------------------------------------------
# AIRCRAFT CRUD
def add_aircraft_data(aircraft_data):
    print("Database->aircraft_data:", aircraft_data)
    try:
        cursor.execute(
            "INSERT INTO `aircrafts`(`aircraft_id`,`model`,`sitting_capacity`,`engine_type`,`other_description`) VALUES(%s,%s,%s,%s,%s)",
            aircraft_data)
        conn.commit()
        return True
    except mysql.connector.Error as error:
        print("Mysql Error:", error)
        return False


def get_aircraft_data():
    try:
        cursor.execute("SELECT * FROM `aircrafts`")
        return cursor.fetchall()
    except mysql.connector.Error as error:
        print("Mysql Error:", error)
        return False


def delete_aircraft_data(aircraft_type):
    print("Database->Arg:", aircraft_type)
    cursor.execute("DELETE FROM `aircrafts`WHERE`id`=%s", aircraft_type)
    conn.commit()
    return True


def update_aircraft_data(aircraft_data):
    try:
        cursor.execute(
            "UPDATE `aircrafts` SET `aircraft_id`=%s,`model`=%s,`sitting_capacity`=%s,`engine_type`=%s,`other_description`=%s WHERE `id`=%s",
            aircraft_data)
        conn.commit()
        return True
    except mysql.connector.Error as error:
        print("Mysql Error:", error)
        return False


# -----------------------------------------------------------------------------------------------------------------------
# ALL BOOKINGS

def get_all_bookings():
    try:
        cursor.execute("SELECT * FROM booking")
        return cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []


def get_all_filtered_bookings(data):
    print("Selected status:- ", data)
    cursor.execute("SELECT * FROM `booking` WHERE `status`=%s", data)
    return cursor.fetchall()


def confirm_booking(data):
    print("Booking data:- ", data)
    try:
        cursor.execute("UPDATE `booking` SET `status`=%s WHERE `id`=%s", data)
        conn.commit()
        return True
    except mysql.connector.Error as error:
        print("MySQL error:- ", error)
        return False


# ----------------------------------------------------------------------------------------------------------------------
# MEASURE VALUES
def total_airlines():
    try:
        cursor.execute("SELECT COUNT(*) FROM airlines")
        return cursor.fetchone()
    except mysql.connector.Error as error:
        print("MySQL error:- ", error)
        return False


def total_aircrafts():
    try:
        cursor.execute("SELECT COUNT(*) FROM aircrafts")
        return cursor.fetchone()
    except mysql.connector.Error as error:
        print("MySQL error:- ", error)
        return False


def total_managers():
    try:
        cursor.execute("SELECT COUNT(*) FROM manager")
        return cursor.fetchone()
    except mysql.connector.Error as error:
        print("MySQL error:- ", error)
        return False


def total_bookings():
    try:
        cursor.execute("SELECT COUNT(*) FROM booking")
        return cursor.fetchone()
    except mysql.connector.Error as error:
        print("MySQL error:- ", error)
        return False
