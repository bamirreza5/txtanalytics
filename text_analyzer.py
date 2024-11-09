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
print(num_lines)
