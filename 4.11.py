input_list = input("Nhập danh sách các phần tử (cách nhau bằng dấu phẩy hoặc khoảng trắng): ")
elements = input_list.replace(',', ' ').split()
new_element = input("Nhập phần tử mới để thêm vào danh sách: ")
elements.append(new_element)
print("Danh sách sau khi thêm phần tử mới:", elements)
print("HÁI QUANG DUY")