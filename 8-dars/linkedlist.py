### context manager ###
# with open('sample.txt','w') as file:
#     file.write('Hello world')

# class OpenFile:
#     def __init__(self, filename, mode) -> None:
#         self.filename=filename
#         self.mode=mode
        
#     def __enter__(self):
#         self.file=open(self.filename, self.mode)
#         return self.file
    
#     def __exit__(self, exc_t, axc_v, traceback):
#         self.file.close()
        
# with OpenFile('sample.txt','w') as file:
#     file.write('Salom, Dunyo')
    
# print(file.closed)

# list_a=[5,8,12,7,15,79]
# list_a.remove(8)
# print(list_a)
### linked list ###
# class Node:
#     def __init__(self, data=None) -> None:
#         self.data=data
#         self.next=None
        
# class LinkedList:
#     def __init__(self) -> None:
#         self.head=Node()
        
#     def append(self, data):
#         new_node=Node(data)
#         current=self.head
        
#         while current.next!=None:
#             current=current.next
#         current.next=new_node
        
#     def show(self):
#         current=self.head
#         elements=[]
        
            
#         while current.next!=None:
#             current=current.next
#             elements.append(current.data)
#         return elements
    
# my_l=LinkedList()
# my_l.append(2)
# my_l.append(1)
# my_l.append(4)
# print(my_l.show())

# buble sort -> selection sort -> insertion sort -> quick sort

### insertion sort ###
# def insertion_s(list_a):
#     index_l=range(1,len(list_a))
    
#     for i in index_l:
#         value=list_a[i]
        
#         while list_a[i-1]>value and i>0:
#             list_a[i],list_a[i-1]= list_a[i-1],list_a[i]
#             i=i-1
            
#     return list_a

# print(insertion_s([6,5,8,11,12]))