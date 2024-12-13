import search
n = int(input("Nhập số lượng phần tử trong danh sách: "))
dlist = []
for i in range(n):
    value = int(input(f"Nhập giá trị cho phần tử thứ {i+1}: "))
    dlist.append(value)
dlist.sort()
print("Danh sách sau khi sắp xếp:", dlist)
value = int(input("Nhập phần tử cần tìm: "))
found = search.binary_search(dlist, value)
if found:
    print(f"Phần tử '{value}' có trong danh sách.")
else:
    print(f"Phần tử '{value}' không có trong danh sách.")
print('THÁI QUANG DUY ')
