class ReverseWords:
    def __init__(self, text):
        self.text = text

    def reverse(self):
        return ' '.join(self.text.split()[::-1])
reverser = ReverseWords('hello .py')
print("Chuỗi đảo ngược:", reverser.reverse())
print('THÁI QUANG DUY')
