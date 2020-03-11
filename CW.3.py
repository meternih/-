# Максимальне/мінімальне

number = []
k = int(input("Please enter the count of the elements of sequence: "))
for i in range(k):
     n = int(input("Please enter the element: "))
     number.append(n)
print(number)
max = number[0]
min = number[0]
for i in range(k):
    if number[i] > max:
        max = number[i]
    if number[i] < min:
        min = number[i]
print("Maximum number = %d. Minimum number = %d." %(max, min))


#  Від 1 до 10 визначити числа:  
#  парні % 2,
#  непарні % 3, 
#  числа які не % на 2 та 3.
#
x1 = []
x2 = []
x3 = []

for x in range(1, 11):
    
    #print(x, 'is even multiple of 2')
    if x % 2 == 0: 
        x1.append(x)
        
    #print(x, 'is an odd multiple of 3')    
    elif x % 3 == 0:
        x2.append(x)
        
    #print(x, 'not divisible by 2 and 3')    
    else:
        x3.append(x)
        
print(x1)        
print(x2)
print(x3)


# Факторіал числа без рекурсивного виклику функції

number = int(input("Enter number more then 0  "))
factorial = 1
for i in range(1, number + 1):
    factorial*= i  
print("Factorial", number, "equal", factorial)


# Напишіть скрипт, який перевіряє логін, який вводить користувач. 
# Якщо логін вірний (First), то привітайте користувача. 
# Якщо ні, то виведіть повідомлення про помилку. 
# (використайте цикл while)

login = input("Enter your login: ")
while login != str('First'):
    login = input("Entered login is incorrect! \nEnter your login again: ")
else:
    print("Welcome, ", login)
    

 
 
# Зчитування чисел. 0 та відємне - зупинка програми
mylist = []
number = int(input("Please enter the element: "))
while number > 0:
    mylist.append(n)
    number = int(input("Please enter the element: "))
else:
    print(mylist)
