#Collection  = 1 variable used to save more then one values
#   List  = [] ordered and changeable. Duplicates 
#   Set   = {} unordered and immutable, but Add/Remove . NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates , FASTER
fruits = ["apple","banana","orange","orange","melon"]
#print(dir(fruits)) to see helpful directories used for list
#print(help(fruits)) to get help regarding directories
print(len(fruits))
print("apple"in fruits)
for x in fruits:
    print(x)
    print("------")
fruitss = {"apple","banana","orange","melon","melon"}
#print(dir(fruits)) to see helpful directories used for sets
#print(help(fruits)) to get help regarding directories
fruitss.add("nga")
for y in fruitss:
    print(y)
#touples r like list just faster