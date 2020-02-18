# 1.  Створити список цілих чисел, які вводяться з терміналу та 
# визначити серед них максимальне та мінімальне число.

# cile4uslo = []
# value = int(input(" Enter the count of the elements of sequence: "))
# for i in range(value):
#     element = int(input("Please enter the element: "))
#     cile4uslo.append(element)
# print(cile4uslo)
# max = cile4uslo[0]
# min = cile4uslo[0]
# for i in range(value):
#     if cile4uslo[i] > max:
#         max = cile4uslo[i]
#     if cile4uslo[i] < min:
#         min = cile4uslo[i]
# print("max 4islo = {}. Min 4islo = {}.".format(max, min))

# другий варіант)))))!!!!!!!

# cile4uslo = []
# value = int(input(" Enter the count of the elements of sequence: "))
# for i in range(value):
#     element = int(input("Please enter the element: "))
#     cile4uslo.append(element)
# print(cile4uslo)
# max = cile4uslo[0]
# min = cile4uslo[0]
# for i in range(value):
#     if cile4uslo[i] > max:
#         max = cile4uslo[i]
#     if cile4uslo[i] < min:
#         min = cile4uslo[i]
#     print("max 4islo = {}. Min 4islo = {}.".format(max, min))

# spisok_4isel = [int(input("Enter int {}: ".format(i + 1))) for i in range(int(input("Enter amount: ")))]
# print(spisok_4isel)
# print("Max 4islo is: ", max(spisok_4isel))
# print("Min 4islo is: ", min(spisok_4isel))


# kilkist_fayliv = int(input("Input kilkist failiv: "))
# spisok_4isel = [int(input(" Input nastupne 4islo: ")) for i in range(kilkist_fayliv)]
# print(" Max 4islo = {}. Min 4islo = {}. ".format(max(spisok_4isel), min(spisok_4isel)))


# 2.  В інтервалі від 1 до 10 визначити числа 
# •  парні, які діляться на 2,
# •  непарні, які діляться на 3, 
# •  числа, які не діляться на 2 та 3.

# for x in range(1, 11):
#     if x % 2 ==0:
#         print(x, "is even multiple of 2")
#     elif x % 3 == 0:
#         print("is even multiple of 3")
#     else:
#         print(x, "not divisible by 2 and 3")
        
        
        
# x1 = []
# x2 = []
# x3 = []
# for x in range(1, 11):
#    if x % 2 == 0:
#        print(x, "is even multiple of 2")
#        x1.append(x)
#    elif x % 3 == 0:
#        print(x, "is even multiple of 3")
#        x2.append(x)
#    else:
#        print(x, "not divisible by 2 and 3")
#        x3.append(x)
# print(x1)
# print(x2)
# print(x3)

#факторіал

# number = int(input("vuberit 4uslo: "))
# factorial = 1
# if number < 0:
#     print("vuba4te vuberit pozutuvne zna4enya.")
# elif number == 0:
#     print("factorial 4usla o bude 1")
# else:
#     for i in range(1, number + 1):
#         factorial = factorial*i
#     print("Factorial of {0} is {1}".format(number, factorial))

# number = int(input("Vvedit cile dodatne 4uslo: "))
# factorial = 1
# for i in range(1, number + 1):
#     factorial*= i
# print("factorial 4usla", number, "dorivnue", factorial)


    
    
    