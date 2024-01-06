### multithreading bn multiprocessingni farqi multithreading birinchi funksiya ishlagandan kegin qoganlari ishledi, multiprocessing xamma funksiya bir xil ishlashdi boshledi

import time
import multiprocessing
start=time.perf_counter()

def foo():
    print('Start running.... ')
    time.sleep(1)
    print('Done running.... ')
    
# foo()
# foo()

if __name__=='__main__':
    res=[]
    for _ in range(100):
        p=multiprocessing.Process(target=foo)
        p.start()
        res.append(p)
        
    for p in res:
        p.join()

finish=time.perf_counter()
print(f'Finished in {round(finish-start,2)} secs')