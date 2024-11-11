def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            # print(content)
        return content
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
text = read_file('./index.txt')

lines = text.splitlines()
num_lines = len(lines)
print("number of lines : ", num_lines)

"""پیاده سازی برای شمارش جملات"""
sentences = []
start = 0
for i, char in enumerate(text):
    if char in ".!?":
        sentences.append(text[start:i+1].strip())
        start = i + 1
num_sentences = len(sentences)
print("Number of sentences:", num_sentences)
