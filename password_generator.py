import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meets_criteria = False
    has_numbers = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char
        if new_char in digits:
            has_numbers = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_numbers
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd

# Function to handle the button click event
def on_generate():
    try:
        min_length = int(entry_min_length.get())
        numbers = var_numbers.get() == 1
        special_characters = var_special_characters.get() == 1

        password = generate_password(min_length, numbers, special_characters)
        messagebox.showinfo("Generated Password", f"Your password is: {password}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for the minimum length")

# Create the main application window
root = tk.Tk()
root.title("Password Generator")

# Create and place widgets
label_min_length = tk.Label(root, text="Enter the minimum length of the password:")
label_min_length.pack()

entry_min_length = tk.Entry(root)
entry_min_length.pack()

var_numbers = tk.IntVar()
check_numbers = tk.Checkbutton(root, text="Include numbers", variable=var_numbers)
check_numbers.pack()

var_special_characters = tk.IntVar()
check_special_characters = tk.Checkbutton(root, text="Include special characters", variable=var_special_characters)
check_special_characters.pack()

button_generate = tk.Button(root, text="Generate Password", command=on_generate)
button_generate.pack()

# Run the application
root.mainloop()
