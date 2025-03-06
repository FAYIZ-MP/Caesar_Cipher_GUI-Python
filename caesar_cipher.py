import tkinter as tk
from tkinter import messagebox

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift if mode == 'encrypt' else -shift
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift_amount) % 26 + ascii_offset)
        else:
            result += char
    return result

def encrypt():
    text = input_text.get("1.0", tk.END).strip()
    shift = int(shift_value.get())
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, caesar_cipher(text, shift, 'encrypt'))

def decrypt():
    text = input_text.get("1.0", tk.END).strip()
    shift = int(shift_value.get())
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, caesar_cipher(text, shift, 'decrypt'))

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(output_text.get("1.0", tk.END).strip())
    root.update()
    messagebox.showinfo("Copied!", "Text copied to clipboard successfully.")

# GUI Setup
root = tk.Tk()
root.title("Caesar Cipher GUI")
root.geometry("500x400")
root.configure(bg="#282c34")

# Header
header = tk.Label(root, text="Caesar Cipher", font=("Arial", 18, "bold"), fg="white", bg="#282c34")
header.pack(pady=10)

# Input Text Box
input_label = tk.Label(root, text="Enter Text:", font=("Arial", 12), fg="white", bg="#282c34")
input_label.pack()
input_text = tk.Text(root, height=3, width=50, font=("Arial", 12))
input_text.pack(pady=5)

# Shift Value
shift_label = tk.Label(root, text="Shift Value:", font=("Arial", 12), fg="white", bg="#282c34")
shift_label.pack()
shift_value = tk.Entry(root, font=("Arial", 12), width=5)
shift_value.pack()

# Buttons
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt, bg="green", fg="white", font=("Arial", 12))
encrypt_button.pack(pady=5)

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt, bg="orange", fg="white", font=("Arial", 12))
decrypt_button.pack(pady=5)

# Output Box
output_label = tk.Label(root, text="Output:", font=("Arial", 12), fg="white", bg="#282c34")
output_label.pack()
output_text = tk.Text(root, height=3, width=50, font=("Arial", 12))
output_text.pack(pady=5)

# Copy Button
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg="blue", fg="white", font=("Arial", 12))
copy_button.pack(pady=10)

# Run GUI
root.mainloop()
