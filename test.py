import math
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
numbers = [num1,num2]
product = math.prod(numbers)
sum = sum(numbers)
if product>1000:
    print("The sum is ",sum)
else:
    print("The product is ",product)