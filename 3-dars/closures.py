### global va local scope
# a=25
# def my_func():
#     name='Suxrob'
#     global a
#     print(a, name)
#     a=30
      
# my_func()
# print(a)

# name='Diyorbek'
# def my_func():
#     name='Suxrob'
    
#     def inner_func():
#         prefix='Google'
#         nonlocal name
#         print(prefix, name)
#         name='Baxrom'
#     inner_func()
#     return name
  
# print(my_func())
# print(name)

# def my_func():
#     age=16
#     name='Suxrob'
    
#     def inner(email):
#         print(email,name)
#     return inner
# execute=my_func()
# execute('s@gmail.com')
#### closer
# def counter(start):
#     def increment(step=1):
#         nonlocal start
#         start=start+step
#         print(start)
#     return increment
# my_func=counter(5)
# my_func()
# my_func()
# my_func()
# my_func()

# import re 
# text='''It is important to note that 54646463 most regular 65 expression programming operations are available car as module-level programingfunctions and methods 77 on compiled regular expressions. cars The functions are shortcuts that don’t require you to compile a regex object first, but miss some fine-tuning parameters.'''
# output=re.findall(r'[0-9]{1,9}', text)#1 xonali sondan kattasini topish uchun
# output=re.findall(r'programm?ing', text)
# output=re.findall(r'cars?', text)
# output=re.findall(r'[0-9]+', text)
# print(output)

### Iterators and iterables ###
#next
# text='banana'
# my_list=iter(text)
# print(next(my_list))
# print(next(my_list))
# print(next(my_list))
# print(next(my_list))
# print(next(my_list))
# print(next(my_list))
