class Vehicle:
    def __init__(self, name) -> None:
        self.name=name
        
class GoinerInterface:
    def go(self):
        print('I can go')
    
class FlyerInterface:
    def fly(self):
        print('I can fly')
        
class Car(Vehicle,GoinerInterface):
    pass

class Aircraft(Vehicle,GoinerInterface, FlyerInterface):
    pass

mashina=Car('Gentra')    
aircraft=Aircraft('Samalyot')


mashina.go()

aircraft.go()
aircraft.fly()