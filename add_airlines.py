from tkinter import *
from tkinter import messagebox
from . import database, manage_airline
from PIL import Image, ImageTk


class AddAirlines:
    def __init__(self, data=""):
        print("Data:-", data)
        self.data = data

        self.t = Toplevel()

        if self.data == "":
            self.t.title("Add Airline | Airline Reservation | Admin Panel")
        else:
            self.t.title("Update Airline | Airline Reservation | Admin Panel")

        self.fullwidth = self.t.winfo_screenwidth()
        self.fullheight = self.t.winfo_screenheight()
        self.width = int((self.fullwidth - 800) / 2)
        self.height = int((self.fullheight - 500) / 2) - 40
        s = "800x500+" + str(self.width) + "+" + str(self.height)
        self.t.geometry(s)
        self.icon = PhotoImage(file="admin/images/icn2.png")
        self.t.iconphoto(False, self.icon)

    def widgets(self):
        self.f = Frame(self.t, bg="white")
        self.f.place(x=0, y=0, width="800", height="500")

        self.image_path = Image.open('admin/images/img4.jpg')
        self.image = self.image_path.resize((800, 500))
        self.background_image = ImageTk.PhotoImage(self.image)
        print("Image path:- ", self.image_path)

        self.i = Canvas(self.f, width='800', height='500')
        self.i.place(x='0', y='0')
        self.i.create_image('0', '0', image=self.background_image, anchor=NW)

        if self.data == "":
            self.i.create_text(420, 40, text='ADD AIRLINE DETAILS', font=("Century Gothic bold", 20))
        else:
            self.i.create_text(420, 40, text='UPDATE AIRLINE DETAILS', font=("Century Gothic bold", 20))

        self.i.create_text(150, 100, text='Airline ID', font=("Century Gothic bold", 15))
        self.airline_id = Entry(self.f, bg="white", fg="black", font=("Century Gothic", 12), bd=3, relief=SOLID,
                                borderwidth=1)
        self.airline_id.place(x=100, y=120, width="220", height="30")

        self.i.create_text(550, 100, text='Airline Name', font=("Century Gothic bold", 15))
        self.airline_name = Entry(self.f, bg="white", fg="black", font=("Century Gothic", 12), bd=3, relief=SOLID,
                                  borderwidth=1)
        self.airline_name.place(x=480, y=120, width="220", height="30")

        self.i.create_text(170, 180, text='Founded Year', font=("Century Gothic bold", 15))
        self.founded_year = Entry(self.f, bg="white", fg="black", font=("Century Gothic", 12), bd=3, relief=SOLID,
                                  borderwidth=1)
        self.founded_year.place(x=100, y=200, width="220", height="30")

        self.i.create_text(520, 180, text='Country', font=("Century Gothic bold", 15))
        self.country = Entry(self.f, bg="white", fg="black", font=("Century Gothic", 12), bd=3, relief=SOLID,
                             borderwidth=1)
        self.country.place(x=480, y=200, width="220", height="30")

        self.i.create_text(210, 280, text='Headquarters Location', font=("Century Gothic bold", 15))
        self.headquarters_location = Text(self.f, bg="white", fg="black", font=("Century Gothic", 12), bd=3,
                                          relief=SOLID,
                                          borderwidth=1)
        self.headquarters_location.place(x=100, y=300, width="600", height="100")

        if self.data == "":
            self.submit = Button(self.t, text="Submit", width='20', bg='Black', fg='White',
                                 font=("Century Gothic bold", 12), command=self.add_data)
            self.submit.place(x=280, y=430, width="250", height="30")
        else:
            result = self.data.get("values")
            print("Result:", result)
            self.airline_id.insert(0, result[0])
            self.airline_name.insert(1, result[1])
            self.founded_year.insert(2, result[2])
            self.country.insert(3, result[3])
            self.headquarters_location.insert("1.0", result[4])
            self.submit = Button(self.t, text="Update", width='20', bg='Black', fg='White',
                                 font=("Century Gothic bold", 12), command=self.updated_entered_data)
            self.submit.place(x=280, y=430, width="250", height="30")

        self.t.mainloop()

    def add_data(self):
        airline_id = self.airline_id.get()
        airline_name = self.airline_name.get()
        founded_year = self.founded_year.get()
        country = self.country.get()
        headquarters = self.headquarters_location.get("1.0", "end-1c")

        if airline_id == "":
            messagebox.showwarning("Alert", "Please enter airline id first.")
        elif airline_name == "":
            messagebox.showwarning("Alert", "Please enter airline name first.")
        elif founded_year == "":
            messagebox.showwarning("Alert", "Please enter founded year first.")
        elif country == "":
            messagebox.showwarning("Alert", "Please enter country first.")
        elif headquarters == "":
            messagebox.showwarning("Alert", "Please enter headquarters first.")
        else:
            print("Airline details:-", airline_id, airline_name, founded_year, country, headquarters)
            data = (airline_id, airline_name, founded_year, country, headquarters)
            result = database.add_airline_data(data)
            if result:
                messagebox.showinfo("Info", "Airline details added successfully")
                self.t.destroy()
                a = manage_airline.ManageAirline()
                a.widgets()
            else:
                messagebox.showwarning("Alert", "Something went wrong")

    def updated_entered_data(self):
        airline_id = self.airline_id.get()
        airline_name = self.airline_name.get()
        founded_year = self.founded_year.get()
        country = self.country.get()
        headquarters = self.headquarters_location.get("1.0", "end-1c")

        if airline_id == "":
            messagebox.showwarning("Alert", "Please enter airline id first.")
        elif airline_name == "":
            messagebox.showwarning("Alert", "Please enter airline name first.")
        elif founded_year == "":
            messagebox.showwarning("Alert", "Please enter founded year first.")
        elif country == "":
            messagebox.showwarning("Alert", "Please enter country first.")
        elif headquarters == "":
            messagebox.showwarning("Alert", "Please enter headquarters first.")
        else:
            print("Airline details:-", airline_id, airline_name, founded_year, country, headquarters)
            updated_data = (airline_id, airline_name, founded_year, country, headquarters, self.data.get("text"))
            result = database.update_airline_data(updated_data)
            if result:
                messagebox.showinfo("Info", "Airline details updated successfully")
                self.t.destroy()
                a = manage_airline.ManageAirline()
                a.widgets()
            else:
                messagebox.showwarning("message", "Something went wrong")


if __name__ == "__main__":
    a = AddAirlines()
    a.widgets()
