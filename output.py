# a = int(input("enter value of a :"))
# b = int(input("enter value of b :"))
# print(a,b,a,b,sep = ",", end = "ended here.\n")# here sep is used to seperate the outputs of every variable and end is used to print the given statement at the end of the print statement
# # here seperate which seberate using , in the output


# name = input("enter name :")
# print("hello",name,sep = "," ,end = "!\n")  

# c = int(input("Enter the value of c :"))
# print("you entered ",c,sep = ":")

# d = float(input("enter the value of d :"))
# print("value of PI:",d,sep=" ")

# # 1. Take a single string input from the user (e.g., "10 20 30")
# e = input("enter value of e : ") 
# # 2. Split the string into 3 separate items wherever there is a space
# # Note: Using .split() without " " is safer as it handles multiple spaces automatically
# x, y, z = e.split(" ")
# # 3. Convert each string into an integer so they can be mathematically added
# total_sum = int(x) + int(y) + int(z)
# # 4. Display the final result to the user
# print(total_sum)

# a = input("enter your name and age ")
# name,age = a.split(",")
# print("Name:",name,",Age:",age,sep="")


# x,y=input("enter the value of a and b : ").split(",")
# a = int(x)
# b = int(y)
# print("addition:",a+b,"substraction:",a-b,"multiplication:",a*b,"division:",a/b, sep=" ")



# 1. Take a single string input, split it by the comma, and assign to x and y
x, y = input("enter value of a and b : ").split(",")
# 2. Convert the string values into integers for proper comparison
a = int(x)
b = int(y)
# 3. Print the results using an f-string to dynamically insert values and boolean results
print(f"{a}>{b}:{a>b} {a}=={b}:{a==b} {a}<{b}:{a<b}  {a}!={b}:{a!=b}")

