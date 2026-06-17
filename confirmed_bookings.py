from tkinter import *
from tkinter.ttk import Treeview
from . import database, add_booking
from tkinter import ttk
from PIL import Image, ImageTk


class ConfirmedBookings:
    def __init__(self, logged_in_data=""):
        self.t = Toplevel()
        self.loggedInData = logged_in_data
        self.t.title("Confirmed Bookings | Airline Reservation | Manager Panel")
        self.fullwidth = self.t.winfo_screenwidth()
        self.fullheight = self.t.winfo_screenheight()
        self.width = int((self.fullwidth - 800) / 2)
        self.height = int((self.fullheight - 500) / 2) - 40
        s = "800x500+" + str(self.width) + "+" + str(self.height)
        self.t.geometry(s)
        self.icon = PhotoImage(file="icn2.png")
        self.t.iconphoto(False, self.icon)

    def widgets(self):
        self.image_path = Image.open('manager/images/img4.jpg')
        self.image = self.image_path.resize((800, 500))
        self.background_image = ImageTk.PhotoImage(self.image)
        print("Image path:- ", self.image_path)

        self.i = Canvas(self.t, width='800', height='500')
        self.i.place(x='0', y='0')
        self.i.create_image('0', '0', image=self.background_image, anchor=NW)

        self.i.create_text(400, 50, text='CONFIRMED BOOKINGS DETAILS', fill='Black',
                           font=("Century Gothic bold", 20))

        self.add_aircraft_button = Button(self.t, text="Add Booking", bg='Black', fg='White', width='20',
                                          font=("Century Gothic bold", 10), command=self.open_add_booking_page)
        self.add_aircraft_button.place(x=650, y=35, width="100", height="30")

        self.f = Frame(self.t, width='700', height='350')
        self.f.place(x=50, y=100)

        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Century Gothic', 10))
        style.configure("mystyle.Treeview.Heading", font=('Century Gothic bold', 10, 'bold'))

        self.tr = Treeview(self.f,
                           columns=("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P"),
                           selectmode='extended',
                           style="mystyle.Treeview")

        self.tr.heading("#0", text="ID")
        self.tr.column("#0", minwidth=100, width=100, stretch=True, anchor=CENTER)

        self.tr.heading("#1", text="FLIGHT NUMBER")
        self.tr.column("#1", minwidth=100, width=200, stretch=True, anchor=CENTER)

        self.tr.heading("#2", text="AIRLINE NAME")
        self.tr.column("#2", minwidth=100, width=200, stretch=True, anchor=CENTER)

        self.tr.heading("#3", text="DEPARTURE AIRPORT")
        self.tr.column("#3", minwidth=100, width=200, stretch=True, anchor=CENTER)

        self.tr.heading("#4", text="DESTINATION")
        self.tr.column("#4", minwidth=100, width=200, stretch=True, anchor=CENTER)

        self.tr.heading("#5", text="DATE")
        self.tr.column("#5", minwidth=100, width=200, stretch=True, anchor=CENTER)

        self.tr.heading("#6", text="AIRCRAFT TYPE")
        self.tr.column("#6", minwidth=100, width=200, stretch=True, anchor=CENTER)

        self.tr.heading("#7", text="TICKET PRICE")
        self.tr.column("#7", minwidth=100, width=200, stretch=True, anchor=CENTER)

        self.tr.heading("#8", text="NUMBER OF TICKETS")
        self.tr.column("#8", minwidth=100, width=200, stretch=True, anchor=CENTER)

        self.tr.heading("#9", text="TOTAL PRICE")
        self.tr.column("#9", minwidth=100, width=200, stretch=True, anchor=CENTER)

        self.tr.heading("#10", text="PASSENGER NAME")
        self.tr.column("#10", minwidth=100, width=200, stretch=True, anchor=CENTER)

        self.tr.heading("#11", text="DATE OF BIRTH")
        self.tr.column("#11", minwidth=100, width=200, stretch=True, anchor=CENTER)

        self.tr.heading("#12", text="GENDER")
        self.tr.column("#12", minwidth=100, width=200, stretch=True, anchor=CENTER)

        self.tr.heading("#13", text="PASSPORT ID NUMBER")
        self.tr.column("#13", minwidth=100, width=250, stretch=True, anchor=CENTER)

        self.tr.heading("#14", text="CONTACT NUMBER")
        self.tr.column("#14", minwidth=100, width=250, stretch=True, anchor=CENTER)

        self.tr.heading("#15", text="PASSENGER EMAIL")
        self.tr.column("#15", minwidth=100, width=250, stretch=True, anchor=CENTER)

        self.tr.heading("#16", text="STATUS")
        self.tr.column("#16", minwidth=100, width=250, stretch=True, anchor=CENTER)

        data = database.get_confirmed_bookings((self.loggedInData[3],))
        for i in data:
            self.tr.insert("", 0, text=i[0],
                           values=(
                               i[1], i[2], i[3], i[4], i[5], i[6], f"Rs.{i[7]}", i[8], f"Rs.{i[9]}", i[10], i[11],
                               i[12],
                               i[13],
                               i[14],
                               i[15],
                               i[16]))

        # Constructing vertical scroll bar on treeview
        self.vertical_scrollbar = Scrollbar(self.tr, orient="vertical", command=self.tr.yview)
        self.vertical_scrollbar.pack(side='right', fill='y')
        self.tr.configure(yscrollcommand=self.vertical_scrollbar.set)

        # Constructing horizontal scroll bar on treeview
        self.horizontal_scrollbar = Scrollbar(self.tr, orient="horizontal", command=self.tr.xview)
        self.horizontal_scrollbar.pack(side='bottom', fill='x')
        self.tr.configure(xscrollcommand=self.horizontal_scrollbar.set)

        self.tr.bind("<Double Button-1>", self.actions)
        self.tr.place(x=1, y=1, width="700", height="350")

        self.t.mainloop()

    def actions(self, e):
        row = self.tr.focus()
        print("Focused row:", row)

        column = self.tr.identify_column(e.x)
        print("column"), column

        data = self.tr.item(row)
        print("Data of focused row", data)

        r_id = (data.get("text"),)
        print("id of focused row", r_id)

    def open_add_booking_page(self):
        self.t.destroy()
        g = add_booking.AddBooking(logged_in_data=self.loggedInData)
        g.widgets()


if __name__ == "__main__":
    a = ConfirmedBookings()
    a.widgets()
