import tkinter as tk

def show_text():
    text = entry.get()
    label.config(text=text)

root = tk.Tk()
root.title("Text Analysis Application") 
root.geometry("500x500")

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Show", command=show_text)
button.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()