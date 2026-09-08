#LOOPS IN PYTHON
# i = 1
# while i <=100:
#     print(i)
#     i+=1
# j = 100
# while j>=1 :
#     print(j)
#     j-=1
#q3
# n= int(input("enter no."))
# k = 1
# while k<=10:
#     print(n*k)
#     k+=1

#Q4

# nums = [1,4,9,16,25,36,49,64,81,100]
# index = 0
# while index<len(nums):
#     print(nums[index])
#     index+=1

#Q 5.
# num = (1,4,9,16,25,36,49,64,81,100)
# i =0
# x =36
# while i<len(num):
#     if (num[i]==x):
#         print("FOUND AT INDEX",i)
#     else:
#         print("finding...")
     
    
#     i+=1

# Break and continue
# v=1
# while v<=10:
#     print(v)
#     if (v==7):
#         break
#     v+=1

#continue
# z = 0
# while z <=10:
#     if (z==3):
#         z+=1
#         continue
#     print(z)
#     z+=1
# #odd no.
# x= 0
# while x <=10:
#     if (x%2==0):#even no. !=0
#         x+=1
#         continue
#     print(x)
#     x+=1

# for loos use for /list tup string
# list =(1,3,4,6,7,9)
# for num in list:
#     print(num)

# else:
#     print("end")

#for loop with else

# str = "apnacollage"

# for char in str:
#     if (char =='o'):
#         print("o found")
#         break
#     print(char)
    
# print("end")


#Q 1. using for loop -->list
# list =[1,2,3,55,4,6,7,0,9]
# for el in list:
#     print(el)

#Q 2.
# nums = (1,2,3,4,5,6,7,8,9,99)
# x= 99
# idx=0
# for el in nums:
#     if(el==x):
#         print("numbers found at idx ",idx)
#         break
#     idx+=1

#rang()
seq = range(6)
for i in seq:
    print(i)

# for i in range(10):
#     print(i)

#range(start , stop)
for s in range(2,8):
    print(s) 

#rang (start , stop, step)
for g in range(1,8,2):
    print(g)







