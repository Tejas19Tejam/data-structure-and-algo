# heap implementation using array 
# max_heapfy
def max_heapfy(arr,n):
    left_child=2*n+1
    right_child=2*n+2

    if left_child<len(arr) and arr[left_child]>arr[n]:
        large=left_child
    else:
        large=n
    if right_child<len(arr) and arr[right_child]>arr[n]:
        large=right_child
    if(large!=n):
        arr[n],arr[large]=arr[large],arr[n]
        max_heapfy(arr,large)


# driver code 

if __name__=="__main__":

    lst=[2,66,30,5,9,10]

    n=len(lst)

    # define max_heapfy
    for i in range(n//2,-1,-1):
        max_heapfy(lst,i)

    print(lst)
