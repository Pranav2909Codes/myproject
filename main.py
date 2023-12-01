for i in range(1,11):
    print(i*3)

a = "My name is Pranav Vishwakarma"
print(a.format)
print(a.istitle())
print(a.swapcase())

a = int(input("Enter your age: "))
print("Your age is",a)

if (a>18):
    print("You can drive")
else:
    print("You can not drive")


Conditional operator   returns boolean(true or false)
 < ,> ,== ,<=,>= ,== ,!= 


Appleprice = 200
Budget = 323m
if (Appleprice >= Budget):
    print("Jarvis, add apple to the cart")
else:
    print("Jarvis, do not add apple to the cart")
          


num = int(input("Enter the num: "))
if (num < 0):
    print("Number is negative")
elif(num == 0):
    print("Number is zero")
else:
    print("Number is positive

Nested if-else statement

num = int(input("Enter the number: "))
if (num < 0):
    if (num < 0) and (num > -10):
        print("number is negative and between 0 to -10")
elif(num > 0):
    if (num > 0 and num <= 10):
        print("number is between 1 to 10")
    elif(num >10 and num <=20):
        print("number is between 11 to 20")
    else:
        print("number is positive")


Exercise

num = int(input("Enter the time: "))
if():





hour=int(input("Time in hours: "))
shift=input("AM or PM: ")

if hour <= 12 and ("AM" in shift):
    print("Good Morning")


elif hour>3 and hour<7 and ("PM" in shift):
    print("Good Evening")

elif  (hour <=12 and "PM" in shift):
    print("Good night")

else :
    print("Enter valid Time")


21 nov 2023##################################################################


for loop  ===iteration means Repetative execution of same block of code over and over

name = "Pranav vishwakarma"
for i in name:
    print(i + 1)

# parameter = start, stop, step

for i in range(1, 201 ,2):
    print(i)


i = 0
while(i<10):
    print(i)
    i = i + 3


i = int(input("Enter the number: "))
while(i<=50):
    i = int(input("Enter the number: "))
    print(i)
    
print("Done with the loop")

count = 5
while(count > 0):
    print(count)
    count = count - 1 

for i in range(1, 20):
    print(i)


count = 5  infinite loop
while(count > 0):
    print(count)
    count = count + 1 
