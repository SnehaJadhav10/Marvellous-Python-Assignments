#Tuple

#Syntax :()
#Heterogeneous
#Ordered
#Index
#Data Immutable
#tuple Immutable
#Duplicate allowed


data = (10,"Hello",90.67,True,10)

print("Data type is :",type(data))
print("Length is :",len(data))
print(data)

print(data[0])
print(data[1])

#data[0] = 11      #for checking mutable(tuple is not mutable i.e immutable)

print("Data using loop")
for value in data:
    print(value)
    
for i in range(0,len(data)):
    print(data[i])
