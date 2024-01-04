import threading
import time 
import concurrent.futures

start=time.perf_counter()
def index():
    print('Running a function.....')
    time.sleep(2.5)
    print('Complete a function ...')
    
    
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     res=executor.submit(index)    
    
    
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     res=[executor.submit(index, 2) for _ in range(10)]
    
#     for f in concurrent.futures.as_completed(res):
#         f.result()
    
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     seconds=[5,4,3,2,1]
    
#     res=[executor.submit(index, secds) for secds in seconds]
#     for f in concurrent.futures.as_completed(res):
#         f.result()  
         
# threads=[]    
# for _ in range(10):
#     t=threading.Thread(target=index, args=[2.4])
#     t.start()
#     threads.append(t)
    
# for thread in threads:
#     thread.join()
# thread1=threading.Thread(target=index)  
# thread2=threading.Thread(target=index)  
# thread3=threading.Thread(target=index)
# thread4=threading.Thread(target=index)

# thread1.start()
# thread2.start()
# thread3.start()
# thread4.start()

# thread1.join()
# thread2.join()
# thread3.join()
# thread4.join()

finish=time.perf_counter()
print(f'finished in {round(finish-start,2)} secs')