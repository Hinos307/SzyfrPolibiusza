# main.py

import tkinter as tk
from cipher_gui import CipherGUI

if __name__ == "__main__":
    root = tk.Tk()
    app = CipherGUI(root)
    root.mainloop()
