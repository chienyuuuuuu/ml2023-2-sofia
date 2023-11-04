from module5_mod import Numbers

numbers = Numbers()
n = int(input("Input N numbers: "))

for i in range(n):
    num = int(input("Input number: "))
    numbers.add_number(num)

x = int(input("Input integer x: "))
idx = numbers.find_index(x)
print(f"Output: {idx}")
