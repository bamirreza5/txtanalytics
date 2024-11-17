import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd

root = tk.Tk()
root.title('Text Analysis')
root.resizable(True, True)
root.geometry('750x550')

input_text = tk.Text(root, height=10, width=40)
input_text.grid(column=0, row=0, padx=10, pady=10, sticky='nsew')

ignored_text = tk.Text(root, height=10, width=40)
ignored_text.grid(column=1, row=0, padx=10, pady=10, sticky='nsew')

def open_input_file():
    """Open and display the input file."""
    filetypes = (
        ('Text files', '*.txt'),
        ('All files', '*.*')
    )
    file = fd.askopenfile(filetypes=filetypes)
    if file:
        input_text.delete('1.0', tk.END)  
        input_text.insert('1.0', file.read())
        file.close()

def open_ignored_file():
    """Open and display the ignored words file."""
    filetypes = (
        ('Text files', '*.txt'),
        ('All files', '*.*')
    )
    file = fd.askopenfile(filetypes=filetypes)
    if file:
        ignored_text.delete('1.0', tk.END)  
        ignored_text.insert('1.0', file.read())
        file.close()

input_button = ttk.Button(
    root,
    text='Open Input File',
    command=open_input_file
)
input_button.grid(column=0, row=1, padx=10, pady=10, sticky='w')

ignored_button = ttk.Button(
    root,
    text='Open Ignored File',
    command=open_ignored_file
)
ignored_button.grid(column=1, row=1, padx=10, pady=10, sticky='w')

input_label = tk.Label(root, text="Input Words", font=("Arial", 12))
input_label.grid(column=0, row=2, padx=10, pady=5)

ignored_label = tk.Label(root, text="Ignored Words", font=("Arial", 12))
ignored_label.grid(column=1, row=2, padx=10, pady=5)

root.mainloop()
