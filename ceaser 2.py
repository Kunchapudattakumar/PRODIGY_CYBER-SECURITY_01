import tkinter as tk
from tkinter import messagebox

def caesar_cipher_encrypt(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():  
           
            shifted = ord(char) + shift
         
            if char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
           
            elif char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char  
    return encrypted_text

def caesar_cipher_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():  
           
            shifted = ord(char) - shift
            
            if char.isupper():
                if shifted < ord('A'):
                    shifted += 26
                elif shifted > ord('Z'):
                    shifted -= 26
           
            elif char.islower():
                if shifted < ord('a'):
                    shifted += 26
                elif shifted > ord('z'):
                    shifted -= 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char 
    return decrypted_text

def encrypt_message():
    plaintext = plaintext_entry.get()
    shift = int(shift_entry.get())
    encrypted_message = caesar_cipher_encrypt(plaintext, shift)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, encrypted_message)

def decrypt_message():
    ciphertext = ciphertext_entry.get()
    shift = int(shift_entry.get())
    decrypted_message = caesar_cipher_decrypt(ciphertext, shift)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, decrypted_message)


window = tk.Tk()
window.title("Caesar Cipher Encryption/Decryption")


plaintext_label = tk.Label(window, text="Message:")
plaintext_label.grid(row=0, column=0, padx=10, pady=5)

plaintext_entry = tk.Entry(window, width=50)
plaintext_entry.grid(row=0, column=1, columnspan=2, padx=10, pady=5)

ciphertext_label = tk.Label(window, text="Ciphertext:") 
ciphertext_label.grid(row=1, column=0, padx=10, pady=5)

ciphertext_entry = tk.Entry(window, width=50)
ciphertext_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=5)

shift_label = tk.Label(window, text="Shift Value:")
shift_label.grid(row=2, column=0, padx=10, pady=5)

shift_entry = tk.Entry(window, width=10)
shift_entry.grid(row=2, column=1, padx=10, pady=5)

encrypt_button = tk.Button(window, text="Encrypt", width=15, command=encrypt_message)
encrypt_button.grid(row=3, column=1, padx=10, pady=5)

decrypt_button = tk.Button(window, text="Decrypt", width=15, command=decrypt_message)
decrypt_button.grid(row=3, column=2, padx=10, pady=5)

result_label = tk.Label(window, text="Result:")
result_label.grid(row=4, column=0, padx=10, pady=5)

result_text = tk.Text(window, height=5, width=50)
result_text.grid(row=4, column=1, columnspan=2, padx=10, pady=5)


window.mainloop()
