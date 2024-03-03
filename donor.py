import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import re

conn = mysql.connector.connect(host='localhost', password='Sree@2004', user='root')
cur = conn.cursor()

root = tk.Tk()
root.title("DONORHUB")
root.geometry("500x600")

def show_frame(frame):
    frame.tkraise()

def go_back(frame):
    frame.destroy()

base_frame = tk.Frame(root)
base_frame.place(relheight=1, relwidth=1)

#donate
donate = tk.Frame(base_frame)
donate.place(relheight=1, relwidth=1)
def search_slot():
    location = location_entry.get()
    preferred_date = preferred_date_entry.get()

    # Add your search slot logic here
    print("Location:", location)
    print("Preferred Date:", preferred_date)

location_label = ttk.Label(donate, text="Location:")
location_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
location_entry = ttk.Entry(donate, width=30)
location_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

preferred_date_label = ttk.Label(donate, text="Preferred Date:")
preferred_date_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
preferred_date_entry = ttk.Entry(donate, width=30)
preferred_date_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

search_button = ttk.Button(donate, text="Search Slot", command=search_slot)
search_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

table_headers = ["Location", "Date", "Time Slot"]
for i, header in enumerate(table_headers):
    label = ttk.Label(donate, text=header)
    label.grid(row=1, column=i, padx=10, pady=5)
donate.grid_rowconfigure(0, weight=1)
donate.grid_columnconfigure(0, weight=1)

#findadonor
find = tk.Frame(base_frame)
find.place(relheight=1, relwidth=1)

def submit():
    name = name_entry.get()
    gender = gender_combobox.get()
    blood_type = blood_combobox.get()
    age = age_entry.get()
    weight = weight_entry.get()
    phone = phone_entry.get()
    hospital = hospital_entry.get()
    pin = pin_entry.get()
    district = district_entry.get()

    print(f"Name: {name}, Gender: {gender}, Blood Type: {blood_type}, Age: {age}, Weight: {weight}, Phone: {phone}, Hospital: {hospital}")

def validate_phone_number(new_value):
    return re.match(r"^\d*$", new_value) is not None or new_value == ""

custom_font = ('Arial', 15)

title_label = tk.Label(find, text="FILL OUT THE DETAILS", font=("Arial", 20, "bold"))
title_label.pack(padx=20, pady=(10, 20))

name_label = ttk.Label(find, text="Name:", font=custom_font)
name_label.pack()
name_entry = ttk.Entry(find, font=custom_font)
name_entry.pack()

gender_label = ttk.Label(find, text="Gender:", font=custom_font)
gender_label.pack()
gender_combobox = ttk.Combobox(find, values=["Male", "Female", "Other"], font=custom_font)
gender_combobox.pack()

blood_type_label = ttk.Label(find, text="Blood Type:", font=custom_font)
blood_type_label.pack()
blood_combobox = ttk.Combobox(find, values=["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"], font=custom_font)
blood_combobox.pack()

age_label = ttk.Label(find, text="Age:", font=custom_font)
age_label.pack()
age_entry = ttk.Entry(find, font=custom_font)
age_entry.pack()

weight_label = ttk.Label(find, text="Weight (kg):", font=custom_font)
weight_label.pack()
weight_entry = ttk.Entry(find, font=custom_font)
weight_entry.pack()

phone_label = ttk.Label(find, text="Phone No.:", font=custom_font)
phone_label.pack()
validate_phone = root.register(validate_phone_number)
phone_entry = ttk.Entry(find, font=custom_font, validate="key", validatecommand=(validate_phone, "%P"))
phone_entry.pack()

hospital_label = ttk.Label(find, text="Hospital:", font=custom_font)
hospital_label.pack()
hospital_entry = ttk.Entry(find, font=custom_font)
hospital_entry.pack()

district_label = ttk.Label(find, text="District:", font=custom_font)
district_label.pack()
district_entry = ttk.Entry(find, font=custom_font)
district_entry.pack()

pin_label = ttk.Label(find, text="Pin Code:", font=custom_font)
pin_label.pack()
pin_entry = ttk.Entry(find, font=custom_font)
pin_entry.pack()

submit_button = ttk.Button(find, text="Submit", command=submit)
submit_button.pack()

back_button = ttk.Button(find, text="Back", command=lambda: go_back(find), style="Custom.TButton")
back_button.pack()

#main page
main= tk.Frame(base_frame)
main.place(relheight=1, relwidth=1)

