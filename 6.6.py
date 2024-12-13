class StringHandler:
    def get_String(self):
        self.user_string = input("Nhập chuỗi: ")

    def print_String(self):
        print(self.user_string.upper())
handler = StringHandler()
handler.get_String()
handler.print_String()
print('THÁI QUANG DUY ')
