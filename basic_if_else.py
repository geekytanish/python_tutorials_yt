age=input("What is your age?")
check=input("Do you have adhaar Card? Press 1 for yes and 0 for no")

if int(age)>=18 and bool(check)==1:
    print("Yes, you can vote")
else:
    print("nikal")
