input_string = input("Nhập một chuỗi: ")
output_string = ''.join(char for char in input_string if not char.isdigit())
print("Chuỗi sau khi loại bỏ chữ số:", output_string)
print("HÁI QUANG DUY")
