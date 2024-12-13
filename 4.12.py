input_list = input("Nhập danh sách các phần tử (cách nhau bằng dấu phẩy hoặc khoảng trắng): ")
elements = input_list.replace(',', ' ').split()
element_to_remove = input("Nhập phần tử cần bỏ khỏi danh sách: ")
if element_to_remove in elements:
    elements.remove(element_to_remove)
else:
    print("Phần tử không có trong danh sách.")

print("Danh sách sau khi bỏ phần tử:", elements)
print("HÁI QUANG DUY")
