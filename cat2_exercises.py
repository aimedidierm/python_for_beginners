# Q1
num=int(input("Enter a number:"))
if (num % 2) == 0:  
   print("Input is even")  
else:  
   print("input is odd")  
#Q2
celsius = float(input("Enter temperature in celsius: "))
fahrenheit = (celsius * 9/5) + 32
print('%.2f Celsius is: %0.2f Fahrenheit' %(celsius, fahrenheit))
#Q3
# Three sides of the triangle is a, b and c:  
a = float(input('Enter first side: '))  
b = float(input('Enter second side: '))  
c = float(input('Enter third side: '))  
  
# calculate the semi-perimeter  
s = (a + b + c) / 2  
  
# calculate the area  
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5  
print('The area of the triangle is %0.2f' %area)
#Q4
n=int(input("Enter the total number you want to enter:"))

sum=0

for i in range(n):

    x=int(input("Enter the number:"))

    sum=sum+x

avg=sum/n

print("Average=",avg)
#Q5
import math

r=float(input("Enter the value of radius:"))

Area=3.14*r*r

print("The area of circle is", Area)

Circumference=2*3.14*r

print("The circumference of circle is", Circumference)
#Q6
# Assumes that n is a positive integer 

def isMultipleof5(n):
    while ( n > 0 ):
        n = n - 5
    if ( n == 0 ):
        return 1
    return 0     
# Driver Code
i = int(input("Enter the integer:"))
if ( isMultipleof5(i) == 1 ):
    print (i, "is multiple of 5")
else:
    print (i, "is not a multiple of 5")
#Q7
sum = 0
count = 0

while count<10:
    n = float(input('Enter a number: '))
    sum = sum + n
    count = count + 1

average = sum/10

print(f'The average of these numbers is: {average}')
#Q8
multiplyValues = 8*16*22*12*41
n = 5
geometricMean = (multiplyValues)**(1/n)
print ('The Geometric Mean is: ' + str(geometricMean))
