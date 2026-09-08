# #LISTS 
# # marks =[76,89,87,90,83,"vivek"]
# # print(len(marks))
# # print(marks[5])
# # print(type(marks))

# # student = ["vivek", 87, 90,"delhi"]
# # print(student[0])
# # student[0] = "arjun"
# # print(student)

# #same cheez hmm string me follow nhi kr skte h
# #ex. 
# # str ="arjun"
# # print(str)
# # str[0] = "b"


# #list slicing

# marks1 = [32,65,78,89,90]
# print(marks1[0:2])
# print(marks1[ : 4])
# print(marks1[0:])

# #negative list slicing 

# print(marks1[-1: -4]) #error
# print(marks1[-4:-1])
# print(marks1[-1: ])
# print(marks1[  : -4])



# #list method 
# # 1. append method 
# list = [2,3,4]
# list.append(5)
# print(list)
# # ise hmm koi bhi value add kr skte h 

# #  2. list sorting   / ascending order
# list1 = [3,2,1,4]
# print (list1.sort())
# print(list1)

# #list1 = [3,2,1,4]
# # print (list1.sort())
# # print(list1.append(5))
# # print(list1)

# # 3. list sorting(reverse= True) / descending order
# list2 = [1,4,7,3,9,0,4,]
# """print likhne pe none print hoga """ 
# (list2.sort(reverse=True))
# print(list2)


# improtant
# list3 = ["banana", "litchi", "apple"]
# print(list3.sort())
# print(list3)
# (list3.sort(reverse=True))
# print(list3)

# 4.  list Reverse 

list4 = ["a,", "b",3 , 4,7,"z"]
list4.reverse()
print(list4)

# 5. list insert(idx,el)
list5 = [2,1,3]
list5.insert(1,5)
print(list5)

# 6. list Removes
list6 = [1,3,4]                         
list6.remove(3)
print(list6)

#7. LIST POP(idx)
list7 = [1,2,3]
list7.pop(2)
print(list7)

# TUPLES IN PYTHON 

list8 = (1,2,3,4)
print(list8[0])
# tup[0] = 5 isme koi value assign nhi hota h
tup = ()
print(tup)
print(type(tup))

tup1 = (1,) # hmm 1, ye likhe to tuple print hogo 
print(type(tup1))

tup2 = (2) # isme integer print hoga
print(tup2)
print(type(tup2))

# tup = (1,2,3,) or (1,2,3) both or same print 

tup3 = (1,2,3,4,5)
print(tup3[1:4])

#tuple method 
# 1. tup.index(el)
tup4 = (1,2,3,)
print(tup4.index(3))

# 2. tup.count(el)
tup5 = (1,2,3,4,2,2,2,2,22,)
print(tup5.count(2))
















