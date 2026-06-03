# multiple inheritance = inherit from more than one parent class
#                                        C(A, B)

# multilevel inheritance = inherit from a parent which inherits from another parent
#                                          C(B) <- B(A) <- A

# --------------1-----------------
class animal():
    def __init__(self,name,category):
        self.name=name
        self.category=category
    def is_alive(self):
        print(f"{self.name} is alive")
    def cate(self):
       print(f"{self.name} is of category {self.category}")
class Human():
    def human(self):
     print("Human is also a animal")

class athrb(animal,Human):
   pass
athrv=athrb("Atharv","Human")

athrv.is_alive()
athrv.cate()
athrv.human()

#----------------2----------------
class animal():
    def __init__(self,name,category):
        self.name=name
        self.category=category
    def is_alive(self):
        print(f"{self.name} is alive")
    def cate(self):
       print(f"{self.name} is of category {self.category}")
class Human(animal):
    def human(self):
     print("Human is also a animal")

class athrb(Human):
   pass
athrv=athrb("Atharv","Human")

athrv.is_alive()
athrv.cate()
athrv.human()

#above somehow both doing same work but can do different according to use