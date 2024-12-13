input_list = input("Nhập danh sách các phần tử (cách nhau bằng dấu phẩy hoặc khoảng trắng): ")
elements = input_list.replace(',', ' ').split()
sliced_list = elements[1:-1]
print("Danh sách sau khi cắt (bỏ phần tử đầu và cuối):", sliced_list)
print("HÁI QUANG DUY")
