import os
import json
import argparse
"""use this format : python text_ana_arg_json.py ./index.txt output.json ignored.txt --min_length 3 --max_length 10 --consecutive_words 2 --sort_order asc"""
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
            return set(word.strip() for word in file.readlines())
    except FileNotFoundError:
        print(f"Ignored words file not found: {file_path}")
        return set()

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

def calculate_word_statistics(words):
    if not words:
        return 0, []
    max_length = max(len(word) for word in words)
    longest_words = [word for word in words if len(word) == max_length]
    average_length = sum(len(word) for word in words) / len(words)
    return average_length, longest_words

def save_results_to_json(output_file, results):
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(results, file, indent=4)

def main(args):
    while True:
        text = read_file(args.input_file)
        if text is None:
            break
        
        ignored_words = read_ignored_words(args.ignored_words_file)
        num_lines = count_lines(text)
        num_sentences = count_sentences(text)
        num_words, words = count_words(text)
        filtered_words = filter_words(words, args.min_length, args.max_length, ignored_words)
        word_combinations = generate_word_combinations(filtered_words, args.consecutive_words, args.sort_order)
        average_length, longest_words = calculate_word_statistics(words)

        results = {
            "Number of lines": num_lines,
            "Number of sentences": num_sentences,
            "Number of words": num_words,
            "Longest words": longest_words,
            "Average word length": average_length,
            "Ignored words": list(ignored_words),
            "Word combinations": word_combinations
        }

        save_results_to_json(args.output_file, results)
        print(f"Results saved to {args.output_file}")
        
        user_input = input("Enter 'quit' to exit(ctrl+c) or press Enter to analyze again: ")
        if user_input.lower() == "quit":
            break

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze a text file.")
    parser.add_argument("input_file", help="Path to the input text file.")
    parser.add_argument("output_file", help="Path to the output JSON file.")
    parser.add_argument("ignored_words_file", help="Path to the ignored words file.")
    parser.add_argument("--min_length", type=int, default=1, help="Minimum word length to consider.")
    parser.add_argument("--max_length", type=int, default=20, help="Maximum word length to consider.")
    parser.add_argument("--consecutive_words", type=int, default=1, help="Number of consecutive words to count.")
    parser.add_argument("--sort_order", choices=["asc", "desc"], help="Sort order for word combinations.")
    args = parser.parse_args()

    try:
        if not os.path.exists(args.input_file):
            print(f"Error: Input file '{args.input_file}' does not exist.")
        elif not os.path.exists(args.ignored_words_file):
            print(f"Error: Ignored words file '{args.ignored_words_file}' does not exist.")
        else:
            main(args)
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting gracefully.")
        exit(0)
