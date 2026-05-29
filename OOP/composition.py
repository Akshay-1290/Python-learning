class Engine():
    
    def __init__(self,hp):
        self.hp=hp

class Tyre():

    def __init__(self,size):
        self.size=size

class Car():
    def __init__(self,made,name,hp,tyre_size):
        self.made=made
        self.name=name
        self.engine=Engine(hp)
        self.wheel=[Tyre(tyre_size) for wheel in range(4)]
    def abt_car(self):
        print(f"{self.made} {self.name} of {self.engine.hp} horsepower {self.wheel[0].size}")

car=Car("Maruti","Omni Van",-5,20)
car.abt_car()
