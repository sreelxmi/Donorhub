import tkinter as tk
from tkinter import *
from tkinter import ttk,filedialog
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

#community
 # Create main application window
comm= tk.Frame(base_frame)
comm.place(relheight=1, relwidth=1)

def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
    if file_path:
        image = tk.PhotoImage(file=file_path)
        image_label.config(image=image)
        image_label.image = image  # Keep a reference to avoid garbage collection

def submit_view():
    view_text = views_entry.get("1.0", "end-1c")  # Get text from the text entry
    # You can do something with the submitted view, such as print it
    print("Submitted view:", view_text)

def create_webpage():
   
    
    # Set the background color of the comm window to "indianred"
    comm.configure(background='indianred')

    # Create a custom font for the title
    title_font = ('Arial', 30, 'bold')

    # Create a frame for the title with a colored background
    title_frame = ttk.Frame(comm, style="Title.TFrame")
    title_frame.pack(pady=20)
    title_frame.grid_columnconfigure(0, weight=1)

    # Create a label for the title
    title_label = ttk.Label(title_frame, text="COMMUNITY PAGE", font=title_font)
    title_label.grid(row=0, column=0, sticky='nsew')

    # Configure a custom style for the title frame with a light blue background
    style = ttk.Style()
    style.configure("Title.TFrame", background="lightblue")

    # Essay description
    essay_text = """\
    Blood donation is a critical aspect of healthcare systems worldwide, playing a vital role in saving lives, supporting medical procedures, and maintaining public health. Each donation can help multiple individuals in need, whether they are undergoing surgery, recovering from a serious illness or injury, or living with a chronic condition. 
    By participating in blood donation initiatives, individuals can make a tangible difference in the lives of others and contribute to the well-being of their communities.

    DonorHub is an online blood donating service provider platform which aids in individuals and organizations to connect with each other during necessary times, also promoting volunteers to come forward for this righteous act of blood donation.
    """

    # Create a label for the essay description with increased font size
    essay_label = ttk.Label(comm, text=essay_text, wraplength=600, font=("Arial", 14))
    essay_label.pack(padx=20, pady=10)

    # Create a text field for users to post their views
    views_frame = ttk.Frame(comm)
    views_frame.pack(pady=10)

    post_view_label = ttk.Label(views_frame, text="POST YOUR VIEW", font=("Arial", 12, "bold"))
    post_view_label.grid(row=0, column=0, padx=5, pady=5)

    global views_entry
    views_entry = tk.Text(views_frame, height=5, width=50)
    views_entry.grid(row=1, column=0, padx=5, pady=5)

    # Create a submit button
    submit_button = ttk.Button(views_frame, text="Submit", command=submit_view)
    submit_button.grid(row=2, column=0, padx=5, pady=5)

    # Create a button to open the file dialog for image uploading
    open_button = ttk.Button(comm, text="Upload Image", command=open_image)
    open_button.pack(pady=10)

    # Create a label to display the selected image
    global image_label
    image_label = ttk.Label(comm)
    image_label.pack()

# Call the function to create the webpage
create_webpage()

# donate
donate = tk.Frame(base_frame)
donate.place(relheight=1, relwidth=1)

def search_slot():
    # Placeholder function for search functionality
    print("Search slot functionality to be implemented.")

# Set window size
window_width = 400
window_height = 200
screen_width = donate.winfo_screenwidth()
screen_height = donate.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))
root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))

# Title label
title_label = ttk.Label(donate, text="Donate Blood", font=("Helvetica", 18))
title_label.pack(pady=10)

# Location label and entry
location_label = ttk.Label(donate, text="Preferred Location:")
location_label.pack()
location_entry = ttk.Entry(donate)
location_entry.pack(pady=5)

# Date label and entry
date_label = ttk.Label(donate, text="Date:")
date_label.pack()
date_entry = ttk.Entry(donate)
date_entry.pack(pady=5)

# Time label and entry
time_label = ttk.Label(donate, text="Time:")
time_label.pack()
time_entry = ttk.Entry(donate)
time_entry.pack(pady=5)

# Search Slot button
search_button = ttk.Button(donate, text="Search Slot", command=search_slot)
search_button.pack(pady=10)

back_button = ttk.Button(donate, text="Back", command=lambda: go_back(donate), style="Custom.TButton")
back_button.pack(pady=10)

# findadonor
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

# main page
main = tk.Frame(base_frame)
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

community_page_btn = tk.Button(main, text="Community Page", command=lambda: [community_page(), show_frame(comm)])
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
