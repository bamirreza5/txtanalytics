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

words = [word.strip(".,!?;:") for word in text.split()]
num_words = len(words)
print("Number of words:", num_words)

min_length = 4
max_length = 4
filtered_words = [word for word in words if min_length <= len(word) <= max_length]
print(filtered_words)

consecutive_words = 3
word_combinations = {}
for i in range(len(filtered_words) - consecutive_words + 1):
    combo = ' '.join(filtered_words[i:i + consecutive_words])
    if combo in word_combinations:
        word_combinations[combo] += 1
    else:
        word_combinations[combo] = 1
print("Word combinations:", word_combinations)

with open('./output.txt', 'w') as output_file:
    output_file.write(f"Number of lines: {num_lines}\n")
    output_file.write(f"Number of sentences: {num_sentences}\n")
    output_file.write(f"Number of words: {num_words}\n")
    output_file.write("Word combinations:\n")
    for combo, count in word_combinations.items():
        output_file.write(f"{combo}: {count}\n")
