input_string = input("Nhập một dãy các từ (cách nhau bằng dấu cách): ")
words = input_string.split()
max_length = max(len(word) for word in words)
longest_words = [word for word in words if len(word) == max_length]
print("Từ dài nhất:", longest_words)
print("HÁI QUANG DUY")
