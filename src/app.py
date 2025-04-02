import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk
from billgenerate import create_pdf

def confirm():
    # create_pdf(entry_int.get())
    output_string.set(f'{entry_int.get()}')
    # label.configure(text='sdsdasd')

# window
window = ttk.Window(themename='darkly')
window.title('Demo')
window.geometry('500x300')

# title
title_label = ttk.Label(master=window, text='Bill Generate', font='Calibri 24 bold').pack()

# input field
input_frame = ttk.Frame(master=window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_int).pack(side='left', padx=10)
button = ttk.Button(master=input_frame, text = 'confirm', command=confirm).pack(side='left')
input_frame.pack(pady=10)

# output
# label = ttk.Label(master=window, text='Text from Input').pack()
output_string = tk.StringVar()
output_label = ttk.Label(
    master=window, 
    text='Success', 
    font='Calibri 24 bold', 
    textvariable=output_string).pack(pady=5)

# run
window.mainloop()



