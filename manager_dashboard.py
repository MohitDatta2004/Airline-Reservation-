from tkinter import *
from . import manager_login, add_booking, manage_bookings, confirmed_bookings, pending_bookings, database
from tkinter import messagebox
from PIL import Image, ImageTk


class ManagerDashboard:
    def __init__(self, logged_in_data=""):
        self.t = Tk()
        self.loggedInData = logged_in_data
        self.fullwidth = self.t.winfo_screenwidth()
        self.fullheight = self.t.winfo_screenheight()
        self.width = int((self.fullwidth - 1000) / 2)
        self.height = int((self.fullheight - 650) / 2) - 40
        s = "1000x650+" + str(self.width) + "+" + str(self.height)
        self.t.geometry(s)
        self.t.title("Dashboard | Manager Panel | Airline Reservation")
        self.t.config(bg="Light Gray")
        self.icon = PhotoImage(file="icn2.png")
        self.t.iconphoto(False, self.icon)

    def widgets(self):
        self.f = Frame(self.t)
        self.f.place(x=0, y=0, width="1000", height="650")

        self.image_path = Image.open('manager/images/img2.jpg')
        self.image = self.image_path.resize((1000, 650))
        self.background_image = ImageTk.PhotoImage(self.image)
        print("Image path:- ", self.image_path)

        self.i = Canvas(self.f, width='1000', height='650')
        self.i.place(x=0, y=0)
        self.i.create_image('0', '0', image=self.background_image, anchor=NW)

        # --------------------------------------------------------------------------------------------------------------
        # MEASURE VALUES
        # Total Bookings
        self.f1 = Frame(self.f, bg="White")
        self.f1.place(x=140, y=120, width="220", height="80")
        self.in1 = Frame(self.f1, bg="Yellow")
        self.in1.place(x=0, y=0, width="10", height="80")
        self.totalBookings = database.total_bookings()
        self.total_airline_label = Label(self.f1, text=f'{self.totalBookings[0]}', font=("Century Gothic bold", 12),
                                         bg="White", fg="black")
        self.total_airline_label.place(x=10, y=20, width="210")
        self.lb1 = Label(self.f1, text='Total Bookings', font=("Century Gothic bold", 12), bg="White", fg="black")
        self.lb1.place(x=10, y=40, width="210")

        # Total Confirmed Bookings
        self.f2 = Frame(self.f, bg="White")
        self.f2.place(x=380, y=120, width="220", height="80")
        self.in2 = Frame(self.f2, bg="Blue")
        self.in2.place(x=0, y=0, width="10", height="80")
        self.totalConfirmedBookings = database.total_confirmed_bookings()
        self.total_aircraft_label = Label(self.f2, text=f'{self.totalConfirmedBookings[0]}', font=("Century Gothic bold", 12),
                                          bg="White",
                                          fg="black")
        self.total_aircraft_label.place(x=10, y=20, width="210")
        self.lb2 = Label(self.f2, text='Total Confirmed Bookings', font=("Century Gothic bold", 12), bg="White", fg="black")
        self.lb2.place(x=10, y=40, width="210")

        # Total Pending Bookings
        self.f3 = Frame(self.f, bg="White")
        self.f3.place(x=619, y=120, width="220", height="80")
        self.in3 = Frame(self.f3, bg="Gray")
        self.in3.place(x=0, y=0, width="10", height="80")
        self.totalPendingBookings = database.total_pending_bookings()
        self.total_manager_label = Label(self.f3, text=f'{self.totalPendingBookings[0]}', font=("Century Gothic bold", 12),
                                         bg="White",
                                         fg="black")
        self.total_manager_label.place(x=10, y=20, width="210")
        self.lb3 = Label(self.f3, text='Total Pending Bookings', font=("Century Gothic bold", 12), bg="White", fg="black")
        self.lb3.place(x=10, y=40, width="210")

        # --------------------------------------------------------------------------------------------------------------
        # ACTIONS
        self.submit = Button(self.f, text="Add Bookings", font=("Century Gothic bold", 10), bg="black", fg="white",
                             activebackground='Black',
                             activeforeground='White', cursor='hand2', command=self.open_add_bookings_page)
        self.submit.place(x=180, y=270, width="250", height="50")

        self.submit = Button(self.f, text="Manage Bookings", font=("Century Gothic bold", 10), bg="black", fg="white",
                             activebackground='Black',
                             activeforeground='White', cursor='hand2', command=self.open_manage_booking_page)
        self.submit.place(x=550, y=270, width="250", height="50")

        self.submit = Button(self.f, text="Confirmed Bookings", font=("Century Gothic bold", 10), bg="black",
                             fg="white", activebackground='Black',
                             activeforeground='White', cursor='hand2', command=self.open_confirmed_booking_page)
        self.submit.place(x=180, y=350, width="250", height="50")

        self.submit = Button(self.f, text="Pending Bookings", font=("Century Gothic bold", 10), bg="black", fg="white",
                             activebackground='Black',
                             activeforeground='White', cursor='hand2', command=self.open_pending_aircraft_page)
        self.submit.place(x=550, y=350, width="250", height="50")

        self.submit = Button(self.f, text="Logout", font=("Century Gothic bold", 10), bg="black", fg="white",
                             activebackground='Black',
                             activeforeground='White', cursor='hand2', command=self.logout_manager)
        self.submit.place(x=180, y=470, width="620", height="50")

        self.t.mainloop()

    def open_add_bookings_page(self):
        a = add_booking.AddBooking(self.loggedInData)
        a.widgets()

    def open_manage_booking_page(self):
        b = manage_bookings.ManageBookings(self.loggedInData)
        b.widgets()

    def open_confirmed_booking_page(self):
        g = confirmed_bookings.ConfirmedBookings(self.loggedInData)
        g.widgets()

    def open_pending_aircraft_page(self):
        t = pending_bookings.PendingBookings(self.loggedInData)
        t.widgets()

    def logout_manager(self):
        choice = messagebox.askyesno("Alert", "Do you really want to logout from your session?")
        if choice:
            messagebox.showinfo("Message", "Logout Successfully")
            self.t.destroy()
            f = manager_login.ManagerLogin()
            f.widgets()


if __name__ == "__main__":
    a = ManagerDashboard()
    a.widgets()
