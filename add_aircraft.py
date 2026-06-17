from tkinter import *
from . import database, manage_aircrafts
from tkinter import messagebox
from tkinter.ttk import Combobox
from PIL import Image, ImageTk


class AddAircraft:
    def __init__(self, data=""):
        print("Data:", data)
        self.data = data
        self.t = Toplevel()

        if self.data == "":
            self.t.title("Add Aircraft | Airline Reservation | Admin Panel")
        else:
            self.t.title("Update Aircraft | Airline Reservation | Admin Panel")

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

        self.image_path = Image.open('admin/images/img3.jpg')
        self.image = self.image_path.resize((800, 500))
        self.background_image = ImageTk.PhotoImage(self.image)
        print("Image path:- ", self.image_path)

        self.i = Canvas(self.f, width='800', height='500')
        self.i.place(x='0', y='0')
        self.i.create_image('0', '0', image=self.background_image, anchor=NW)

        if self.data == "":
            self.i.create_text(420, 40, text='ADD AIRCRAFT DETAILS', font=("Century Gothic bold", 20))
        else:
            self.i.create_text(420, 40, text='UPDATE AIRCRAFT DETAILS', font=("Century Gothic bold", 20))

        self.i.create_text(150, 100, text='Aircraft ID', font=("Century Gothic bold", 15))
        self.aircraft_id = Entry(self.f, bg="White", fg="black", font=("Century Gothic", 12), bd=3, relief=SOLID,
                                 borderwidth=1)
        self.aircraft_id.place(x=100, y=120, width="220", height="30")

        self.i.create_text(510, 100, text='Model', font=("Century Gothic bold", 15))
        self.model = Entry(self.f, bg="white", fg="black", font=("Century Gothic", 12), bd=3, relief=SOLID,
                           borderwidth=1)
        self.model.place(x=480, y=120, width="220", height="30")

        self.i.create_text(185, 180, text='Seating Capacity', font=("Century Gothic bold", 15))
        self.sitting_capacity = Entry(self.f, bg="white", fg="black", font=("Century Gothic", 12), bd=3, relief=SOLID,
                                      borderwidth=1)
        self.sitting_capacity.place(x=100, y=200, width="220", height="30")

        self.i.create_text(570, 180, text='Select Engine Type', font=("Century Gothic bold", 15))
        self.engine_type_list = ["Turbo Jet", "Turbo Fans"]
        self.engine_type = Combobox(self.f, values=self.engine_type_list, state="readonly", width=18,
                                    font=("Century Gothic", 12))
        self.engine_type.place(x=480, y=200, width="220", height="30")

        self.i.create_text(240, 280, text='Other Description (Optional)', font=("Century Gothic bold", 15))
        self.other_description = Text(self.f, bg="white", fg="black", font=("Century Gothic", 12), bd=3, relief=SOLID,
                                      borderwidth=1)
        self.other_description.place(x=100, y=300, width="600", height="100")

        if self.data == "":
            self.submit = Button(self.t, text="Submit", width='20', bg='Black', fg='White',
                                 font=("Century Gothic bold", 12), command=self.add_data)
            self.submit.place(x=280, y=430, width="250", height="30")
        else:
            result = self.data.get("values")
            print("Result:", result)
            self.aircraft_id.insert(0, result[0])
            self.model.insert(1, result[1])
            self.sitting_capacity.insert(2, result[2])
            self.engine_type.set(result[3])
            self.other_description.insert("1.0", result[4])
            self.submit = Button(self.t, text="Update", width='20', bg='Black', fg='White',
                                 font=("Century Gothic bold", 12), command=self.updated_data)
            self.submit.place(x=280, y=430, width="250", height="30")

        self.t.mainloop()

    def add_data(self):
        aircraft_id = self.aircraft_id.get()
        model = self.model.get()
        sitting_capacity = self.sitting_capacity.get()
        engine_type = self.engine_type.get()
        other_description = self.other_description.get("1.0", "end-1c")

        if aircraft_id == "":
            messagebox.showwarning("Alert", "Please enter aircraft id first.")
        elif model == "":
            messagebox.showwarning("Alert", "Please enter model name first.")
        elif sitting_capacity == "":
            messagebox.showwarning("Alert", "Please enter sitting capacity first.")
        elif engine_type == "":
            messagebox.showwarning("Alert", "Please select engine type first.")
        else:
            print("Aircraft details:", aircraft_id, model, sitting_capacity, engine_type, other_description)

            if other_description == "":
                data = (aircraft_id, model, sitting_capacity, engine_type, "Not Available")
            else:
                data = (aircraft_id, model, sitting_capacity, engine_type, other_description)

            result = database.add_aircraft_data(data)
            if result:
                messagebox.showinfo("Message", "Aircraft added successfully")
                self.t.destroy()
                f = manage_aircrafts.ManageAircraft()
                f.widgets()
            else:
                messagebox.showwarning("Alert", "Something went wrong")

    def updated_data(self):
        aircraft_id = self.aircraft_id.get()
        model = self.model.get()
        sitting_capacity = self.sitting_capacity.get()
        engine_type = self.engine_type.get()
        other_description = self.other_description.get("1.0", "end-1c")

        if aircraft_id == "":
            messagebox.showwarning("Alert", "Please enter aircraft id first")
        elif model == "":
            messagebox.showwarning("Alert", "Please enter model name first.")
        elif sitting_capacity == "":
            messagebox.showwarning("Alert", "Please enter sitting capacity first.")
        elif engine_type == "":
            messagebox.showwarning("Alert", "Please select engine type first.")
        else:
            print("Aircraft details:", aircraft_id, model, sitting_capacity, engine_type, other_description)

            if other_description == "":
                updated_data = (
                    aircraft_id, model, sitting_capacity, engine_type, "Not Available", self.data.get("text"))
            else:
                updated_data = (
                    aircraft_id, model, sitting_capacity, engine_type, other_description, self.data.get("text"))

            result = database.update_aircraft_data(updated_data)
            if result:
                messagebox.showinfo("Message", "Aircraft details updated successfully")
                self.t.destroy()
                a = manage_aircrafts.ManageAircraft()
                a.widgets()
            else:
                messagebox.showwarning("Alert", "Something went wrong")


if __name__ == "__main__":
    a = AddAircraft()
    a.widgets()
