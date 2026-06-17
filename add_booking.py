from tkinter import *
from . import database, manage_bookings
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkcalendar import DateEntry
from PIL import Image, ImageTk


class AddBooking:
    def __init__(self, logged_in_data=""):
        self.t = Toplevel()
        self.loggedInData = logged_in_data
        self.t.title("Add Booking | Airline Reservation | Admin Panel")

        self.fullwidth = self.t.winfo_screenwidth()
        self.fullheight = self.t.winfo_screenheight()
        self.width = int((self.fullwidth - 1000) / 2)
        self.height = int((self.fullheight - 600) / 2) - 40
        s = "1000x600+" + str(self.width) + "+" + str(self.height)
        self.t.geometry(s)
        self.icon = PhotoImage(file="icn2.png")
        self.t.iconphoto(False, self.icon)

    def widgets(self):
        self.f = Frame(self.t, bg="white")
        self.f.place(x=0, y=0, width="1000", height="600")

        self.image_path = Image.open('manager/images/img3.jpg')
        self.image = self.image_path.resize((1000, 600))
        self.background_image = ImageTk.PhotoImage(self.image)
        print("Image path:- ", self.image_path)

        self.i = Canvas(self.f, width='1000', height='600')
        self.i.place(x='0', y='0')
        self.i.create_image('0', '0', image=self.background_image, anchor=NW)

        self.i.create_text(520, 40, text='ADD BOOKING DETAILS', font=("Century Gothic bold", 20))

        # ----------------- Flight Details ----------------------------------------------------------------------
        self.i.create_text(190, 100, text='Flight Number', font=("Century Gothic bold", 15))
        self.flight_number = Entry(self.f, bg="white", fg="black", font=("Century Gothic", 12), bd=3, relief=SOLID,
                                   borderwidth=1)
        self.flight_number.place(x=120, y=120, width="220", height="30")

        self.i.create_text(185, 180, text='Select Airline', font=("Century Gothic bold", 15))
        self.airline_list = []
        for i in database.get_airlines():
            self.airline_list.append(i[2])
        self.airline = Combobox(self.f, values=self.airline_list, state="readonly", width=18,
                                font=("Century Gothic", 12))
        self.airline.place(x=120, y=200, width="220", height="30")

        self.i.create_text(205, 260, text='Departure Airport', font=("Century Gothic bold", 15))
        self.departure_airport = Entry(self.f, bg="white", fg="black", font=("Century Gothic", 12), bd=3, relief=SOLID,
                                       borderwidth=1)
        self.departure_airport.place(x=120, y=280, width="220", height="30")

        self.i.create_text(200, 340, text='Select Flight Date', font=("Century Gothic bold", 15))
        self.date = DateEntry(self.f, bg="white", fg="black", font=("Century Gothic", 12), bd=3, relief=SOLID,
                              borderwidth=1, state="readonly")
        self.date.place(x=120, y=360, width="220", height="30")

        self.i.create_text(215, 420, text='Select Aircraft Type', font=("Century Gothic bold", 15))
        self.aircraft_type_list = []
        for i in database.get_aircraft_data():
            self.aircraft_type_list.append(i[2])
        self.aircraft_type = Combobox(self.f, values=self.aircraft_type_list, state="readonly", width=18,
                                      font=("Century Gothic", 12))
        self.aircraft_type.place(x=120, y=440, width="220", height="30")

        # --------------------- Passenger Details ----------------------------------------------------------------
        self.i.create_text(740, 100, text='Passenger Name', font=("Century Gothic bold", 15))
        self.passenger_name = Entry(self.f, bg="white", fg="black", font=("Century Gothic", 12), bd=3, relief=SOLID,
                                    borderwidth=1)
        self.passenger_name.place(x=660, y=120, width="220", height="30")

        self.i.create_text(720, 180, text='Date of Birth', font=("Century Gothic bold", 15))
        self.date_of_birth = DateEntry(self.f, bg="white", fg="black", font=("Century Gothic", 12), bd=3, relief=SOLID,
                                       borderwidth=1, state="readonly")
        self.date_of_birth.place(x=660, y=200, width="220", height="30")

        self.i.create_text(730, 260, text='Select Gender', font=("Century Gothic bold", 15))
        self.gender_list = ["Male", "Female", "Other"]
        self.gender = Combobox(self.f, values=self.gender_list, state="readonly", width=18,
                               font=("Century Gothic", 12))
        self.gender.place(x=660, y=280, width="220", height="30")

        self.i.create_text(755, 340, text='Passport ID Number', font=("Century Gothic bold", 15))
        self.passport_id = Entry(self.f, bg="white", fg="black", font=("Century Gothic", 12), bd=3, relief=SOLID,
                                 borderwidth=1)
        self.passport_id.place(x=660, y=360, width="220", height="30")

        self.i.create_text(740, 420, text='Contact Number', font=("Century Gothic bold", 15))
        self.contact_number = Entry(self.f, bg="white", fg="black", font=("Century Gothic", 12), bd=3, relief=SOLID,
                                    borderwidth=1)
        self.contact_number.place(x=660, y=440, width="220", height="30")

        self.i.create_text(490, 420, text='Passenger Email', font=("Century Gothic bold", 15))
        self.passenger_email = Entry(self.f, bg="white", fg="black", font=("Century Gothic", 12), bd=3, relief=SOLID,
                                     borderwidth=1)
        self.passenger_email.place(x=390, y=440, width="220", height="30")

        # ------------------------ Price Details -------------------------------------------------------------------

        self.i.create_text(490, 100, text='Ticket Price (Fixed)', font=("Century Gothic bold", 15))
        self.ticket_price = Entry(self.f, bg="white", fg="black",
                                  font=("Century Gothic", 12), bd=3, relief=SOLID,
                                  borderwidth=1)
        self.ticket_price.place(x=385, y=120, width="220", height="30")

        self.i.create_text(490, 180, text='Number of Tickets', font=("Century Gothic bold", 15))
        self.number_of_tickets = StringVar()
        self.tickets = Entry(self.f, textvariable=self.number_of_tickets, bg="white", fg="black",
                             font=("Century Gothic", 12), bd=3, relief=SOLID,
                             borderwidth=1)
        self.tickets.place(x=388, y=200, width="220", height="30")
        self.tickets.bind('<KeyRelease>', self.on_key_release)

        self.i.create_text(490, 260, text='Final Price', font=("Century Gothic bold", 15))
        self.price_label = self.i.create_text(490, 290, font=("Century Gothic bold", 15))

        self.i.create_text(490, 340, text='Destination', font=("Century Gothic bold", 15))
        self.destination = Entry(self.f, bg="white", fg="black",
                                 font=("Century Gothic", 12), bd=3, relief=SOLID,
                                 borderwidth=1)
        self.destination.place(x=390, y=360, width="220", height="30")

        self.submit = Button(self.t, text="Submit", width='20', bg='Black', fg='White',
                             font=("Century Gothic bold", 12), command=self.add_data)
        self.submit.place(x=380, y=500, width="250", height="30")

        self.t.mainloop()

    def on_key_release(self, event):
        # Retrieve the text from the Entry widget
        entered_text = self.number_of_tickets.get()
        print("Number of tickets:- ", entered_text)
        self.total_price = int(self.ticket_price.get()) * int(entered_text)
        print("Total price:- ", self.total_price)
        self.i.itemconfig(self.price_label, text="")
        self.i.itemconfig(self.price_label, text=f"Rs.{self.total_price}")

    def add_data(self):
        # Flight Details
        flight_number = self.flight_number.get()
        airline = self.airline.get()
        departure_airport = self.departure_airport.get()
        destination = self.destination.get()
        date = self.date.get()
        aircraft_type = self.aircraft_type.get()
        ticket_price = self.ticket_price.get()
        number_of_tickets = self.number_of_tickets.get()

        # Passenger Details
        passenger_name = self.passenger_name.get()
        date_of_birth = self.date_of_birth.get()
        gender = self.gender.get()
        passport_id = self.passport_id.get()
        contact_number = self.aircraft_type.get()
        passenger_email = self.passenger_email.get()

        if flight_number == "":
            messagebox.showwarning("Alert", "Please enter flight number first.")
        elif airline == "":
            messagebox.showwarning("Alert", "Please select airline first.")
        elif departure_airport == "":
            messagebox.showwarning("Alert", "Please enter departure airport first.")
        elif destination == "":
            messagebox.showwarning("Alert", "Please enter destination first.")
        elif date == "":
            messagebox.showwarning("Alert", "Please select flight date first.")
        elif aircraft_type == "":
            messagebox.showwarning("Alert", "Please select aircraft first.")
        elif ticket_price == "":
            messagebox.showwarning("Alert", "Please enter ticket price first.")
        elif number_of_tickets == "":
            messagebox.showwarning("Alert", "Please enter number of ticket first.")
        elif passenger_name == "":
            messagebox.showwarning("Alert", "Please enter passenger name first.")
        elif date_of_birth == "":
            messagebox.showwarning("Alert", "Please enter date of birth first.")
        elif gender == "":
            messagebox.showwarning("Alert", "Please select gender first.")
        elif passport_id == "":
            messagebox.showwarning("Alert", "Please enter passport id number first.")
        elif contact_number == "":
            messagebox.showwarning("Alert", "Please enter contact number first.")
        elif passenger_email == "":
            messagebox.showwarning("Alert", "Please enter passenger email first.")
        else:
            print("Flight details:", flight_number, airline, departure_airport, destination, date, aircraft_type,
                  ticket_price, number_of_tickets, self.total_price)
            print("Passenger details:- ", passenger_name, date_of_birth, gender, passport_id, contact_number,
                  passenger_email)

            data = (
                flight_number, airline, departure_airport, destination, date, aircraft_type, ticket_price,
                number_of_tickets,
                self.total_price,
                passenger_name,
                date_of_birth, gender,
                passport_id, contact_number, passenger_email, "Pending", self.loggedInData[3])

            result = database.add_flight_booking_data(data)
            if result:
                messagebox.showinfo("Message", "Booking placed successfully")
                self.t.destroy()
                f = manage_bookings.ManageBookings(logged_in_data=self.loggedInData)
                f.widgets()
            else:
                messagebox.showwarning("Alert", "Something went wrong")


if __name__ == "__main__":
    a = AddBooking()
    a.widgets()
