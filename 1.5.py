name = "THÁI QUANG DUY"         
age = 18
height = 16.2             
is_student = 'SVDHV'
print(f"Tên: {name}, Tuổi: {age}, Chiều cao: {height}, Sinh viên: {is_student}")
age = int(input("Nhập tuổi của bạn: "))

if age < 18:
    print("Bạn là thiếu niên.")
elif 18 <= age < 60:
    print("Bạn là người trưởng thành.")
else:
    print("Bạn là người cao tuổi.")
print("Các số từ 1 đến 5:")
for i in range(1, 6):
    print(i)

count = 0
print("Vòng lặp while:")
while count < 5:
    print(count)
    count += 1
def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Lỗi: Không thể chia cho 0."
    except TypeError:
        return "Lỗi: Nhập vào phải là số."
    finally:
        print("Kết thúc hàm divide.")

num1 = float(input("Nhập số thứ nhất: "))
num2 = float(input("Nhập số thứ hai: "))

result = divide(num1, num2)
print(f"Kết quả: {result}")
print("THÁI QUANG DUY")
