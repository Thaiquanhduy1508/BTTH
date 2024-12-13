
from search import Sequential_Search  
def main():
    n = int(input("Nhập số lượng phần tử trong danh sách: "))
    dlist = []
    
    for i in range(n):
        value = int(input(f"Nhập giá trị phần tử thứ {i + 1}: "))
        dlist.append(value)

    item = int(input("Nhập phần tử cần tìm kiếm: "))

    found, index = Sequential_Search(dlist, item)
    if found:
        print(f"Phần tử {item} đã tìm thấy tại vị trí {index}.")
    else:
        print(f"Phần tử {item} không tìm thấy trong danh sách.")

if __name__ == "__main__":
    main()
print("THÁI QUANG DUY")
