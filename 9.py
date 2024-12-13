str_input = input("Enter a String: ")

char_count = {}

for char in str_input:
    if char not in char_count:  
        char_count[char] = str_input.count(char)

print(char_count)
print("THÁI QUANG DUY")
