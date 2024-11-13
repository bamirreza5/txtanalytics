import os

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
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

def read_ignored_words(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            print(file)
            return set(word.strip() for word in file.readlines())
    except FileNotFoundError:
        print(f"Ignored words file not found: {file_path}")
        return set()

def filter_words(words, min_length, max_length, ignored_words):
    return [word for word in words if min_length <= len(word) <= max_length and word.lower() not in ignored_words]

    # Using list comprehension for simplicity and efficiency
    # result = []
    # for word in words:
    #     if min_length <= len(word) <= max_length:
    #         result.append(word)
    # return result
    
def generate_word_combinations(filtered_words, consecutive_count):
    combinations = {}
    for i in range(len(filtered_words) - consecutive_count + 1):
        combo = ' '.join(filtered_words[i:i + consecutive_count])
        combinations[combo] = combinations.get(combo, 0) + 1
    return combinations

def save_to_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def save_results(output_dir, num_lines, num_sentences, num_words, word_combinations):
    save_to_file(os.path.join(output_dir, 'lines_output.txt'), f"Number of lines: {num_lines}\n")
    save_to_file(os.path.join(output_dir, 'sentences_output.txt'), f"Number of sentences: {num_sentences}\n")
    save_to_file(os.path.join(output_dir, 'words_output.txt'), f"Number of words: {num_words}\n")
    
    combinations_content = "Word combinations:\n"
    for combo, count in word_combinations.items():
        combinations_content += f"{combo}: {count}\n"
    save_to_file(os.path.join(output_dir, 'combinations_output.txt'), combinations_content)

def combine_results(output_dir):
    final_content = ""
    for file_name in ['lines_output.txt', 'sentences_output.txt', 'words_output.txt', 'combinations_output.txt']:
        with open(os.path.join(output_dir, file_name), 'r', encoding='utf-8') as file:
            final_content += file.read()
    save_to_file(os.path.join(output_dir, 'output.txt'), final_content)

def main(input_file, output_dir, ignored_words_file, min_length=4, max_length=4, consecutive_words=3):
    text = read_file(input_file)
    if text is None:
        return

    ignored_words = read_ignored_words(ignored_words_file)
    
    num_lines = count_lines(text)
    num_sentences = count_sentences(text)
    num_words, words = count_words(text)
    filtered_words = filter_words(words, min_length, max_length, ignored_words)
    word_combinations = generate_word_combinations(filtered_words, consecutive_words)

    save_results(output_dir, num_lines, num_sentences, num_words, word_combinations)
    combine_results(output_dir)


if __name__ == "__main__":
    input_file = input('Enter input directory: ')
    output_dir = input('Enter output directory: ')
    ignored_words_file = input('Enter ignored words file path: ')

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    main(input_file, output_dir, ignored_words_file)
