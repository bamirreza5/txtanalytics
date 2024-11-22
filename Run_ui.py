import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox
import os
import json

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        messagebox.showerror("Error", f"File not found: {file_path}")
        return None

def count_lines(text):
    return len(text.splitlines())

def count_sentences(text):
    sentences = []
    start = 0
    for i, char in enumerate(text):
        if char in ".!?":
            sentences.append(text[start:i+1].strip())
            start = i + 1
    return len(sentences)

def count_words(text):
    words = [word.strip(".,!?;:") for word in text.split()]
    return len(words), words

def read_ignored_words(content):
    return set(word.strip() for word in content.splitlines())

def filter_words(words, min_length, max_length, ignored_words):
    return [word for word in words if min_length <= len(word) <= max_length and word.lower() not in ignored_words]

def generate_word_combinations(filtered_words, consecutive_count, sort_order=None):
    combinations = {}
    for i in range(len(filtered_words) - consecutive_count + 1):
        combo = ' '.join(filtered_words[i:i + consecutive_count])
        combinations[combo] = combinations.get(combo, 0) + 1
    if sort_order == 'asc':
        return dict(sorted(combinations.items(), key=lambda item: item[1]))
    elif sort_order == 'desc':
        return dict(sorted(combinations.items(), key=lambda item: item[1], reverse=True))
    return combinations

def save_results_to_json(output_file, results):
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(results, file, indent=4)

def analyze_text():
    text = input_text.get('1.0', tk.END).strip()
    ignored_content = ignored_text.get('1.0', tk.END).strip()
    if not text:
        messagebox.showwarning("Warning", "Input text is empty!")
        return
    if not ignored_content:
        ignored_words = set()
    else:
        ignored_words = read_ignored_words(ignored_content)
    
    try:
        min_length = int(min_length_entry.get())
        max_length = int(max_length_entry.get())
        consecutive_words = int(consecutive_entry.get())
        sort_order = sort_order_combo.get()
    except ValueError:
        messagebox.showerror("Error", "Invalid numerical input!")
        return

    num_lines = count_lines(text)
    num_sentences = count_sentences(text)
    num_words, words = count_words(text)
    filtered_words = filter_words(words, min_length, max_length, ignored_words)
    word_combinations = generate_word_combinations(filtered_words, consecutive_words, sort_order)
    output_text.config(state='normal')
    output_text.delete('1.0', tk.END)
    output_text.insert('1.0', f"Number of lines: {num_lines}\n")
    output_text.insert('end', f"Number of sentences: {num_sentences}\n")
    output_text.insert('end', f"Number of words: {num_words}\n\n")
    output_text.insert('end', "Word Combinations:\n")
    for combo, count in word_combinations.items():
        output_text.insert('end', f"{combo}: {count}\n")
    output_text.config(state='disabled')

    # ذخیره‌سازی نتایج به فایل JSON
    output_file = output_file_entry.get()
    save_results_to_json(output_file, {
        "Number of lines": num_lines,
        "Number of sentences": num_sentences,
        "Number of words": num_words,
        "Word combinations": word_combinations
    })
    messagebox.showinfo("Success", f"Results saved to {output_file}")

root = tk.Tk()
root.title('Text Analysis')
root.geometry('850x600')

input_text = tk.Text(root, height=10, width=40)
input_text.grid(column=0, row=0, padx=10, pady=10, sticky='nsew')

ignored_text = tk.Text(root, height=10, width=40)
ignored_text.grid(column=1, row=0, padx=10, pady=10, sticky='nsew')

output_text = tk.Text(root, height=15, width=80, state='disabled')
output_text.grid(column=0, row=2, columnspan=2, padx=10, pady=10)
def open_input_file():
    filetypes = (('Text files', '*.txt'), ('All files', '*.*'))
    file = fd.askopenfile(filetypes=filetypes)
    if file:
        input_text.delete('1.0', tk.END)
        input_text.insert('1.0', file.read())
        file.close()
def open_ignored_file():
    filetypes = (('Text files', '*.txt'), ('All files', '*.*'))
    file = fd.askopenfile(filetypes=filetypes)
    if file:
        ignored_text.delete('1.0', tk.END)
        ignored_text.insert('1.0', file.read())
        file.close()

def save_output_file():
    file = fd.asksaveasfile(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    if file:
        output_file_entry.delete(0, tk.END)
        output_file_entry.insert(0, file.name)

input_button = ttk.Button(root, text='Open Input File', command=open_input_file)
input_button.grid(column=0, row=1, padx=10, pady=5, sticky='w')

ignored_button = ttk.Button(root, text='Open Ignored File', command=open_ignored_file)
ignored_button.grid(column=1, row=1, padx=10, pady=5, sticky='w')

save_output_button = ttk.Button(root, text="Select Output File", command=save_output_file)
save_output_button.grid(column=0, row=6, columnspan=2, padx=10, pady=10)

min_length_label = tk.Label(root, text="Min Word Length:")
min_length_label.grid(column=0, row=3, sticky='w', padx=10)
min_length_entry = ttk.Entry(root, width=10)
min_length_entry.grid(column=0, row=3, sticky='e', padx=10)

max_length_label = tk.Label(root, text="Max Word Length:")
max_length_label.grid(column=1, row=3, sticky='w', padx=10)
max_length_entry = ttk.Entry(root, width=10)
max_length_entry.grid(column=1, row=3, sticky='e', padx=10)

consecutive_label = tk.Label(root, text="Consecutive Words:")
consecutive_label.grid(column=0, row=4, sticky='w', padx=10)
consecutive_entry = ttk.Entry(root, width=10)
consecutive_entry.grid(column=0, row=4, sticky='e', padx=10)
sort_order_label = tk.Label(root, text="Sort Order:")
sort_order_label.grid(column=1, row=4, sticky='w', padx=10)
sort_order_combo = ttk.Combobox(root, values=["asc", "desc", ""])
sort_order_combo.grid(column=1, row=4, sticky='e', padx=10)
output_file_label = tk.Label(root, text="Output File Path:")
output_file_label.grid(column=0, row=5, sticky='w', padx=10)
output_file_entry = ttk.Entry(root, width=40)
output_file_entry.grid(column=0, row=5, columnspan=2, padx=10, pady=10)
analyze_button = ttk.Button(root, text="Analyze Text", command=analyze_text)
analyze_button.grid(column=0, row=7, columnspan=2, pady=10)
root.mainloop()
