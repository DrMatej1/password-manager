from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pw():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    print(f"Your password is: {password}")
    pw_e.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    ws = website_e.get()
    em = email_e.get()
    pww = pw_e.get()
    new_data = {
        ws: {
            "email": em,
            "password": pww,
        }
    }
    if len(website_e.get()) == 0 or len(pw_e.get()) == 0:
        messagebox.showinfo(title="Empty fields", message="Please fill in all fields")

    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_e.delete(0, END)
            pw_e.delete(0, END)

def searchf():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            print(data)
    except:
        pass
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
pic = Canvas(width=200, height=200)
lock = PhotoImage(file="logo.png")
pic.create_image(100, 100, image=lock)
pic.grid(row=0, column=1)
website_v = StringVar()
website = Label(text="Website:")
website_e = Entry(width=17, textvariable=website_v)
website.grid(row=1,column=0)
website_e.grid(row=1,column=1)
website_e.focus()
email_v = StringVar()
email = Label(text="Email/Username:")
email_e = Entry(width=42, textvariable=email_v)
email.grid(row=2,column=0)
email_e.grid(row=2,column=1, columnspan=2)
email_e.insert(0, "crazord@gmail.com")
pw_v = StringVar()
pw = Label(text="Password:")
pw_e = Entry(width=17, textvariable=pw_v)
pw.grid(row=3,column=0)
pw_e.grid(row=3,column=1)
pw_g = Button(text="Generate Password", command=generate_pw, width=20)
pw_g.grid(row=3,column=2)
add = Button(text="Add", width=30, command=save)
add.grid(row=4,column=1, columnspan=2)
search = Button(text="Search", width=20, command=searchf)
search.grid(row=1, column=2)
window.mainloop()