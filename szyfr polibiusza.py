import tkinter as tk
from tkinter import messagebox
import math

# List of 10 different Polybius tables, each with letters in a unique arrangement
polybius_tables = [
    [
        ['B', 'Q', 'Y', 'a', 'Ć', 'E', 'Z', 'Ó', 'V'],
         ['ą', ' ', 'J', 'I', 'Ł', 'G', 'P', 'M', 'Ś'],
         ['Ź', 'X', 'd', 'T', 'F', 'H', 'Ż', 'f', 'A'],
         ['D', 'N', 'O', 'W', 'K', 'S', 'ę', 'Ć', 'R'],
         ['L', 'U', 'C', 'Ń', 'e', 'Ę', 'o', 'V', 'b']

    ],
    [['d', 'Ą', 'ę', 'E', 'P', 'S', 'B', 'V', 'F'],
     ['I', 'L', 'Q', 'J', 'M', 'T', 'Ń', 'Ź', 'b'],
     ['O', 'o', 'N', 'Ż', 'U', 'y', ' ', 'X', 'c'],
     ['R', 'f', 'Ł', 'Ź', 'ę', 'W', 'Ć', 'ą', 'H'],
     ['D', 'Ś', 'G', 'a', 'Ą', 'ż', 'Y', 'Z', 'O']],

    [['Ż', 'Q', 'Y', 'B', 'O', 'Ę', 'o', 'F', 'd'],
     ['Ć', 'G', 'V', 'K', 'ę', 'L', 'b', 'P', 'Ś'],
     ['Ź', 'c', 'J', 'T', 'R', 'Ń', 'O', 'a', 'N'],
     ['Z', 'f', 'C', 'U', 'W', 'S', 'D', ' ', 'L'],
     ['M', 'Ą', 'I', 'A', 'ć', 'X', 'ą', 'Y', 'Ę']],

    [['M', 'L', 'a', 'Y', 'F', 'ę', 'A', 'P', 'Ż'],
    ['G', 'N', 'K', 'Ź', 'ć', 'U', ' ', 'D', 'V'],
    ['Ę', 'o', 'Ś', 'J', 'T', 'L', 'y', 'Ż', 'B'],
    ['I', 'H', 'b', 'C', 'D', 'ą', 'f', 'S', 'X'],
    ['Q', 'Z', 'O', 'R', 'O', 'Ń', 'Ć', 'Ź', 'E']],

    [['T', 'V', 'C', 'ą', 'E', 'Ż', 'Ę', 'd', 'B'],
    ['Ź', 'F', 'J', 'G', 'a', 'o', 'K', 'L', 'I'],
    [' ', 'Ł', 'Q', 'Ć', 'Y', 'X', 'R', 'Ś', 'D'],
    ['N', 'P', 'f', 'U', 'Ż', 'b', 'Ń', 'S', 'O'],
    ['Ą', 'Ą', 'H', 'A', 'Ź', 'W', 'ć', 'Z', 'e']],

    [['L', 'Ź', 'E', 'Y', 'D', 'T', 'Ą', 'ę', 'X'],
    ['F', 'Ż', 'C', 'V', 'B', 'a', 'P', 'Ś', 'H'],
    ['A', 'o', 'G', 'Ł', ' ', 'Ź', 'Z', 'S', 'Ć'],
    ['Ę', 'N', 'Q', 'R', 'N', 'J', 'M', 'O', 'ą'],
    ['I', 'U', 'b', 'O', 'Ń', 'f', 'K', 'ć', 'd']],

    [['Ź', 'E', 'Z', 'B', 'Y', 'P', 'ą', 'A', 'F'],
    ['V', 'o', 'L', 'G', 'ć', 'S', 'ę', 'T', 'I'],
    ['Ź', ' ', 'a', 'Q', 'Ć', 'Ż', 'M', 'D', 'J'],
    ['K', 'X', 'R', 'd', 'f', 'U', 'b', 'H', 'W'],
    ['O', 'Ń', 'L', 'Ż', 'Ę', 'Ą', 'N', 'c', 'Ś']],

    [['Ż', 'T', 'Ź', 'N', 'C', 'J', 'R', 'd', 'Ą'],
    ['ą', 'Z', 'E', 'V', ' ', 'G', 'o', 'Q', 'P'],
    ['Ś', 'Ć', 'a', 'H', 'U', 'M', 'D', 'Ę', 'f'],
    ['W', 'b', 'I', 'Y', 'A', 'Ź', 'Ł', 'O', 'L'],
    ['Ź', 'ę', 'K', 'S', 'X', 'ć', 'Ó', 'O', 'F']],

    [['P', 'M', 'Ż', 'Ź', 'D', 'ę', 'ą', 'N', 'H'],
     ['o', 'A', 'Ę', 'F', 'V', 'Ź', 'b', 'Y', 'Q'],
    ['C', 'Ź', 'S', 'G', 'Ć', 'R', 'I', 'U', 'X'],
    ['L', 'B', 'd', 'Q', 'f', 'Z', 'T', ' ', 'O'],
    ['Ń', 'ą', 'W', 'E', 'Ć', 'K', 'Y', 'J', 'L']],

    [['Y', 'L', 'a', 'Ę', 'Ć', 'D', 'Ź', 'O', 'G'],
    [  'o', 'T', 'A', 'F', 'P', 'B', 'V', 'Ą', 'Z'],
    ['Q', 'S', 'L', 'Ź', 'K', 'ę', 'f', 'X', 'W'],
    ['I', 'J', 'N', 'b', 'Ó', ' ', 'R', 'Ź', 'M'],
    ['d', 'U', 'Ś', 'G', 'C', 'ą', 'H', 'Ć', 'O']],
]


