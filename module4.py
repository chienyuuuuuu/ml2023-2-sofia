n = int(input("Input N numbers: "))

numbers = []

for i in range(n):
    num = int(input("Input number: "))
    numbers.append(num)

x = int(input("Input integer x: "))
if x in numbers:
    idx = numbers.index(x)
    print(f"Output: {idx + 1}")
else:
    print("-1")
