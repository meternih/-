# Cереднє арифметичне значення довільної кількості чисел.
 
# def ser(*numlist):
#     print(sum(numlist)/len(numlist))
# ser(34, 10, 20, 80)


# Повернення абсолютного значення числа

# type = int(input('Type number: '))
# print(abs(type))


#Написати програму, яка обчислює площу прямокутника, трикутника та кола.
# (написати три функції для обчислення площі, і викликати їх в головній програмі в залежності від вибору користувача)


# def triangle():
#   height = int(input('Height of triangle: '))
#   base = int(input('Base of triangle: '))
#   if height >= 1 and base >= 1:
#       print('Triangle area is: ', (height*base)/2)
#   else:
#     print('Height and base shouldn\'t be less than 1')
#     triangle()


# def rectangle():
#   legnth = int(input('Legnth of rectangle: '))
#   width = int(input('Width of rectangle: '))
#   if legnth >= 1 and width >= 1:
#     print('Rectangle area is: ', legnth * width)
#   else:
#     print('Legnth and width shouldn\'t be less than 1')
#     rectangle()



# def circle():
#   PI = 3.14
#   radius = int((input('Radius of circle: ')))
#   if radius >= 1:
#     print('Circle area is: ', PI*(radius**2))
#   else:
#     print('Radius shouldn\'t be less than 1')
#     circle()
    
# area = int(input('What area you want to find? If triangle - 1, rectangle - 2, circle - 3: '))
# while area != 1 and area != 2 and area !=3:
#     print('Choose between numbers 1, 2 or 3')
#     area = int(input('What area you want to find? If triangle - 1, rectangle - 2, circle - 3: '))
# if area ==1:
#     triangle()
# if area == 2:
#     rectangle()
# elif area == 3:
#     circle()