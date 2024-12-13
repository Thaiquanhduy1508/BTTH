def count_lines_in_file(file_path):
    with open(file_path, 'r') as file:
        num_lines = sum(1 for line in file)
    print(f"Số dòng trong tệp: {num_lines}")
count_lines_in_file('file.txt')
print('THÁI QUANG DUY')
