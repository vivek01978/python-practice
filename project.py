Maths = int(input("enter maths number"))
Chemistry = int(input("enter Chemistry number"))
Physics = int(input("enter Physics number"))
English = int(input("enter English number"))
Computer = int(input("enter Computer number"))



sum = Maths+Chemistry+Physics+English+Computer
Percentage = (sum/500)*100
print("percentage =",Percentage,"%")

if Percentage >=90:
    print("Grade = A+")
elif Percentage >=80:
    print("Grade = A")
elif Percentage >=70:
    print("Grade =B")
elif Percentage >=60:
    print("Grade =D")
else:
    print("Grada = F")