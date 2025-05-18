Data = []
print("Enter the Elements:")
Size = int(input())

print("Please enter numeric values:")
for i in range(Size):
    no = int(input())
    Data.append(no)

print("Input Data",Data)

print("Element to search:")
search_num = int(input())

count = 0

for num in Data:
    if num == search_num:
        count = count + 1

print("Frequency of number is :",count)