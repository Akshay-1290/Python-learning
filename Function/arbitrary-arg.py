#arbitrary args are args with no fix numbers and for loop is used for computation (*)before name for ints(non key arguments) and (**) for strings(key arguments)
def add(*nums):
    total = 0
    for num in nums :
        total+=num
    return total

print(add(1,2,3,4,5,6))
print(add(*range(1,7)))

def name(**nam):
    for key,value in nam.items():
        print(f"{key}:{value}")

name(first_name="first",last="last")