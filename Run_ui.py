import tkinter as tk

def show_main_window():
    splash.destroy()

    root = tk.Tk()
    root.title("Text Analysis Application") 
    root.geometry("1000x1000")
    
    def show_text():
        text = entry.get()
        label.config(text=text)
    
    entry = tk.Entry(root)
    entry.pack()

    button = tk.Button(root, text="Show", command=show_text)
    button.pack()

    label = tk.Label(root, text="")
    label.pack()

    root.mainloop()

splash = tk.Tk()
splash.title("Text Analysis Application")
splash.geometry("1000x1000")
splash.configure(bg="lightgreen")

splash_label = tk.Label(splash, text="Welcome to the Text Analysis Application!", font=("Arial", 16), bg="lightgreen")
splash_label.pack(expand=True)
splash_label = tk.Label(splash, text="develope for jsharif course", font=("Arial", 16), bg="lightgreen")
splash_label.pack(expand=True)

splash.after(5000, show_main_window)

splash.mainloop()
