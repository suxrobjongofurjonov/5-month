### multithreading bn multiprocessingni farqi multithreading birinchi funksiya ishlagandan kegin qoganlari ishledi, multiprocessing xamma funksiya bir xil ishlashdi boshledi

import time
# import multiprocessing
import concurrent.futures

start=time.perf_counter()

def foo(num):
    print(f'Start running {num}.... ')
    time.sleep(num)
    print(f'Done running {num}.... ')
    
# foo()
# foo()

# if __name__=='__main__':
#     res=[]
#     for _ in range(100):
#         p=multiprocessing.Process(target=foo)
#         p.start()
#         res.append(p)
        
#     for p in res:
#         p.join()

# if __name__=='__main__':
#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         secs=[5,4,3,2,1]
#         res=executor.map(foo, secs)
        
#         for i in res:
#             print(i)

finish=time.perf_counter()
print(f'Finished in {round(finish-start,2)} secs')

