#Підсумок
def summation(num):
    return sum(xrange(num + 1))

#Виправити цикл
def list_animals(animals):
    return ''.join(str(i + 1) + '. ' + animals[i] + '\n' for i in range(0, len(animals)))

#Подвійна куля
def double_char(s):
    return ''.join(char * 2 for char in s)
