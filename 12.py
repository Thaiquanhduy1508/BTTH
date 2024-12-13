import re

def validate_password(password):
    if not re.search(r'[A-Z]', password):
        return False, "Mật khẩu phải có ít nhất 1 ký tự in hoa [A-Z]"

    if not re.search(r'[a-z]', password):
        return False, "Mật khẩu phải có ít nhất 1 ký tự in thường [a-z]"

    if not re.search(r'[0-9]', password):
        return False, "Mật khẩu phải có ít nhất 1 ký tự số [0-9]"

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False, "Mật khẩu phải có ít nhất 1 ký tự đặc biệt [!@#$%^&*(),.?\":{}|<>]"

    if not (6 <= len(password) <= 20):
        return False, "Mật khẩu phải có độ dài từ 6 đến 20 ký tự"
    
    return True, "Mật khẩu hợp lệ"

password = input("Nhập mật khẩu Tài Khoản Ngân Hàng: ").strip()
def validate_password(password):
    
    if not re.search(r'[0-9]', password):
        return False, "Mật khẩu phải có ít nhất 1 ký tự số [0-9]"


    if not (6 <= len(password) <= 20):
        return False, "Mật khẩu phải có độ dài từ 6 đến 20 ký tự"
    
    return True, "Mật khẩu hợp lệ"
password = input("Nhập mật khẩu OTP Tài Khoản Ngân Hàng: ").strip()

is_valid, message = validate_password(password)

print(message)
print("THÁI QUANG DUY ")
