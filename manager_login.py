from tkinter import *
from . import database, manager_dashboard
from tkinter import messagebox
from PIL import Image, ImageTk


class ManagerLogin:
    def __init__(self):
        self.t = Tk()
        self.t.title("Manager Panel | Airline Reservation | Login Page")
        self.fullwidth = self.t.winfo_screenwidth()
        self.fullheight = self.t.winfo_screenheight()
        self.width = int((self.fullwidth - 800) / 2)
        self.height = int((self.fullheight - 600) / 2) - 40
        s = "800x600+" + str(self.width) + "+" + str(self.height)
        self.t.geometry(s)
        self.icon = PhotoImage(file="icn2.png")
        self.t.iconphoto(False, self.icon)

    def widgets(self):
        self.image_path = Image.open('manager/images/img1.jpg')
        self.image = self.image_path.resize((800, 600))
        self.background_image = ImageTk.PhotoImage(self.image)
        print("Image path:- ", self.image_path)

        self.i = Canvas(self.t, width='800', height='600')
        self.i.place(x=0, y=0)
        self.i.create_image('0', '0', image=self.background_image, anchor=NW)

        self.i.create_text(420, 60, text='Manager Panel', font=("Century Gothic bold", 20), fill="Black")

        self.f = Frame(self.t, bg="black")
        self.f.place(x=250, y=130, width="350", height="350")

        self.email_label = Label(self.t, text="Enter Your Email", bg="black", fg="white", font=(3))
        self.email_label.place(x=300, y=170)

        self.email = Entry(self.t, font=("Century Gothic", 12), bd=3, relief=SOLID, borderwidth=1)
        self.email.place(x=300, y=210, width="250", height="30")

        self.password_label = Label(self.t, text="Enter Your Password", bg="black", fg="white", font=(3))
        self.password_label.place(x=300, y=280)

        self.password = Entry(self.t, font=("Century Gothic", 12), show="*", bd=3, relief=SOLID, borderwidth=1)
        self.password.place(x=300, y=320, width="250", height="30")

        self.submit = Button(self.t, text="Login Here", bg="black", fg="white", font=("Century Gothic", 12),
                             activebackground='Black',
                             activeforeground='White', cursor='hand2', command=self.add_data)
        self.submit.place(x=300, y=390, width="250", height="35")

        self.t.mainloop()

    def add_data(self):
        email = self.email.get()
        password = self.password.get()
        print("Username:", email, "Password:", password)

        if email == "":
            messagebox.showwarning("Alert", "Please enter the email first")
        elif password == "":
            messagebox.showwarning("Alert", "Please enter the password first")
        else:
            data = (email, password)
            result = database.manager_login(data)

            if result:
                messagebox.showinfo("Info", "Login Successfully")
                self.t.destroy()
                a = manager_dashboard.ManagerDashboard(result)
                a.widgets()
            else:
                messagebox.showerror("Alert", "Wrong username or Password")


if __name__ == "__main__":
    a = ManagerLogin()
    a.widgets()
