'''
Multiprocessing in Python

Multiprocessing is a Python module that provides a simple way to run multiple 
processes in parallel. It allows you to take advantage of multiple cores or 
processors on your system and can significantly improve the performance of your 
code. In this repl, we'll take a closer look at the multiprocessing module and 
its various functions and how they can be used in Python.
'''

import multiprocessing
import requests
import concurrent.futures

def downloadFile(url, name):
  print(f"Started Downloading {name}")
  response = requests.get(url)
  open(f"OPPs/tut32-files/file-{name}.jpg", "wb").write(response.content)
  print(f"Finished Downloading {name}")
  

url = "https://picsum.photos/100/200"
# downloadFile(url, "file-11.jpg")

#* Using multiprocessing method
# processes = []
# if __name__ == '__main__':
#   for i in range(6):
#     p = multiprocessing.Process(target=downloadFile, args=[url, i])
#     p.start()
#     processes.append(p)
    
#   for process in processes:
#     #* wait until the child process is finished & then join all the processes
#     process.join()

#* Using the concurrent ProcessPoolExecutor
with concurrent.futures.ProcessPoolExecutor as executor:
  list_url = [url for i in range(10)]
  list_name = [i for i in range(10)]

  results = executor.map(downloadFile, list_url, list_name)
  for result in results:
    print(result)