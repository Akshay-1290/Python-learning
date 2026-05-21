#default arguments are the arguments which have fix value most of the times so it doesnt change in funtion until changed intensionalyy by entering new value while execution
# arguments -----> which are written after def in bracket 
def root(x,y=2):
    
    x=x**(1/y)
    return x
print(root(4))
print(root(4,2))
print(root(16))
print(root(16,4))
#default argument is placed after normal argument
