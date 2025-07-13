# Calculate Factorial Using a Function
a = int(input("Enter a number:"))

def fact(num):
    if num<=1:
        return 1
    else:
        return num*(fact(num-1))

result = fact(a)
print("Factorial of",a,"is:",result)