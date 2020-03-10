#Чи є верхній регістр рядка?

def is_uppercase(inp):
    return inp == inp.upper()

#Сортувати підручники

sorter = lambda textbooks: sorted(textbooks, key = str.lower)

#Приберіть час

shorten_to_date = lambda d: d[:d.find(",")]