# Encrypt function
def encrypt(text, a, b, table_index):
    # Remove spaces and convert to uppercase
    text = ''.join(text.split()).upper()
    table = polybius_tables[table_index]

    pairs = []
    for char in text:
        for i, row in enumerate(table):
            if char in row:
                j = row.index(char)
                pairs.append((i + 1, j + 1))
                break

    x = int(''.join(f"{i}{j}" for i, j in pairs))
    y = a * (x ** 2) + b
    return y


# Decrypt function
def decrypt(y, a, b, table_index):
    if a == 0:
        return None

    x = math.isqrt((y - b) // a)
    pairs = [(int(str(x)[i]), int(str(x)[i + 1])) for i in range(0, len(str(x)), 2)]

    decrypted_text = ''
    table = polybius_tables[table_index]
    for i, j in pairs:
        if 1 <= i <= 5 and 1 <= j <= 9:
            decrypted_text += table[i - 1][j - 1]

    return decrypted_text


# Encrypt button handler
def on_encrypt():
    try:
        text = input_text.get()
        a = int(a_key.get())
        b = int(b_key.get())
        table_index = table_selector.get()
        result = encrypt(text, a, b, table_index)
        output_text.delete(0, tk.END)
        output_text.insert(0, str(result))
    except ValueError:
        messagebox.showerror("Error", "Proszę wpisać wartość klucza")


# Decrypt button handler
def on_decrypt():
    try:
        y = int(output_text.get())
        a = int(a_key.get())
        b = int(b_key.get())
        table_index = table_selector.get()
        result = decrypt(y, a, b, table_index)
        if result is None:
            messagebox.showerror("Error", "Klucz a musi mieć wartość")
        else:
            decrypted_text.delete(0, tk.END)
            decrypted_text.insert(0, result)
    except ValueError:
        messagebox.showerror("Error", "Prosze użyć odpowiedniego klucza.")


# Create interface
root = tk.Tk()
root.title("Polybius Encryption Machine")

tk.Label(root, text="Tekst do zaszyfrowania").pack()
input_text = tk.Entry(root, width=50)
input_text.pack()

tk.Label(root, text="Klucz a (1-100):").pack()
a_key = tk.Entry(root, width=10)
a_key.pack()

tk.Label(root, text="Klucz b (1-30):").pack()
b_key = tk.Entry(root, width=10)
b_key.pack()

tk.Label(root, text="Wybierz Tabelę (1-10):").pack()
table_selector = tk.Scale(root, from_=1, to=10, orient=tk.HORIZONTAL)
table_selector.pack()

encrypt_button = tk.Button(root, text="Szyfruj", command=on_encrypt)
encrypt_button.pack()

tk.Label(root, text="Wynik szyfrowania").pack()
output_text = tk.Entry(root, width=50)
output_text.pack()

decrypt_button = tk.Button(root, text="Deszyfruj", command=on_decrypt)
decrypt_button.pack()

tk.Label(root, text="Wynik deszyfrowania").pack()
decrypted_text = tk.Entry(root, width=50)
decrypted_text.pack()

root.mainloop()
