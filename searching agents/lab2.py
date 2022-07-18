import copy

class Node:
    # b1,b2,m1,m2

    def __init__(self,b1,b2,m1=3,m2=4,parent=None):
        self.b1=b1
        self.b2=b2
        self.m1=m1
        self.m2=m2
        self.parent=parent


    def emptyb1(self):
        self.b1=0
    
    def emptyb2(self):
        self.b2=0

    def fillUpb1(self):
        self.b1=self.m1
    
    def fillUpb2(self):
        self.b2=self.m2
    
    def trasnferb1Tob2(self):
        if(self.b1==0):
            return
        self.b2=self.b2+self.b1
        self.b1=0
        if(self.b2>self.m2):
            extra= self.b2-self.m2
            self.b1=extra            
            self.b2=self.b2-extra 
    
    def trasnferb2Tob1(self):
        if(self.b2==0):
            return
        self.b1=self.b1+self.b2
        self.b2=0
        if(self.b1>self.m1):
            extra= self.b1-self.m1
            self.b2=extra            
            self.b1=self.b1-extra 
    
    def __str__(self):
        return f'(b1={self.b1},b2={self.b2})'

    def __hash__(self):
        return self.b1+self.b2

    def __eq__(self,other):
        if (other==None):
            return False
        if(self.b1==other.b1 and self.b2==other.b2 and self.m1==other.m1 and self.m2==other.m2):
            return True
        else:
            return False


node1=Node(3,0,3,4,None)
node2=Node(3,0,3,4,None)
myList=[]

mySet=set()
mySet.add(node1)
mySet.add(node2)
#print(node1==node2)
#print(mySet)

listA=list()
listA.append(node1)
listA.append(node2)

def goalTest(node):
    if(node.b1==2 or node.b2==2):
        return True
    else:
        return False

node=Node(0,2,3,4)
result=goalTest(node)
#print(result)

def bfs():
    initialNode=Node(0,0,3,4,None)
    if(goalTest(initialNode)):
        return initialNode
    frontier=[]
    frontier.append(initialNode)
    exploredSet=set()
    while True:
        if (len(frontier)==0): # empty frontier
            return None
        node=frontier.pop()
        exploredSet.add(node)
        
        child1=copy.deepcopy(node)        
        child1.parent=node
        child1.fillUpb1()
        

        child2=copy.deepcopy(node)
        child2.parent=node
        child2.fillUpb2()
        

        child3=copy.deepcopy(node)
        child3.parent=node
        child3.emptyb1()
        

        child4=copy.deepcopy(node)
        child4.parent=node
        child4.emptyb2()
        

        child5=copy.deepcopy(node)
        child5.parent=node
        child5.trasnferb1Tob2()
        

        child6=copy.deepcopy(node)
        child6.parent=node
        child6.trasnferb2Tob1()

        childList=[child1,child2,child3,child4,child5,child6]
        for child in childList:
            #print(child)
            if (child not in exploredSet and child not in frontier):
                if (goalTest(child)):
                    return child
                else:
                    frontier.append(child)

x=bfs()
#print(x)

def printActions(node):    
    seqList=[]
    while True:
        if(node.parent==None):
            seqList.append(node)
            break
        else:            
            seqList.append(node)
            node=node.parent   
    return seqList


seqList=printActions(x)
seqList.reverse()
print("The sequence are:")
for node in seqList:
    print(node)