import copy

class Node:
    # local vars
    # b1 , b2
    # c1 and c2
    def __init__(self,b1,b2,c1=3,c2=4,parent=None):
        self.b1=b1
        self.b2=b2
        self.c1=c1
        self.c2=c2
        self.parent=parent
    
    def __str__(self):
        return f'({self.b1},{self.b2})'

    def emptyb1(self):
        self.b1=0

    def emptyb2(self):
        self.b2=0

    def fillUpb1(self):
        self.b1=self.c1
    
    def fillUpb2(self):
        self.b2=self.c2

    def transferb1tob2(self):
        self.b2=self.b2+self.b1
        self.b1=0
        if(self.b2>self.c2):
            extra=self.b2-self.c2
            self.b2=self.b2-extra
            self.b1=extra
        else:
            pass
    
    def transferb2tob1(self):
        self.b1=self.b1+self.b2
        self.b2=0
        if(self.b1>self.c1):
            extra=self.b1-self.c1
            self.b1=self.b1-extra
            self.b2=extra        
        else:
            pass
    
    def __hash__(self):
        return self.b1+self.b2

    def __eq__(self,other):
        if(other==None):
            return False
        if(self.b1==other.b1 and self.b2==other.b2 and self.c1==other.c1 and self.c2==other.c2):
            return True
        else :
            return False
    
    
     
def goalTest(node):
    if(node.b1==2 or node.b2==2):
        return True
    else:
        return False



def bfs():
    initialNode=Node(0,0)
    
    if (goalTest(initialNode)):
        return initialNode
    
    frontier=[]
    frontier.append(initialNode)

    explored=set()    

    while True:
        
        if(len(frontier)==0):
            return None
        
        node=frontier.pop()
        #print(node)
        explored.add(node)

        child1=copy.deepcopy(node)
        child1.emptyb1()
        child1.parent=node

        child2=copy.deepcopy(node)
        child2.emptyb2()
        child2.parent=node

        child3=copy.deepcopy(node)
        child3.fillUpb1()
        child3.parent=node

        child4=copy.deepcopy(node)
        child4.fillUpb2()
        child4.parent=node
        
        child5=copy.deepcopy(node)
        child5.transferb1tob2()
        child5.parent=node

        child6=copy.deepcopy(node)
        child6.transferb2tob1()
        child6.parent=node

        childList=[child1,child2,child3,child4,child5,child6]

        for child in childList:
            
            if(child not in explored and child not in frontier):
                    if(goalTest(child)):
                        return child
                    frontier.append(child)
                   




goalNode=bfs()

def printPath(node):
    if(node==None):
        return
    printPath(node.parent)
    print(node)

printPath(goalNode)  


