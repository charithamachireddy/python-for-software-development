value = 100   # global variable

def display():
    value = 50   # local variable
    print("Local value:", value)

display()
print("Global value:", value)