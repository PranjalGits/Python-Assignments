filename = 'example.txt'  # Replace with your file name or path

line_count = 0
file_size = 0

with open(filename, 'r') as file:
    for line in file:
        line_count += 1
        file_size += len(line.encode())  # Increment file size by the length of each line

print(f"Number of lines in '{filename}': {line_count}")
print(f"File size of '{filename}': {file_size} bytes")
