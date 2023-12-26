class Person:
    def __init__(self, name, age) -> None:
        self.name=name
        self.age=age
        
    def talk(self):
        print('I can talk')
        
boy=Person('Suxrob', 16)
girl=Person('Mushtariy', 15)
adult=Person('Gofurjon', 72)
people=(boy, girl, adult)

for var in people:
    print(var)