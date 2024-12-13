a, b = 1, 2
total = 0

print("Fibonacci numbers up to 4,000,000:")
while a < 4000000:
    print(a, end=', ') 
    if a % 2 == 0:      
        total += a      
    a, b = b, a + b  

print("\nSum of even Fibonacci numbers:", total)
print("THÁI QUANG DUY ")
