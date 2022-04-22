#3
# Three sides of the triangle is a, b and c:  
a = float(input('Enter first side: '))  
b = float(input('Enter second side: '))  
c = float(input('Enter third side: '))  
  
# calculate the semi-perimeter  
s = (a + b + c) / 2  
  
# calculate the area  
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5  
print('The area of the triangle is %0.2f' %area)
#4
n=int(input("Enter the total number you want to enter:"))

sum=0

for i in range(n):

    x=int(input("Enter the number:"))

    sum=sum+x

avg=sum/n

print("Average=",avg)
#5
