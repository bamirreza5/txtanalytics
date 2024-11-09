def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
        return content
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
read_file('./index.txt')

# ignore_file = input("Enter the path to the ignored words file: ")
# ignore_words_content = read_file(ignore_file)

# if ignore_words_content is not None:
#     ignore_words = ignore_words_content.split()
#     print("Ignore words loaded:", ignore_words)
# else:
#     print("Failed to load ignore words file.")
