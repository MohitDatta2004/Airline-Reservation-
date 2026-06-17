from tkinter import *
from tkinter.ttk import Treeview
from tkinter import ttk
from tkinter import messagebox
from . import database, add_manager
from PIL import Image, ImageTk


class ManageManager:
    def __init__(self):
        self.t = Toplevel()
        self.t.title("Manage Managers | Airline Reservations | Admin Panel")
        self.fullwidth = self.t.winfo_screenwidth()
        self.fullheight = self.t.winfo_screenheight()
        self.width = int((self.fullwidth - 800) / 2)
        self.height = int((self.fullheight - 500) / 2) - 40
        s = "800x500+" + str(self.width) + "+" + str(self.height)
        self.t.geometry(s)
        self.icon = PhotoImage(file="admin/images/icn2.png")
        self.t.iconphoto(False, self.icon)

    def widgets(self):
        self.image_path = Image.open('admin/images/img9.jpg')
        self.image = self.image_path.resize((800, 500))
        self.background_image = ImageTk.PhotoImage(self.image)
        print("Image path:- ", self.image_path)

        self.i = Canvas(self.t, width='800', height='500')
        self.i.place(x='0', y='0')
        self.i.create_image('0', '0', image=self.background_image, anchor=NW)

        self.i.create_text(430, 50, text='MANAGERS DETAILS', fill='Black',
                           font=("Century Gothic bold", 20))

        self.add_manager_button = Button(self.t, text="Add Manager", bg='Black', fg='White', width='20',
                                         font=("Century Gothic bold", 10), command=self.open_add_manager_page)
        self.add_manager_button.place(x=650, y=35, width="100", height="30")

        self.f = Frame(self.t, width='700', height='350')
        self.f.place(x=50, y=100)

        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Century Gothic', 10))
        style.configure("mystyle.Treeview.Heading", font=('Century Gothic bold', 10, 'bold'))

        self.tr = Treeview(self.f, columns=("A", "B", "C", "D", "E", "F", "G", "H"), selectmode='extended',
                           style="mystyle.Treeview")

        self.tr.heading("#0", text="ID")
        self.tr.column("#0", minwidth=100, width=100, stretch=True, anchor=CENTER)

        self.tr.heading("#1", text="NAME")
        self.tr.column("#1", minwidth=100, width=100, stretch=True, anchor=CENTER)

        self.tr.heading("#2", text="PHONE NUMBER")
        self.tr.column("#2", minwidth=100, width=100, stretch=True, anchor=CENTER)

        self.tr.heading("#3", text="EMAIL")
        self.tr.column("#3", minwidth=100, width=100, stretch=True, anchor=CENTER)

        self.tr.heading("#4", text="PASSWORD")
        self.tr.column("#4", minwidth=100, width=100, stretch=True, anchor=CENTER)

        self.tr.heading("#5", text="ADDRESS")
        self.tr.column("#5", minwidth=100, width=100, stretch=True, anchor=CENTER)

        self.tr.heading("#6", text="DELETE")
        self.tr.column("#6", minwidth=100, width=100, stretch=True, anchor=CENTER)

        self.tr.heading("#7", text="UPDATE")
        self.tr.column("#7", minwidth=100, width=100, stretch=True, anchor=CENTER)

        data = database.get_managers()
        for i in data:
            self.tr.insert("", 0, text=i[0], values=(i[1], i[2], i[3], i[4], i[5], "Delete", "Update"))

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
        print("Column", column)

        data = self.tr.item(row)
        print("Data of focused row:", data)

        r_id = (data.get("text"),)
        print("Id of focused row:", r_id)

        if column == "#6":
            choice = messagebox.askyesno("Alert", "Do you really want to delete this manager details?")
            if choice:
                result = database.delete_manager(r_id)
                if result:
                    messagebox.showinfo("Message", "Manager details deleted successfully")
                    self.t.destroy()
                    r = ManageManager()
                    r.widgets()
                else:
                    messagebox.showwarning("Alert", "Something went wrong")
        elif column == "#7":
            r = add_manager.AddManager(self.tr.item(row))
            self.t.destroy()
            r.widgets()

    def open_add_manager_page(self):
        self.t.destroy()
        a = add_manager.AddManager()
        a.widgets()


if __name__ == "__main__":
    r = ManageManager()
    r.widgets()
