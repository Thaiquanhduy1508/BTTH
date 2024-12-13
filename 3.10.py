import math

def Tinh(R):
    if R < 0:
        return "Bán kính không hợp lệ. Vui lòng nhập bán kính lớn hơn hoặc bằng 0."
    chu_vi = 2 * math.pi * R
    dien_tich = math.pi * R ** 2
    
    return chu_vi, dien_tich
try:
    R = float(input("Nhập bán kính R: "))
    chu_vi, dien_tich = Tinh(R)
    print(f"Chu vi của hình tròn: {chu_vi:.2f}")
    print(f"Diện tích của hình tròn: {dien_tich:.2f}")
except ValueError:
    print("Vui lòng nhập một số hợp lệ.")
print("HÁI QUANG DUY")
