from text_analyzer import *

def main(input_file, output_dir, ignored_words_file, min_length=1, max_length=20, consecutive_words=1, sort_order=None):
    text = read_file(input_file)
    if text is None:
        return

    ignored_words = read_ignored_words(ignored_words_file)
    
    num_lines = count_lines(text)
    num_sentences = count_sentences(text)
    num_words, words = count_words(text)
    filtered_words = filter_words(words, min_length, max_length, ignored_words)
    word_combinations = generate_word_combinations(filtered_words, consecutive_words, sort_order)

    save_results(output_dir, num_lines, num_sentences, num_words, word_combinations)
    combine_results(output_dir)


if __name__ == "__main__":
    input_file = input('Enter input directory: ')
    output_dir = input('Enter output directory: ')
    ignored_words_file = input('Enter ignored words file path: ')

    min_length = int(input('Enter minimum word length: '))
    max_length = int(input('Enter maximum word length: '))
    consecutive_words = int(input('Enter number of consecutive words to count: '))
    sort_order = input("Enter sort order (asc/desc or leave blank for no sorting): ").strip().lower()

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    main(input_file, output_dir, ignored_words_file, min_length, max_length, consecutive_words, sort_order)