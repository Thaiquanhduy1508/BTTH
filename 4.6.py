full_name = input("Nhập tên người (họ và tên): ")
name_parts = full_name.split()
if len(name_parts) >= 2:
    last_name = name_parts[0]  
    first_name = name_parts[1] 
    print("Họ:", last_name)
    print("Tên riêng:", first_name)
else:
    print("Vui lòng nhập đầy đủ họ và tên.")
