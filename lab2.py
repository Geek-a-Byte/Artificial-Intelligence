import copy
class Node:
    
    # b1=current measure of water in bottle 1,
    # b2=current measure of water in bottle 2,
    # m1=capacity of bottle 1
    # m2=capacity of bottle 2
    def __init__(self, b1,b2,m1=3,m2=4,parent=None):
        self.b1=b1
        self.b2=b2
        self.m1=m1
        self.m2=m2
        self.parent=parent
    
    def emptyb1(self):
        self.b1=0

    def emptyb2(self):
        self.b2=0

    def fillupb1(self):
        self.b1=self.m1
    
    def fillupb2(self):
        self.b2=self.m2
    
    def transferb1Tob2(self):
        if(self.b1==0):
            return
        self.b2=self.b2+self.b1
        self.b1=0

        if(self.b2>self.m2):
           extra=self.b2-self.m2
           self.b1=extra
           self.b2=self.b2-extra
    
    def transferb2Tob1(self):
        if(self.b2==0):
            return
        self.b1=self.b2+self.b1
        self.b2=0

        if(self.b1>self.m1):
           extra=self.b1-self.m1
           self.b2=extra
           self.b1=self.b1-extra
    def __str__(self):
        return f'(b1={self.b1},b2={self.b2})'

    # 3,0 3,0
    def __hash__(self):
        return self.b1+self.b2

    # 3,0 0,3
    def __eq__(self,other):
        if(other==None):
            return False
        if(self.b1==other.b1 and self.b2==other.b2 and self.m1==other.m1 and self.m2==other.m2):
            return True
        else:
            return False

node1 = Node(0,0,3,4,None)
node2 = Node(0,0)
myList=[]
mS=set()
mS.add(node1)
mS.add(node2)
print(node1==node2)    

listA=list()
listA.append(node1)
listA.append(node2)

def goalTest(node):
    if(node.b1==2 or node.b2==2):
        return True
    else:
        return False

node=Node(0,0,3,4)
result=goalTest(node)
print(result)

def bfs():
    initialNode=Node(0,0,3,4,None)
    if(goalTest(initialNode)):
        return initialNode
    frontier=[]
    frontier.append(initialNode)
    exploredSet=set()
    while True:
        if(len(frontier)==0): #empty frontier
           return None
        node=frontier.pop()
        exploredSet.add(node)

        child1=copy.deepcopy(node)
        child1.parent=node
        child1.fillupb1()


        child2=copy.deepcopy(node)
        child2.parent=node
        child2.fillupb2()

        child3=copy.deepcopy(node)
        child3.parent=node
        child3.emptyb1()
        # print(child3)

        child4=copy.deepcopy(node)
        child4.parent=node
        child4.emptyb2()
        # print(child4)
        
        child5=copy.deepcopy(node)
        child5.parent=node
        child5.transferb1Tob2()
        # print(child5)
        
        child6=copy.deepcopy(node)
        child6.parent=node
        child6.transferb2Tob1()
        # print(child6)


        childList=[child1,child2,child3,child4,child5,child6]
        for child in childList:
            # print(child)
            if(child not in exploredSet and child not in frontier):
               if(goalTest(child)):
                   return child
               else:
                   frontier.append(child)


x=bfs()
# print(x)

def printActions(node):
    seqlist=[]
    while True:
        if(node.parent==None):
            break
        else:
            seqlist.append(node)
            node=node.parent
    return seqlist

seqlist=printActions(x)
seqlist.reverse()
for node in seqlist:
    print(node)
