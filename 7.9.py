def copy_file_content(source_file, destination_file):
    with open(source_file, 'r', encoding='utf-8') as src:
        content = src.read()
    with open(destination_file, 'w', encoding='utf-8') as dest:
        dest.write(content)
    print("Nội dung đã được sao chép.")
copy_file_content('source.txt', 'destination.txt')  
print('THÁI QUANG DUY ')
