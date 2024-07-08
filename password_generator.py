import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password(min_length, num_numbers, num_special_characters):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    # Initialize password with random letters
    pwd = ''.join(random.choice(letters) for _ in range(min_length - num_numbers - num_special_characters))

    # Add specified number of random numbers
    pwd += ''.join(random.choice(digits) for _ in range(num_numbers))

    # Add specified number of random special characters
    pwd += ''.join(random.choice(special) for _ in range(num_special_characters))

    # Shuffle the password to mix characters, numbers, and special characters
    pwd_list = list(pwd)
    random.shuffle(pwd_list)
    pwd = ''.join(pwd_list)

    return pwd

# Function to handle the button click event
def on_generate():
    try:
        min_length = int(entry_min_length.get())
        num_numbers = int(entry_num_numbers.get())
        num_special_characters = int(entry_num_special_characters.get())
        password_name = entry_password_name.get().strip()

        if not password_name:
            messagebox.showerror("Input Error", "Please enter a name for the password")
            return

        password = generate_password(min_length, num_numbers, num_special_characters)
        with open("passwords.txt", "a") as file:
            file.write(f"{password_name}: {password}\n")

        messagebox.showinfo("Generated Password", f"Your password '{password_name}' is: {password}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for the inputs")

# Create the main application window
root = tk.Tk()
root.title("Password Generator")

# Create and place widgets
label_password_name = tk.Label(root, text="Enter the name for the password:")
label_password_name.pack()

entry_password_name = tk.Entry(root)
entry_password_name.pack()

label_min_length = tk.Label(root, text="Enter the minimum length of the password:")
label_min_length.pack()

entry_min_length = tk.Entry(root)
entry_min_length.pack()

label_num_numbers = tk.Label(root, text="Enter the number of numbers to include:")
label_num_numbers.pack()

entry_num_numbers = tk.Entry(root)
entry_num_numbers.pack()

label_num_special_characters = tk.Label(root, text="Enter the number of special characters to include:")
label_num_special_characters.pack()

entry_num_special_characters = tk.Entry(root)
entry_num_special_characters.pack()

button_generate = tk.Button(root, text="Generate Password", command=on_generate)
button_generate.pack()

# Run the application
root.mainloop()
