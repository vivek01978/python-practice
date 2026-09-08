#concatenation
stri = "hello"
stri1 = "world"
final_str = stri + " " + stri1
print(final_str)
print(len(final_str))

#length strings
stri2 = "vivek"
len1 = len(stri2)
print(len1)


#indexing
#accessing parts of string
str3 = "engineering"
print(str3[1])

#slicing
str4 = "vivek kumar gupta"
print(str4[0:17 ])
print(str4[6:12])
print(str4[ :5])
print(str4[6:])

print(str4[5:1]) #false

#slicing negative index
str5  = "apple"
print(str5[-5:-1])
print(str5[-1: -5]) #false

 #strings functions 
 # 1. str.endswith("jo end me likha ho usko likhna h ")  give me true and false

str6 = " i am studying in invertis university"
print(str6.endswith("sity"))
print(str6.endswith("tis" ))

# 2. str.capitalize()
str7 = "hello i am vivek"
print(str.capitalize("h"))

# example 
str7 = str7.capitalize()
print(str7)
print(str7)

# 3. str.replace(old,new)
# but change only single string
str8 = "i am vivek form bareilly"
print(str8.replace("bareilly" ," banaras"))
print(str8.replace("i ", ""))
print(str8.replace("i" , "his" ))

# 4. str.find(word)
str9 = "i am vivek , software engineering"
print(str9.find("s"))
#example
print(str9.find("z"))

#5.  str.count()
#str9
print(str9.count("e"))

# conditional statements / if else
age = 19
if(age>=18):
    print("you can  vote  and apply for license")
elif(age<=18):
    print("you can  not eligiable for vote") 
else:
    print("not found")

#ham isme multiple time if if use kre skte h 

#question 
age1 = 19 #change for age = 13 and print else condition
if(age>=18):
    print("they can vote")
else:
    print("you not eligiable for vote")

#improtant line---> jo hmm if ke bad likhte h to hmm 4 space dete h use khte h 
#indentation

#nesting condition--> if else
age_1 = 89

if(age_1>=18):
    if(age_1>=70):
        print("you can not drive")
    else:
        print("they ccan vote")
else:
    print("not eligiable")







