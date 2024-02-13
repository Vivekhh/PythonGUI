import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import re

def validate_student_name():
    student_name = entry_name.get()
    if not student_name.strip():
        messagebox.showerror("Error", "Please enter a student name.")
        return False
    if not re.match(r'^[a-zA-Z\s]+$', student_name):
        messagebox.showerror("Error", "Student name should not contain numbers or special characters.")
        return False
    return True

def validate_gender():
    gender = entry_gender.get()
    if not gender:
        #messagebox.showerror("Error", "Please select a gender.")
        return False
    if gender.lower() not in ('male', 'female', 'others', 'prefer not to specify'):
        messagebox.showerror("Error", "Invalid gender. Please enter 'Male', 'Female', 'Others', or 'Prefer not to specify'.")
        return False
    return True

def validate_date_of_birth():
    date_of_birth = entry_dob.get()
    if not date_of_birth.strip():
        #messagebox.showerror("Error", "Please enter a date of birth.")
        return False
    if not re.match(r'^\d{2}/\d{2}/\d{4}$', date_of_birth):
        messagebox.showerror("Error", "Date of birth should be in DD/MM/YYYY format.")
        return False
    return True

def validate_email():
    email = entry_email.get()
    if not email.strip() or not validate_email_format(email):
        messagebox.showerror("Error", "Please enter a valid email address.")
        return False
    return True

def validate_email_format(email):
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)

def validate_course():
    course_selected = course.get()
    if not course_selected:
        messagebox.showerror("Error", "Please select a course.")
        return False
    return True

def submit_form():
    if (
        validate_student_name() and
        validate_gender() and
        validate_date_of_birth() and
        validate_email() and
        validate_course()
    ):
        # Process and use the data here
        student_name = entry_name.get()
        gender = entry_gender.get()
        date_of_birth = entry_dob.get()
        email = entry_email.get()
        course_selected = course.get()
        
        print(f"Student Name: {student_name}")
        print(f"Gender: {gender}")
        print(f"Date of Birth: {date_of_birth}")
        print(f"Email: {email}")
        print(f"Course: {course_selected}")

root = tk.Tk()
root.title('Form')
root.geometry('500x400')

# Creating labels and entry fields using grid
label1 = tk.Label(root, text='Student Application Form', font=('Arial', 16))
label1.grid(row=0, column=0, columnspan=2, pady=10)  # Span 2 columns for a centered title

label2 = tk.Label(root, text='Student name', anchor='w')
label2.grid(row=1, column=0, padx=10, sticky='w')  # Align to the left
entry_name = tk.Entry(root, validate="focusout", validatecommand=validate_student_name)
entry_name.grid(row=1, column=1, padx=10)

label3 = tk.Label(root, text='Gender', anchor='w')
label3.grid(row=2, column=0, padx=10, sticky='w')  # Align to the left
entry_gender = tk.Entry(root, validate="focusout", validatecommand=validate_gender)
entry_gender.grid(row=2, column=1, padx=10)

label4 = tk.Label(root, text='Date of Birth (DD/MM/YYYY)', anchor='w')
label4.grid(row=3, column=0, padx=10, sticky='w')  # Align to the left
entry_dob = tk.Entry(root, validate="focusout", validatecommand=validate_date_of_birth)
entry_dob.grid(row=3, column=1, padx=10)

label5 = tk.Label(root, text='Email', anchor='w')
label5.grid(row=4, column=0, padx=10, sticky='w')  # Align to the left
entry_email = tk.Entry(root, validate="focusout", validatecommand=validate_email)
entry_email.grid(row=4, column=1, padx=10)

# Combobox for selecting a course
course_label = tk.Label(root, text='Select a Course', anchor='w')
course_label.grid(row=5, column=0, padx=10, sticky='w')  # Align to the left
courses = ('Python', 'Django', 'Machine learning')
course = ttk.Combobox(root, values=courses)
course.grid(row=5, column=1, padx=10)

# Submit button
submit_button = tk.Button(root, text='Submit', command=submit_form)
submit_button.grid(row=6, column=0, columnspan=2, pady=10)  # Span 2 columns for a centered button

root.mainloop()
