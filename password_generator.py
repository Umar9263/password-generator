#for GUI
import tkinter as tk
import random
import string

def generate_password():
    password_length = int(length_entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(password_length))
    password_label.config(text=password)
    generated_password = password

def copy_to_clipboard():
    password = password_label["text"]
    root.clipboard_clear()
    root.clipboard_append(password)

# Create the main application window
root = tk.Tk()
root.title("Password Generator")
root.attributes("-fullscreen", True)
root.bind("<Escape>", lambda event: root.attributes("-fullscreen", False))

# Create the entry field to specify password length
length_entry = tk.Entry(root, font=("Arial", 18))
length_entry.pack(pady=20)

# Create the button to generate the password
generate_button = tk.Button(root, text="Generate Password", font=("Arial", 16), command=generate_password)
generate_button.pack()

# Create the label to display the generated password
password_label = tk.Label(root, text="", font=("Arial", 16))
password_label.pack(pady=20)

# Create the button to copy the generated password to clipboard
copy_button = tk.Button(root, text="Copy to Clipboard", font=("Arial", 16), command=copy_to_clipboard)
copy_button.pack()

# Start the application
root.mainloop()
