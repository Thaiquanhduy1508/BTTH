def read_first_n_lines(file_path, n):
    with open(file_path, 'r') as file:
        for _ in range(n):
            print(file.readline().rstrip())

read_first_n_lines('file.txt', 5)
print('THÁI QUANG DUY ')
