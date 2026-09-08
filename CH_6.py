#function in python
def add(a,b): #parameters
    add = a+b
    print(add)
    return add
add(7272,9907)#function call, arguments

def name():
    print("vivek")
name()
# name()
# name()
# name()
# name()
# name()

#average of 3 number
def calu_aver(a,b,c):
    sum =a+b+c
    averg = sum/3
    return averg
print(calu_aver(1,2,3))


#Q wap to print the length of a list (list is the parameter) 
cities = ["delhi", "varanasi","noida","pune","chennai"]
heroes = ["ironman","thor", "captain"]

def name(list):
    print(len(list))
name(cities)
name(heroes)


#Recursion in python
def show(n): 
    if(n==0):
        return
    print(n)
    show(n-1)
show(5)






