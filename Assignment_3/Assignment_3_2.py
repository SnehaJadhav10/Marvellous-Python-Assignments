Data = []
print("Enter the Elements:")
Size = int(input())

print("Please enter numeric values:")
for i in range(Size):
    no = int(input())
    Data.append(no)

print("Input Data",Data)

Max_num = max(Data)
print("Maximum number from Data : ",Max_num)