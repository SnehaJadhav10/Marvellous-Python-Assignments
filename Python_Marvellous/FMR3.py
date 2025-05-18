from functools import reduce
   
Data = [7,10,15,12,4,6,9,8,12,16]
print(" Input Data:",Data)

FData = list(filter(lambda No : (No % 2 == 0),Data))
print("Filter output:",FData)

MData = list(map(lambda No : No+1,FData))
print("Map Output:",MData)

RData = reduce(lambda A,B : A + B,MData)
print("Reduce Data:",RData)
