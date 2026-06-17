import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="airline_reservation_2"
)
cursor = conn.cursor()


def manager_login(data):
    print("Manager login dat:- ", data)
    try:
        cursor.execute("SELECT * FROM `manager` WHERE `email`=%s AND `password`=%s", data)
        return cursor.fetchone()
    except mysql.connector.Error as error:
        print("Error:- ", error)
        return False


def get_airlines():
    try:
        cursor.execute("SELECT * FROM `airlines`")
        return cursor.fetchall()
    except mysql.connector.Error as error:
        print("MySQL error :-", error)
        return False


def get_aircraft_data():
    try:
        cursor.execute("SELECT * FROM `aircrafts`")
        return cursor.fetchall()
    except mysql.connector.Error as error:
        print("Mysql Error:", error)
        return False


def add_flight_booking_data(booking_data):
    print("Booking details:- ", booking_data)
    try:
        cursor.execute(
            "INSERT INTO booking (`flight_number`, `airline`, `departure_airport`,`destination`, `date`, `aircraft_type`,`ticket_price`,`number_of_tickets`,`total_price`, `passenger_name`, `date_of_birth`, `gender`, `passport_id`, `contact_number`,`passenger_email`, `status`,`added_by`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            booking_data)
        conn.commit()
        return True
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False


def get_bookings(manager_email):
    print("Manager email:- ", manager_email)
    try:
        cursor.execute("SELECT * FROM booking WHERE `added_by`=%s", manager_email)
        return cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []


def get_confirmed_bookings(manager_email):
    print("Manager email:- ", manager_email)
    try:
        cursor.execute("SELECT * FROM booking WHERE `status`='Confirmed' AND `added_by`=%s", manager_email)
        return cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []


def get_pending_bookings(manager_email):
    print("Manager email:- ", manager_email)
    try:
        cursor.execute("SELECT * FROM booking WHERE `status`='Pending' AND `added_by`=%s", manager_email)
        return cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []


def delete_booking(booking_id):
    try:
        cursor.execute("DELETE FROM booking WHERE id=%s", (booking_id,))
        conn.commit()
        return True
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False


def update_booking(booking_data):
    try:
        query = """
        UPDATE booking SET passenger_name=%s, phone_number=%s, address=%s, email=%s, occupation=%s,
                            gender=%s, flight_number=%s, date_of_booking=%s, price=%s, route_from=%s,
                            route_to=%s, num_passengers=%s, airline_name=%s
        WHERE id=%s
        """
        cursor.execute(query, booking_data)
        conn.commit()
        return True
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False


# ----------------------------------------------------------------------------------------------------------------------
# MEASURE VALUES
def total_confirmed_bookings():
    try:
        cursor.execute("SELECT COUNT(*) FROM booking WHERE `status`='Confirmed'")
        return cursor.fetchone()
    except mysql.connector.Error as error:
        print("MySQL error:- ", error)
        return False


def total_pending_bookings():
    try:
        cursor.execute("SELECT COUNT(*) FROM booking WHERE `status`='Pending'")
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


# Close connection when done
def close_connection():
    cursor.close()
    conn.close()
