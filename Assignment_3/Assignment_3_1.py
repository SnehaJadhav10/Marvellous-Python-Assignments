Data = []
print("Enter the Elements:")
Size = int(input())

print("Please enter numeric values:")
for i in range(Size):
    no = int(input())
    Data.append(no)

print("Input Data",Data)

Add = 0
for i in Data:
    Add = Add + i

print("Sum =",Add)
