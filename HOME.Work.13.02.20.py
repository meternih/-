#Дві точки
def distance(x1, y1, x2, y2):
    import math

    dist = round((math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)),2)

    return (dist)

#21 паличка
makeMove = lambda s: s % 4 or 1

#Без крику
def filter_words(stg):
    return " ".join(stg.split()).capitalize()

#Петля
create_array = lambda n: list(range(1,n+1))