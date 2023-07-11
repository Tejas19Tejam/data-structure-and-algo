queue=[]

def enqueue():
    element=input("Please Enter Elements :")
    queue.append(element)
    print(element,"is added to the queue")

def dequeue():
    if not queue:
        print("Queue is empty ")

    else:
        e=queue.pop(0)
        print(e,"element is deleted")
def show():
    print(queue)

    while True:
        print("Please select following options 1 . Add  2 . Delete  3. Show  4 . Exit")
        option=int(input())
        if option==1:
            enqueue()

        elif option==2:
            dequeue()

        elif option==3:
            show()
        elif option==4:
            break
        else:
            print("Please select correct option")
                