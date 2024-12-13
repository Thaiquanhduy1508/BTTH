def read_last_n_lines(file_path, n):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines[-n:]:
            print(line.rstrip())
read_last_n_lines('file.txt', 3)
print('THÁI QUANG DUY')
