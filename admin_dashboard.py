from tkinter import *
from . import add_manager, manage_managers, add_airlines, manage_airline, all_bookings, add_aircraft, manage_aircrafts, \
    admin_login_page, database
from tkinter import messagebox
from PIL import Image, ImageTk


class AdminDashboard:
    def __init__(self):
        self.t = Tk()
        self.fullwidth = self.t.winfo_screenwidth()
        self.fullheight = self.t.winfo_screenheight()
        self.width = int((self.fullwidth - 1000) / 2)
        self.height = int((self.fullheight - 650) / 2) - 40
        s = "1000x650+" + str(self.width) + "+" + str(self.height)
        self.t.geometry(s)
        self.t.title("Dashboard | Admin Panel | Airline Reservation")
        self.t.config(bg="Light Gray")
        self.icon = PhotoImage(file="admin/images/icn2.png")
        self.t.iconphoto(False, self.icon)

    def widgets(self):
        self.f = Frame(self.t)
        self.f.place(x=0, y=0, width="1000", height="650")

        self.image_path = Image.open('admin/images/img2.jpg')
        self.image = self.image_path.resize((1000, 650))
        self.background_image = ImageTk.PhotoImage(self.image)
        print("Image path:- ", self.image_path)

        self.i = Canvas(self.f, width='1000', height='650')
        self.i.place(x=0, y=0)
        self.i.create_image('0', '0', image=self.background_image, anchor=NW)

        # --------------------------------------------------------------------------------------------------------------
        # MEASURE VALUES
        # Total Airlines
        self.f1 = Frame(self.f, bg="White")
        self.f1.place(x=30, y=50, width="220", height="80")
        self.in1 = Frame(self.f1, bg="Yellow")
        self.in1.place(x=0, y=0, width="10", height="80")
        self.totalAirlines = database.total_airlines()
        self.total_airline_label = Label(self.f1, text=f'{self.totalAirlines[0]}', font=("Century Gothic bold", 12),
                                         bg="White", fg="black")
        self.total_airline_label.place(x=10, y=20, width="210")
        self.lb1 = Label(self.f1, text='Total Airlines', font=("Century Gothic bold", 12), bg="White", fg="black")
        self.lb1.place(x=10, y=40, width="210")

        # Total Aircrafts
        self.f2 = Frame(self.f, bg="White")
        self.f2.place(x=269, y=50, width="220", height="80")
        self.in2 = Frame(self.f2, bg="Blue")
        self.in2.place(x=0, y=0, width="10", height="80")
        self.totalAircrafts = database.total_aircrafts()
        self.total_aircraft_label = Label(self.f2, text=f'{self.totalAircrafts[0]}', font=("Century Gothic bold", 12),
                                          bg="White",
                                          fg="black")
        self.total_aircraft_label.place(x=10, y=20, width="210")
        self.lb2 = Label(self.f2, text='Total Aircrafts', font=("Century Gothic bold", 12), bg="White", fg="black")
        self.lb2.place(x=10, y=40, width="210")

        # Total Managers
        self.f3 = Frame(self.f, bg="White")
        self.f3.place(x=509, y=50, width="220", height="80")
        self.in3 = Frame(self.f3, bg="Gray")
        self.in3.place(x=0, y=0, width="10", height="80")
        self.totalManagers = database.total_managers()
        self.total_manager_label = Label(self.f3, text=f'{self.totalManagers[0]}', font=("Century Gothic bold", 12),
                                         bg="White",
                                         fg="black")
        self.total_manager_label.place(x=10, y=20, width="210")
        self.lb3 = Label(self.f3, text='Total Managers', font=("Century Gothic bold", 12), bg="White", fg="black")
        self.lb3.place(x=10, y=40, width="210")

        # Total Bookings
        self.f4 = Frame(self.f, bg="White")
        self.f4.place(x=750, y=50, width="220", height="80")
        self.in4 = Frame(self.f4, bg="Brown")
        self.in4.place(x=0, y=0, width="10", height="80")
        self.totalBookings = database.total_bookings()
        self.total_bookings_label = Label(self.f4, text=f'{self.totalBookings[0]}', font=("Century Gothic bold", 12),
                                          bg="White",
                                          fg="black")
        self.total_bookings_label.place(x=10, y=20, width="210")
        self.lb4 = Label(self.f4, text='Total Bookings', font=("Century Gothic bold", 12), bg="White", fg="black")
        self.lb4.place(x=10, y=40, width="210")

        # --------------------------------------------------------------------------------------------------------------
        # ACTIONS
        self.submit = Button(self.f, text="Add Manager", font=("Century Gothic bold", 10), bg="black", fg="white",
                             activebackground='Black',
                             activeforeground='White', cursor='hand2', command=self.open_add_manager_page)
        self.submit.place(x=180, y=230, width="250", height="50")

        self.submit = Button(self.f, text="Add Aircraft", font=("Century Gothic bold", 10), bg="black", fg="white",
                             activebackground='Black',
                             activeforeground='White', cursor='hand2', command=self.open_add_aircraft_page)
        self.submit.place(x=550, y=230, width="250", height="50")

        self.submit = Button(self.f, text="Manage Manager", font=("Century Gothic bold", 10), bg="black", fg="white",
                             activebackground='Black',
                             activeforeground='White', cursor='hand2', command=self.open_manage_managers_page)
        self.submit.place(x=180, y=310, width="250", height="50")

        self.submit = Button(self.f, text="Manage Aircraft", font=("Century Gothic bold", 10), bg="black", fg="white",
                             activebackground='Black',
                             activeforeground='White', cursor='hand2', command=self.open_manage_aircraft_page)
        self.submit.place(x=550, y=310, width="250", height="50")

        self.submit = Button(self.f, text="Add Airline", font=("Century Gothic bold", 10), bg="black", fg="white",
                             activebackground='Black',
                             activeforeground='White', cursor='hand2', command=self.open_add_airlines_page)
        self.submit.place(x=180, y=390, width="250", height="50")

        self.submit = Button(self.f, text="All Bookings", font=("Century Gothic bold", 10), bg="black", fg="white",
                             activebackground='Black',
                             activeforeground='White', cursor='hand2', command=self.open_all_bookings_page)
        self.submit.place(x=550, y=390, width="250", height="50")

        self.submit = Button(self.f, text="Manage Airline", font=("Century Gothic bold", 10), bg="black", fg="white",
                             activebackground='Black',
                             activeforeground='White', cursor='hand2', command=self.open_manage_airline_page)
        self.submit.place(x=180, y=470, width="250", height="50")

        self.submit = Button(self.f, text="Logout", font=("Century Gothic bold", 10), bg="black", fg="white",
                             activebackground='Black',
                             activeforeground='White', cursor='hand2', command=self.logout_admin)
        self.submit.place(x=550, y=470, width="250", height="50")
        self.t.mainloop()

    def open_add_manager_page(self):
        a = add_manager.AddManager()
        a.widgets()

    def open_manage_managers_page(self):
        a = manage_managers.ManageManager()
        a.widgets()

    def open_add_airlines_page(self):
        a = add_airlines.AddAirlines()
        a.widgets()

    def open_manage_airline_page(self):
        a = manage_airline.ManageAirline()
        a.widgets()

    def open_add_aircraft_page(self):
        a = add_aircraft.AddAircraft()
        a.widgets()

    def open_manage_aircraft_page(self):
        a = manage_aircrafts.ManageAircraft()
        a.widgets()

    def open_all_bookings_page(self):
        a = all_bookings.AllBookings()
        a.widgets()

    def logout_admin(self):
        choice = messagebox.askyesno("Alert", "Do you really want to logout from your session?")
        if choice:
            messagebox.showinfo("Message", "Logout Successfully")
            self.t.destroy()
            d = admin_login_page.AdminLogin()
            d.widgets()


if __name__ == "__main__":
    a = AdminDashboard()
    a.widgets()
