'''
Dictionary Methods
'''

ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
ep2 = {222: 67, 566: 90}

ep1.update(ep2) #join ep2 to ep1
print(ep1)

# ep1.clear()#clear ep1
# print(ep1) #{}
ep1.pop(567)
print(ep1) #remove the 567 from ep1

ep1.popitem() #remove from ep1 last item

del ep1[123] #delete 123 from ep1
print(ep1)