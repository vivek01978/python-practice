# dist  = {
#     "name" : "vivek",
#     "class" : "B.tech",
#     "cgpa" : 66.67
# }
# print(type(dist))
# print(dist)


# nested dictionary
student = {
    "name" : "vivek",
    "subject" : {
        "maths" : 99,
        "physics" : 89,
        "chemistry" : 98,

    }
}
new_student = {
    "name": "deep", "age": 21
}


print(student)
print(student["subject"]["maths"])

# 1. myDict.key()
print(student.keys())
print(list(student.keys()))
print(len(student))
#example name & subject

# 2. myDict.keys()
print(student.values())
print(list(student.values()))
print(len(student))

# 3. myDict.items
print(student.items())
print(list(student.items()))

# 4. myDict.get("key")
print(student.get("name"))
print(student.get("name1")) # this is dict.get

# 5. myDict.update(newdict)
student.update({"city":"varanasi"})
print(student)
print(list(student))

# set in python

set = { 1,1,2,2,4,"vivek", "krishna"}
print(set)
print(type(set))
# empty set
null_set = {}
print(null_set)
print(type(null_set))

# 1. set.add(el)
Set = { 1,2,3,4,5,6,5}
Set.add("vivek")
Set.add((1,8,7,55))

Set.add(7)
print(Set)

# 2. set.remove
Set.remove(7)
print(Set)

# 3. set.clear()
Set.clear()
print(Set)

# 4. set.pop()
set_1 = { "vivek", "deep" , "sonali"}
print(set_1.pop())
print(set_1.pop())
print(set_1.pop())

# 5. set.union(set2)
set1= { 1,2,3,4}
set2 = { 2,3,4,5,6,7}
print(set1.union(set2))
print(set1)
print(set2)

# 6. set.intersection(set2)
set3 = { 1,2,3,4}
set4 = { 1,2,3,4,5,6,7,8}
print(set3.intersection(set4))



# dict = {
#     "name" : "vivek",
#     "class" : "b.tech",
#     "sub": {
#         "math" : 54,
#         "che" : 90,
#     }
# }

# print(dict.keys())
# print(dict.values())
# print(list(dict.items()))
# print(dict.get("sub"))
# print(dict.get("name"))
# print(dict.update({"city": "varanasi"}))
# print(dict)

# set = {1,2,3,5,6}
# set1 = {1,4,3,5,6,7,8,9,9}
# null_set = {}
# print(set)
# set.add(9)
# set.remove(1)
# set.pop()
# set.union()
# print(set)
# print(set.union(set1))
# print(set.intersection(set1))































