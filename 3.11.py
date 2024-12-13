def benefit(n, k):
    try:
        lai_suat = float(input("Nhập lãi suất hàng tháng (%): ")) / 100
        tien_lai = n * lai_suat * k
        return tien_lai
    except ValueError:
        return "Vui lòng nhập một số hợp lệ."
try:
    n = float(input("Nhập số vốn ban đầu (n): "))
    k = int(input("Nhập số tháng (k): "))
    
    if n < 0 or k < 0:
        print("Số vốn và số tháng phải lớn hơn hoặc bằng 0.")
    else:
        tien_lai = benefit(n, k)
        print(f"Số tiền lãi nhận được sau {k} tháng: {tien_lai:.2f}")
except ValueError:
    print("Vui lòng nhập một số hợp lệ.")
print("HÁI QUANG DUY")
