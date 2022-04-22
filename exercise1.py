#First Q
num=int(input("Enter a number:"))
if (num % 2) == 0:  
   print("Input is even")  
else:  
   print("input is odd")  
#Second Q
celsius = float(input("Enter temperature in celsius: "))
fahrenheit = (celsius * 9/5) + 32
print('%.2f Celsius is: %0.2f Fahrenheit' %(celsius, fahrenheit))
