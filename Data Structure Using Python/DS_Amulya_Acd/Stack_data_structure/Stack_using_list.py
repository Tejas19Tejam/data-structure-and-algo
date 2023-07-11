stack=[]
def push():
    element=input(" please Enter elements : ")
    stack.append(element)
    print(stack)


def pop():
    if not stack:
        print("Stack is empty !!!!")
    else:
        e=stack.pop()
        print("Element is removed : ",e)
        print(stack)


while True:
    print("""Plaese select the operation 1 . Push 
                                         2 . Pop 
                                         3 . Quite  """)

    choise=int(input())
    if choise==1:
        push()
    elif choise==2:
        pop()
    elif choise==3:
        break
    else:
        print("Please enter the correct input")



