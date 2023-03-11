#strings methods

name=input("What is you name? ")
print(name.upper()) #this will convert whole string to uppercase
print(name.find('z')) #this will return the index of the found position or -1 if not found
print(name.capitalize())#this will capitalise first letter
print(name.isdecimal()) #checks whether the element is decimal or not
print(name.replace("stark","iron man")) #this will replace the whole string
print('T' in name) #checks for presence of specified substring in a string
