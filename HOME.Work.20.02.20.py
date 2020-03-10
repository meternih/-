#Підсумок
def summation(num):
    return sum(xrange(num + 1))

#Виправити цикл
def list_animals(animals):
    return ''.join(str(i + 1) + '. ' + animals[i] + '\n' for i in range(0, len(animals)))

#Приберіть час
shorten_to_date = lambda d: d[:d.find(",")]