def find_donor():
    print("Find Donor button clicked")

def donate_blood():
    print("Donate Blood button clicked")

def community_page():
    print("Community Page button clicked")

find_donor_btn = tk.Button(main, text="Find Donor", command=lambda: [find_donor(), show_frame(find)])
find_donor_btn.pack(fill=tk.BOTH, padx=10, pady=5)

donate_blood_btn = tk.Button(main, text="Donate Blood", command=lambda: [donate_blood(), show_frame(donate)])
donate_blood_btn.pack(fill=tk.BOTH, padx=10, pady=5)

community_page_btn = tk.Button(main, text="Community Page", command=community_page)
community_page_btn.pack(fill=tk.BOTH, padx=10, pady=5)

# login page
login = tk.Frame(base_frame)
login.place(relheight=1, relwidth=1)

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)

def sign_up():
    try:
        name = name_entry.get()
        if not name.replace(" ", "").isalpha():
            raise ValueError("Name must contain only alphabets")

        age = age_entry.get()
        if not age.isdigit():
            raise ValueError("Age must be a number")
        age = int(age)

        phone = phone_entry.get()

        email = email_entry.get()
        if not validate_email(email):
            raise ValueError("Invalid email address")

        state = state_entry.get()
        district = district_entry.get()
        blood_group = blood_group_var.get()
        password = password_entry.get()

        print("Name:", name)
        print("Age:", age)
        print("Phone:", phone)
        print("Email:", email)
        print("State:", state)
        print("District:", district)
        print("Blood Group:", blood_group)
        print("Password:", password)

        messagebox.showinfo("Success", "Sign up successful!")

    except ValueError as ve:
        messagebox.showerror("Error", str(ve))
    except Exception as e:
        messagebox.showerror("Error", str(e))

def clear_entries():
    name_entry.delete(0, END)
    age_entry.delete(0, END)
    phone_entry.delete(0, END)
    email_entry.delete(0, END)
    state_entry.delete(0, END)
    district_entry.delete(0, END)
    password_entry.delete(0, END)

tk.Label(login, text="Name:", justify="center", width=10).pack()
name_entry = tk.Entry(login, width=50)
name_entry.pack()

tk.Label(login, text="Age:", justify="center", width=10).pack()
age_entry = tk.Entry(login, width=50)
age_entry.pack()

tk.Label(login, text="Phone:", justify="center", width=10).pack()
phone_entry = tk.Entry(login, width=50)
phone_entry.pack()

tk.Label(login, text="Email:", justify="center", width=10).pack()
email_entry = tk.Entry(login, width=50)
email_entry.pack()

tk.Label(login, text="State:", justify="center", width=10).pack()
state_entry = tk.Entry(login, width=50)
state_entry.pack()

tk.Label(login, text="District:", justify="center", width=10).pack()
district_entry = tk.Entry(login, width=50)
district_entry.pack()

tk.Label(login, text="Blood Group:", justify="center", width=10).pack()
blood_group_var = StringVar(root)
blood_group_var.set("A+")
blood_group_dropdown = OptionMenu(login, blood_group_var, "A+", "B+", "AB+", "O+", "A-", "B-", "AB-", "O-")
blood_group_dropdown.pack()

tk.Label(login, text="Password:", justify="center", width=10).pack()
password_entry = tk.Entry(login, show="*", width=50)
password_entry.pack()

sign_up_button = tk.Button(login, text="Sign Up", command=lambda: [sign_up(), show_frame(main)])
sign_up_button.pack()

clear_button = tk.Button(login, text="Clear", command=clear_entries)
clear_button.pack()

for child in login.winfo_children():
    child.pack(padx=5)

# homepage
home = tk.Frame(base_frame)
home.place(relheight=1, relwidth=1)

show_frame(home)

image_path = PhotoImage(file=r"C:\Users\sreea\OneDrive\Desktop\project\Donorhub\bg.png")
bg_image = Label(home, image=image_path)
bg_image.place(relheight=1, relwidth=1)

lbl = Label(home, text="DONOR HUB", bg="LightSkyBlue1", fg="red2", font=("Times New Roman", 58, "bold"),
            justify="right")
lbl.place(relx=0.3, rely=0.2, x=400, y=4)

donate_button = Button(home, text="DONATE", font=("Times New Roman", 25), command=lambda: show_frame(login))
donate_button.place(relx=0.7, rely=0.5)

root.mainloop()
