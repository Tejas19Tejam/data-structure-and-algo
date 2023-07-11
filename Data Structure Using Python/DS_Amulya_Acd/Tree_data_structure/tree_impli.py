
def show_info(self):
    """
    Algorithm : 

    
    Topic : Binary Search Tree 
    1. Create node 
    2. Insertion Method 
        1. If BST is empty 
        2. If data < root node 
        3. If data > root node
        
        
    3. Search data is present or not 
        1. check if data is root 
        2. if data < root 
        3. if data > root 

    4. Traversing a binary tree

        1. In-order traversal 
        2. Pre-order traversal 
        3. Post-order traversal 

    5. Delete 

        1. Check empty or not 
        2. 

    """
    pass

class BST:
  def __init__(self,key):
    self.key=key
    self.lft=None
    self.rht=None

  # insertion 

  def insert(self,data):

    # if tree is empty 
    
    if self.key is None:
      self.key=data

    elif self.key==data:
      return

      """
      IF TREE IS NOT EMPTY :
        1. PLACE IT LHS -----> IF ----->  DATA <= NODE 
        2. PLACE IT RHS -----> IF ----->  DATA >= NODE 

      """
    elif data<self.key:
      if self.lft:
        self.lft.insert(data)
      else:
        self.lft=BST(data)
    elif data>self.key:
      if self.rht:
        self.rht.insert(data)
      else:
        self.rht=BST(data)


  def search(self,data):

    # compairing with root 

    if data==self.key:
      print(f'Given data {data} is root ')
    elif data<self.key:
      if self.lft:
        self.lft.search(data)
      else:
        print(f'Given data {data} is not present in the tree ')

    else:
      if self.rht:
        self.rht.search(data)
      else:
        print(f'Given data {data} is not present in the tree ')


    # traversing a binary tree 


    """ 

    1. Pre- order traversing 
    2. In - order traversing 
    3. Post order traversing 

    """

  def preorder(self):
    if self.key:
      print(self.key,end="---->")
      if self.lft:
        self.lft.preorder()
      if self.rht:
        self.rht.preorder()
    else:
      print("Tree is empty")


  def inorder(self):
      if self.lft:
        self.lft.inorder()
      print(self.key,end="--->")
      if self.rht:
        self.rht.inorder()

  def postorder(self):
        if self.lft:
            self.lft.postorder()
            
        if self.rht:
            self.rht.postorder()
            
        print(self.key,end=" ----> ")

  def delete(self,data,curr):

    # conditon 1 

    if self.key is None:
      print("Tree is empty")
      return
    
    # condition 2 

    elif data<self.key:
      if self.lft:
        self.lft=self.lft.delete(data,curr)
      else:
        print(f'{data} is not present')

    # condition 3 

    elif data>self.key:
      if self.rht:
        self.rht=self.rht.delete(data,curr)
      else:
        print(f'{data} is not present')

    # condition 4

    else:
      # if parant node contain 1 or 0 child 

        if self.lft is None:
            temp=self.rht
            if data==curr:
                self.key=curr.key
                self.lft=curr.lft
                self.rht=curr.rht
                temp=None
                return 

            self=None
            return temp

        if self.rht is None:
          temp=self.lft
          if data==curr:
            self.key=temp.key
            self.lft=temp.lft
            self.rht=temp.rht
            temp=None
            return
          self=None
          return temp

        else:
          # if parant node contain two child 
          node=self.rht
          while node.lft:
            node=node.lft
          self.key=node.key
          self.rht=self.rht.delete(node.key,curr)
    return self

  # Condition 5 
  # Deleting root naode 

  # find min-nade in the given tree 

  def min_node(self):
    current=self
    while current.lft:
      current=current.lft
    return current.key

  # find max-nade in the given tree 


  def max_node(self):
    current=self
    while current.rht:
      current=current.rht
    return current.key

# counting node present in the given tree 

def count(node):
  if node is None :
    return 0
  else:
    return 1+count(node.lft)+count(node.rht)


if __name__=="__main__":

  print(show_info.__doc__)


  # creating list of node

  lst=[12,13,14]

  # object 

  root=BST(lst[0])

  # inserting 

  for i in lst:
    root.insert(i)

  # printing count 

  print(f'Count of Node : {count(root)}')
  # root.preorder()

  print("Searching .......")
  root.search(8)

  # if count(root)>1:

  #   print(root.delete(12,root.key))
  # else:
  #   print("We can't delete ")

  print("Minimumm node : ",root.min_node())
  print("Maximum node : ",root.max_node())

  root.inorder()







