# Яке число більше?

z1 = int(input("Enter first number "))
z2 = int(input("Enter second number "))
if z1 > z2:
    print('First value is more then Second')
else:
   print('Second value is more then First') 
   
# Парне/Непарне

z = int(input("Enter any number "))
if z%2 == 0:
   print("Even number")
else:
   print("Odd number")
   
# Факторіал

nunber = int(input("Enter number that you need to find factorial for "))
factorial = 1
while nunber > 1:
    factorial *= nunber
    nunber -= 1
print(factorial)

# а.1 Роздрукувати всі парні числа менші 100 

vid = 0
print("printed all even number up to 100: ", end = '')
while vid < 100:
    print
    print(vid, end = " ")
    vid += 2
    
# a.2. Цикл - For
vid = range(100)
print("printed all even number up to 100: ", end = '')
z = 0
for i in vid:
    print(z, end = " ")
    z = z + 2
    if z > 100:
        break
    


