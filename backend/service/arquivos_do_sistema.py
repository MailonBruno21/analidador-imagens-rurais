import tkinter as tk
from tkinter import filedialog

def save_file():
   f = filedialog.asksaveasfile(initialfile = 'modelo.h5',
    defaultextension=".h5",filetypes=[("All Files","*.h5*")])
