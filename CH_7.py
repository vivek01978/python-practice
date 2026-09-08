#File I/O in python

#read
# r = open("read.txt","r")
# data = r.read()
# print(data)
# r.close

#write
# w = open("read.txt","w")
# w.write("hey what are doing")
# w.close()

#append
# a = open("read.txt","a")
# a.write("i am learning python")
# a.close()

# create a file
# f = open("write.txt", "w")
# f.close()

# R+ read and write
# rp = open("read.txt","r+")
# rp.write("abc")
# print(rp.read())
# rp.close()

#w+
# wp = open("read.txt","w+")
# print(wp.read())
# wp.write("hey everone")
# wp.close()

#a+
# ap=open("read.txt","a+")
# print(ap.read())
# ap.write("abc")
# ap.close()

# with syntax
# with open("read.txt","r") as f:
#     data = f.read()
#     print(data)

# with open("read.txt","w") as g:
#     g.write("hey vivek")

#deleting a file
# import os 
# os.remove("write.txt")


#question 
with open("practice.txt","r") as f:
    data = f.read()
new_data = data.replace("java","python")
print(new_data)
   


        






