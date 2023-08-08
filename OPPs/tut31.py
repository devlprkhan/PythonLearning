'''
Multithreading in Python

Multithreading is a technique in programming that allows multiple threads of 
execution to run concurrently within a single process. In Python, we can use 
the threading module to implement multithreading. In this tutorial, we will 
take a closer look at the threading module and its various functions and how 
they can be used in Python.
'''

import threading
from concurrent.futures import ThreadPoolExecutor
import time

#* Normal way (without threading)
def execWithTime(sec):
  time.sleep(sec)
  print(f"Executing for {sec} seconds")
  return sec

# t1 = time.perf_counter()
# execWithTime(4)
# execWithTime(2)
# execWithTime(1)
# t2 = time.perf_counter()
# print(f"Time consumed: {t2-t1} seconds")

#* With Threading
def mulThreadFunc():
  t1 = time.perf_counter()
  print("Hello from thread", threading.current_thread().name)
  thread1 = threading.Thread(target=execWithTime, args=[4])
  thread2 = threading.Thread(target=execWithTime, args=[3])
  thread3 = threading.Thread(target=execWithTime, args=[2])
  thread4 = threading.Thread(target=execWithTime, args=[1])
  
  thread1.start()
  thread2.start()
  thread3.start()
  thread4.start()
  t2 = time.perf_counter()
  print("Time consumed in threads:-----", t2-t1)

# mulThreadFunc()

#* Advance technique of threads and most used
def poolingDemo():
  with ThreadPoolExecutor() as executor:
    #* Manual Way
    # future1 = executor.submit(execWithTime, 4)
    # future2 = executor.submit(execWithTime, 2)
    # future3 = executor.submit(execWithTime, 1)
    
    # print(future1.result())
    # print(future2.result())
    # print(future3.result())
    
    #* Using Map method
    l = [2,3,5,4]
    result = executor.map(execWithTime, l)
    for res in result:
      print(res)
      
poolingDemo()