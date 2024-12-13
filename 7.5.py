def append_text_to_file(file_path, text):
    with open(file_path, 'a', encoding='utf-8') as file:  
        file.write(text + '\n') 
    print("Nội dung đã thêm vào tệp.")
append_text_to_file('file.txt', 'Nội dung mới')  
print('THÁI QUANG DUY ')
