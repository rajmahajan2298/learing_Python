x = input("Enter Number 1: ")
y = input("Enter Number 2: ")

try:
    z = int(x) / int(y)
except ZeroDivisonError as e:
    print("Exception occured: " ,e)
    z = 0

print("division is: ",z)