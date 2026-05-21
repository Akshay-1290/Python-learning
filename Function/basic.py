#A block of reusable code in called a function
def add(a,b):
    c=a+b
    return c
a = float(input("enter a :"))
b = float(input("Enter b :"))
print(add(a,b))

def greeting(username):
    print(f"hi {username}")
    print("have a good day")


username = input("Enter you name :")
print(greeting(username))