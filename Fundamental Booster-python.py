print("Welcome to the Interactive Personal Data Collector!",end="\n\n")

Name=input("Enter your name:-")
Age=int(input("Enter your age:-"))
height=float(input("Enter your height in meters:-"))
number=int(input("Enter your Favourite number:-"))

print("*****************************************************************************************")
print("Thank You! Here is the Information we collected:",end="\n\n")

print(f"Name: {Name} (Type: {type(Name)} ,Memory Address: {id(Name)})")
print(f"Name: {Age} (Type: {type(Age)} ,Memory Address: {id(Age)})")
print(f"Name: {height} (Type: {type(height)} ,Memory Address: {id(height)})")
print(f"Name: {number} (Type: {type(number)} ,Memory Address: {id(number)})",end="\n\n")

Year=2025
appage=Year-Age   # appage=appage-1
print("Your birth year is approximately:",appage,end="\n\n")
print("*****************************************************************************************")

print("Thank You For using the Personal Data Collector. Goodbye!")