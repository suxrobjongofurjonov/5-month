### SOLID ###
# nums=[1,2,3]#iterable
# i_nums=(nums).__iter__()#iterator
# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))

# nums=[1,2,3]#iterable
# iterator_nums=iter(nums)#iterator

# while True:
#     try:
#         item=next(iterator_nums)
#         print(item)
#     except StopIteration:
#         break

# class MyRange:
#     def __init__(self, start, end) -> None:
#         self.start=start
#         self.end=end
        
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.start>=self.end:
#             raise StopIteration
        
#         self.start+=1
#         return self.start -1
    
# nums=MyRange(1,10)
# for i in nums:
#     print(nums)

### SOLID ###
# programming paradigms: 1)imperative paradigm;1)prodecular programming, 2)OOP, 3)structured programming. 2)declarative paradigm;1)functional programming, 2)logic programming
#S=single resposibility, 1maqsad=1qator
#O=open to extend but closed to change
#L=liskov substitution principle
#I=interface segregation principle
#D=dependency inversion principle
##########################
# import time
# class Logger:
#     def __init__(self) -> None:
#         self.prefix=time.strftime('%Y-%B-%d %H:%M:%S', time.localtime())
#     def log(self, message):
#         print(f'{self.prefix}-->{message}')
        
# class CustomerLogger(Logger):
#     def __init__(self) -> None:
#         super().__init__()
#         self.prefix=time.strftime('%Y-%B-%d', time.localtime())
               
# logger=Logger()
# logger.log('-Soat minut sekund kerak')
###############################
# class Creature:
#     def __init__(self, name, age) -> None:
#         self.value={'name':name, 'age':age}
        
#     def eat(self):
#         print('I can eat')
        
# dog=Creature('Reks', 5)
# cat=Creature('Kisa', 2)
# hen=Creature('noname', 4)
# horse=Creature('Olov',8)
# arrributes=(dog,cat,hen,horse)

# for i in arrributes:
#     print(i.value['name'])
#######################
# class Creature:
#     def __init__(self, name) -> None:
#         self.name=name
    
#     def eat(self):
#         print('I can eat')
        
# class SwimmerInterface:        
#     def swim(self):
#         print('I can swim')

# class WalkerInterface:       
#     def walk(self):
#         print('I can walk')

# class TalkerInterface:        
#     def talk(self):
#         print('I can talk')
        
# class Human(Creature, SwimmerInterface, WalkerInterface, TalkerInterface):
#     pass

# class  Fish(Creature, SwimmerInterface):
#     pass

# class Snake(Creature):
#     pass

# fish=Fish('skumbria')
# javohir=Human('Javohir') 
# snake=Snake('Python')

# snake.eat()

# javohir.walk()
# javohir.talk()
# javohir.swim()

# fish.eat()
# fish.swim() 
########################
import time

class TerminalPrinter():
    def write(self, msg):
        print(f'{msg}')
        
class FilePrinter():
    def write(self, msg):
        with open('loq.txt', 'a+', encoding='UTF-8') as file:
            file.write(f'{msg}')
            
class Logger:
    def __init__(self) -> None:
        self.prefix=time.strftime('%Y-%B-%d %H:%M:%S', time.localtime())
    
        
    def log_terminal(self, message):
        TerminalPrinter().write(f'{self.prefix}-->{message}')
        
    def log_file(self, message):
        FilePrinter().write(f'{self.prefix}-->{message}')
               
logger=Logger()
logger.log_terminal('Hello World', FilePrinter)
logger.log_terminal('Hello World', TerminalPrinter)