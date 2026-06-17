from tkinter import *
from . import database, manage_managers
from tkinter import messagebox
from PIL import Image, ImageTk


class AddManager:
    def __init__(self, data=""):
        print("Data:-", data)
        self.data = data

        self.t = Toplevel()
        if self.data == "":
            self.t.title("Add Manager | Airline Reservation | Admin Panel")
        else:
            self.t.title("Update Manager | Airline Reservation | Admin Panel")

        self.fullwidth = self.t.winfo_screenwidth()
        self.fullheight = self.t.winfo_screenheight()
        self.width = int((self.fullwidth - 800) / 2)
        self.height = int((self.fullheight - 500) / 2) - 40
        s = "800x500+" + str(self.width) + "+" + str(self.height)
        self.t.geometry(s)
        self.t.config(bg="grey")
        self.icon = PhotoImage(file="admin/images/icn2.png")
        self.t.iconphoto(False, self.icon)

    def widgets(self):
        self.f = Frame(self.t, bg='Orange')
        self.f.place(x=0, y=0, width='800', height='500')

        self.image_path = Image.open('admin/images/img5.jpg')
        self.image = self.image_path.resize((800, 500))
        self.background_image = ImageTk.PhotoImage(self.image)
        print("Image path:- ", self.image_path)

        self.i = Canvas(self.f, width='800', height='500')
        self.i.place(x='0', y='0')
        self.i.create_image('0', '0', image=self.background_image, anchor=NW)

        if self.data == "":
            self.i.create_text(420, 40, text='ADD MANAGER DETAILS', font=("Century Gothic bold", 20))
        else:
            self.i.create_text(420, 40, text='UPDATE MANAGER DETAILS', font=("Century Gothic bold", 20))

        self.i.create_text(130, 100, text='Name', font=("Century Gothic bold", 15))
        self.name = Entry(self.f, bg="white", fg="black", font=("Century Gothic", 12), bd=3, relief=SOLID,
                          borderwidth=1)
        self.name.place(x=100, y=120, width="220", height="30")

        self.i.create_text(550, 100, text='Phone Number', font=("Century Gothic bold", 15))
        self.phone = Entry(self.f, bg="white", fg="black", font=("Century Gothic", 12), bd=3, relief=SOLID,
                           borderwidth=1)
        self.phone.place(x=480, y=120, width="220", height="30")

        self.i.create_text(130, 180, text='Email', font=("Century Gothic bold", 15))
        self.email = Entry(self.f, bg="white", fg="black", font=("Century Gothic", 12), bd=3, relief=SOLID,
                           borderwidth=1)
        self.email.place(x=100, y=200, width="220", height="30")

        self.i.create_text(525, 180, text='Password', font=("Century Gothic bold", 15))
        self.password = Entry(self.f, bg="white", fg="black", font=("Century Gothic", 12), bd=3, relief=SOLID,
                              borderwidth=1)
        self.password.place(x=480, y=200, width="220", height="30")

        self.i.create_text(140, 280, text='Address', font=("Century Gothic bold", 15))
        self.address = Text(self.f, bg="white", fg="black", font=("Century Gothic", 12), bd=3, relief=SOLID,
                            borderwidth=1)
        self.address.place(x=100, y=300, width="600", height="100")

        if self.data == "":
            self.submit = Button(self.f, text="Submit", bg='Black', fg='White', width='20',
                                 font=("Century Gothic bold", 12), command=self.add_data)
            self.submit.place(x=280, y=430, width="250", height="30")
        else:
            result = self.data.get("values")
            print("Result:-", result)
            self.name.insert(0, result[0])
            self.phone.insert(1, result[1])
            self.email.insert(2, result[2])
            self.password.insert(3, result[3])
            self.address.insert("1.0", result[4])
            self.submit = Button(self.t, text="Update", bg='Black', fg='White', width='20',
                                 font=("Century Gothic bold", 12), command=self.update_entered_data)
            self.submit.place(x=280, y=430, width="250", height="30")

        self.t.mainloop()

    def add_data(self):
        name = self.name.get()
        phone_number = self.phone.get()
        email = self.email.get()
        password = self.password.get()
        address = self.address.get("1.0", "end-1c")

        if name == "":
            messagebox.showwarning("Alert", "Please enter the name first.")
        elif phone_number == "":
            messagebox.showwarning("Alert", "Please enter your phone number first.")
        elif email == "":
            messagebox.showwarning("Alert", "Please enter your email first.")
        elif password == "":
            messagebox.showwarning("Alert", "Please enter your password first.")
        elif address == "":
            messagebox.showwarning("Alert", "Please enter your address first.")
        else:
            print("Name:-", name, "Phone Number:-", phone_number, "Email:-", email, "Password:-", password, "Address:-",
                  address)
            data = (name, phone_number, email, password, address)
            result = database.add_manager_data(data)
            if result:
                messagebox.showinfo("Message", "Manager details added successfully")
                self.t.destroy()
                r = manage_managers.ManageManager()
                r.widgets()
            else:
                messagebox.showerror("Alert", "Something went wrong.")

    def update_entered_data(self):
        name = self.name.get()
        phone_number = self.phone.get()
        email = self.email.get()
        password = self.password.get()
        address = self.address.get("1.0", "end-1c")

        if name == "":
            messagebox.showwarning("Alert", "Please enter the name first.")
        elif phone_number == "":
            messagebox.showwarning("Alert", "Please enter your phone number first.")
        elif email == "":
            messagebox.showwarning("Alert", "Please enter your email first.")
        elif password == "":
            messagebox.showwarning("Alert", "Please enter your password first.")
        elif address == "":
            messagebox.showwarning("Alert", "Please enter your address first.")
        else:
            print("Name:", name, "Phone Number:-", phone_number, "Email:-", email, "Password:-", password, "Address:-",
                  address)
            updated_data = (name, phone_number, email, password, address, self.data.get("text"))
            result = database.update_manager_data(updated_data)
            if result:
                messagebox.showinfo("Message", "Manager details updated successfully")
                self.t.destroy()
                a = manage_managers.ManageManager()
                a.widgets()
            else:
                messagebox.showwarning("Alert", "Something went wrong")


if __name__ == "__main__":
    a = AddManager()
    a.widgets()
