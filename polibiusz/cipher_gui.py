# cipher_gui.py

import tkinter as tk
from tkinter import messagebox
from cipher_controller import CipherController

class CipherGUI:
    def __init__(self, root):
        self.controller = CipherController()

        root.title("Polybius Encryption Machine")

        tk.Label(root, text="Text to encrypt:").pack()
        self.input_text = tk.Entry(root, width=50)
        self.input_text.pack()

        tk.Label(root, text="Key a (0-100):").pack()
        self.a_key = tk.Entry(root, width=10)
        self.a_key.pack()

        tk.Label(root, text="Key b (0-30):").pack()
        self.b_key = tk.Entry(root, width=10)
        self.b_key.pack()

        tk.Label(root, text="Select Table (0-9):").pack()
        self.table_selector = tk.Scale(root, from_=0, to=9, orient=tk.HORIZONTAL)
        self.table_selector.pack()

        self.encrypt_button = tk.Button(root, text="Encrypt", command=self.on_encrypt)
        self.encrypt_button.pack()

        tk.Label(root, text="Encryption result:").pack()
        self.output_text = tk.Entry(root, width=50)
        self.output_text.pack()

        self.decrypt_button = tk.Button(root, text="Decrypt", command=self.on_decrypt)
        self.decrypt_button.pack()

        tk.Label(root, text="Decryption result:").pack()
        self.decrypted_text = tk.Entry(root, width=50)
        self.decrypted_text.pack()

    def on_encrypt(self):
        try:
            text = self.input_text.get()
            a = int(self.a_key.get())
            b = int(self.b_key.get())
            table_index = self.table_selector.get()
            result = self.controller.encrypt_text(text, a, b, table_index)
            self.output_text.delete(0, tk.END)
            self.output_text.insert(0, str(result))
        except ValueError:
            messagebox.showerror("Error", "Please enter valid key values.")

    def on_decrypt(self):
        try:
            y = int(self.output_text.get())
            a = int(self.a_key.get())
            b = int(self.b_key.get())
            table_index = self.table_selector.get()
            result = self.controller.decrypt_text(y, a, b, table_index)
            if result is None:
                messagebox.showerror("Error", "Cannot decrypt, as key 'a' cannot be zero.")
            else:
                self.decrypted_text.delete(0, tk.END)
                self.decrypted_text.insert(0, result)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid key values.")
