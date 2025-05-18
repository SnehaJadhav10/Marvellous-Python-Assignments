#dictionary

#syntax : {key : value}
# heterogeneous
# ordered
# indexed (not numeric)
# key duplicates are allowed but oid keys value gets overwritten(i.e in place of name)
# value duplicates allowed
# data mutable

# data = { "Name" : "Let us C", "Author":340 ,"Price":340 , "Publication":"BPB Publication" , "Name":"Let us C++"} (for understanding features)
data = { "Name" : "Let us C", "Author":"Y Kanetkar" ,"Price":340 , "Publication":"BPB Publication" }

print("Datatype is :",type(data))
print("Length is :",len(data))

print(data)

print(data["Author"]) #indexed

print["Price"] = 400
print(data)