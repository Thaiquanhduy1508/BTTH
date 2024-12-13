def read_entire_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)
read_entire_file('file.txt')  
print('THÁI QUANG DUY')
