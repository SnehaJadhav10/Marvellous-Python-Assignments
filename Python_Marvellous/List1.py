#List

#Syntax : []
#Heterogeneous
#Ordered
#Indexed
#Data Mutable
#list Mutable
#Duplicate Allowed


data = [10,90.67,"Hello",40,True]

print("Datatype is:",type(data))
print("Length is :",len(data))
print(data)

print(data[0])
print(data[1])
print(data[2])
print(data[3])

data[0] = 11
print(data[0])

data.append(40) #to check mutable
print(data[4])

print("Data Display using loop")
for value in data:
    print(value)