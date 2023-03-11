#every variale in python is stored as string so to avoid it type conversion is
#done
old_age=input("Enter Old Age: ")
new_age=int(old_age)+2
name=input("What is your name?")
surname=input("What is your surname?")
fullName=str(name)+" "+str(surname)
print(str(fullName))
print(int(new_age))
print(float(new_age))
print(complex(new_age))
print(bool(new_age))
