Data = []
print("Enter the Elements:")
Size = int(input())

print("Please enter numeric values:")
for i in range(Size):
    no = int(input())
    Data.append(no)

print("Input Data",Data)

Min_num = min(Data)
print("Minimum number from Data : ",Min_num)