

import heapq

# create empty empty heap list  ( default heap conversion is min-heap)

heap=[]

# add elements to the empty heap by maintaining heap property 

heapq.heappush(heap,20)
heapq.heappush(heap,21)
heapq.heappush(heap,6)
heapq.heappush(heap,1)


# remove elements from the  heap by maintaining heap property 

heapq.heappop(heap)
heapq.heappop(heap)
print(heap)

# heapipy the following list 

lst=[1,4,8,2,4,9,10]

heapq.heapify(lst)
print(lst)



