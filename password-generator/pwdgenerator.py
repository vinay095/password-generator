from tkinter import *
import string
import random
import pyperclip

def generator():
    small = string.ascii_lowercase
    capital = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    combine = small + capital + digits + special
    
    password_length = int(length_box.get())

    pin = ''.join(random.choices(combine, k=password_length))

    pwdField.delete(0, END) 
    pwdField.insert(0, pin)

    # Check password strength and update strength indicator
    strength = check_password_strength(pin)
    update_strength_bar(strength)

def check_password_strength(password):
    length_score = min(len(password) / 20, 1.0)  # Normalize length score
    complexity_score = sum(c in string.punctuation or c in string.ascii_letters or c in string.digits for c in password) / len(password)
    return (length_score + complexity_score) / 2  # Average of length and complexity scores

def update_strength_bar(strength):
    strength_canvas.delete("all")

    if strength < 0.4:
        color = "red"
    elif strength < 0.7:
        color = "orange"
    else:
        color = "green"

    bar_width = 200
    bar_height = 10
    strength_canvas.create_rectangle(10, 10, 10 + bar_width * strength, 10 + bar_height, fill=color, outline="")

def copy():
    newpwd = pwdField.get()
    pyperclip.copy(newpwd)

root = Tk()
# root.iconbitmap('')       can change the leaf icon
root.title('Password Generator')
F = ('arial', 13, 'bold')
root.geometry("400x500")

pwdLabel = Label(root, text="Password Generator", font=("Consolas", 20, 'bold'))
pwdLabel.grid(row=0, column=0, columnspan=2, pady=20)  # Centered and spanning two columns

lengthLabel = Label(root, text='Length:', font=F)
lengthLabel.grid(row=1, column=0, padx=(50, 1), pady=5)  # Adjusted padx to reduce gap

length_box = Spinbox(root, from_=10, to_=24, width=10, font=F)
length_box.grid(row=1, column=1,)

strength_label = Label(root, text='Strength:', font=F)
strength_label.grid(row=2, column=0, pady=5, sticky=E)

# Canvas for strength indicator
strength_canvas = Canvas(root, width=220, height=20)
strength_canvas.grid(row=2, column=1, pady=5, sticky=W)

generate = Button(root, text='Generate Password', font=F, command=generator)
generate.grid(row=3, column=0, columnspan=2, pady=10)

pwdField = Entry(root, width=25, bd=2, font='consolas')
pwdField.grid(row=4, column=0, columnspan=2, pady=5, padx=10)

copy_button = Button(root, text='Copy', font=F, command=copy)
copy_button.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
