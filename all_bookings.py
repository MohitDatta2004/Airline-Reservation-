from tkinter import *
from tkinter.ttk import Treeview
from tkinter import messagebox
from . import database
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter.ttk import Combobox


class AllBookings:
    def __init__(self):
        self.t = Toplevel()
        self.t.title("All Bookings | Airline Reservation | Admin Panel")
        self.fullwidth = self.t.winfo_screenwidth()
        self.fullheight = self.t.winfo_screenheight()
        self.width = int((self.fullwidth - 800) / 2)
        self.height = int((self.fullheight - 500) / 2) - 40
        s = "800x500+" + str(self.width) + "+" + str(self.height)
        self.t.geometry(s)
        self.icon = PhotoImage(file="admin/images/icn2.png")
        self.t.iconphoto(False, self.icon)

    def widgets(self):
        self.image_path = Image.open('admin/images/img6.jpg')
        self.image = self.image_path.resize((800, 500))
        self.background_image = ImageTk.PhotoImage(self.image)
        print("Image path:- ", self.image_path)

        self.i = Canvas(self.t, width='800', height='500')
        self.i.place(x='0', y='0')
        self.i.create_image('0', '0', image=self.background_image, anchor=NW)

        self.i.create_text(400, 50, text='ALL BOOKINGS DETAILS', fill='Black',
                           font=("Century Gothic bold", 20))

        self.i.create_text(550, 80, text='Filter By', fill='Black',
                           font=("Century Gothic bold", 15))
        self.selected_status = Combobox(self.t, values=["All", "Pending", "Confirmed"], state="readonly", width=16,
                                        font=("Century Gothic", 10))
        self.selected_status.place(x=600, y=70)
        self.selected_status.bind("<<ComboboxSelected>>", self.get_selected_value)

        self.f = Frame(self.t, width='700', height='350')
        self.f.place(x=50, y=100)

        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Century Gothic', 10))
        style.configure("mystyle.Treeview.Heading", font=('Century Gothic bold', 10, 'bold'))

        self.tr = Treeview(self.f,
                           columns=(
                               "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q"),
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

        self.tr.heading("#17", text="ACTION")
        self.tr.column("#17", minwidth=100, width=250, stretch=True, anchor=CENTER)

        data = database.get_all_bookings()
        for i in data:
            self.tr.insert("", 0, text=i[0],
                           values=(
                               i[1], i[2], i[3], i[4], i[5], i[6], f"Rs.{i[7]}", i[8], f"Rs.{i[9]}", i[10], i[11],
                               i[12],
                               i[13],
                               i[14],
                               i[15],
                               i[16],
                               "Booking Confirmed"))

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

        if column == "#17":
            choice = messagebox.askyesno("Alert", "Press yes to confirmed booking.")
            if choice:
                data = ("Confirmed", r_id[0])
                result = database.confirm_booking(data)
                if result:
                    messagebox.showinfo("Message", "Booking Confirmed.")
                    self.t.destroy()
                    a = AllBookings()
                    a.widgets()
                else:
                    messagebox.showwarning("Alert", "Something went wrong")
                    self.t.destroy()
                    a = AllBookings()
                    a.widgets()

    def get_selected_value(self, e):
        self.tr.delete(*self.tr.get_children())
        selected_value = self.selected_status.get()

        if selected_value == "All":
            data = database.get_all_bookings()
        else:
            data = database.get_all_filtered_bookings((selected_value,))

        for i in data:
            self.tr.insert("", 0, text=i[0],
                           values=(
                               i[1], i[2], i[3], i[4], i[5], i[6], f"Rs.{i[7]}", i[8], f"Rs.{i[9]}", i[10], i[11],
                               i[12],
                               i[13],
                               i[14],
                               i[15],
                               i[16],
                               "Booking Confirmed"))


if __name__ == "__main__":
    a = AllBookings()
    a.widgets()
