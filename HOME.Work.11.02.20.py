#паливо
def zeroFuel(a, b, c):
    return b * c >= a

#чи вистарчить місця?
def enough(cap, on, wait):
    return max(0, on + wait - cap)

#Банджо
def areYouPlayingBanjo(name):
    if name[0].lower() == 'r':
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'

#конвертувати булеве значення
def bool_to_word(boolean):
    return "Yes" if boolean else "No"

#Підрахунок овець
def count_sheeps(x):
  return x.count(True)

#Це мій хвіст?
def correct_tail(body, tail):
    return body.endswith(tail)