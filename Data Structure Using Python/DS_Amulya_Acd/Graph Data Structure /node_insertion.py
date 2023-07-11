


class Graph:
    def __init__(self,node_list):
        self.node_list=node_list
        self.graph=[]

    #  Funcrion to add a node using adjacency matrix representation 
    def add_node(self,value):
        if value in self.node_list:
            print(f'{value} is present in the graph ')
            return 
        else:
            self.node_list.append(value)
            self.adj_matrix=list([0 for i in range(len(self.node_list))] for j in range(len(self.node_list)))

    #  Funcrion to add an edge between two vertices using adjacency matrix representation 
    def add_edge(self,v1,v2):
        if v1 not in self.node_list:
            print(f'{v1} is not present in the list ')
        elif v2 not in self.node_list:
            print(f'{v2} is not present in the list ')
        else:
            # self.adj_matrix=list([])
            indOfv1=self.node_list[v1]
            indOfv2=self.node_list[v2]
            self.adj_matrix[indOfv1][indOfv2]=1
                    


    def print_graph(self):
        print(self.node_list)
        return self.adj_matrix
    


            
            


if __name__=="__main__":

    node_list=[]
    ob=Graph(node_list)
    ob.add_node("A")
    ob.add_node("B")
    ob.add_edge("A","B")

    # print adjacency matrix 
    adj_matrix=ob.print_graph()
    for col in range(len(adj_matrix)):
            for row in range(len(adj_matrix)):
                print(adj_matrix[col][row],end=" ")
            print()
