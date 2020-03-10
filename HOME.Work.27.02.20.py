#Супер Бальон

class Ball(object):
    def __init__(self, type_="regular"):
      self.ball_type = type_
      

#Випадковий колір привида

import random

class Ghost(object):
  def __init__(self):
    self.color = random.choice(["white", "yellow", "purple", "red"])
    

#Адам і Єва

class Human():
    pass
    
class Man(Human):
    pass
    
class Woman(Human):
    pass

def God():
    adam = Man()
    eve = Woman()
    return [adam, eve]


#Класні класи

class Person(): __init__ = lambda s,n,a: setattr(s,"info",'{}s age is {}'.format(n,a))