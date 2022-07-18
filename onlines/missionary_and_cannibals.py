# your code goes here
import copy

class Node:
    # b1,b2,m1,m2
        
    def __init__(self,b1,b2,m1=3,m2=3,parent=None,flag=0):
        self.b1=b1
        self.b2=b2
        self.m1=m1
        self.m2=m2
        self.parent=parent
        self.flag = flag

    def pathaboOneM(self):
        self.b1 += 1
        self.m1 -= 1
        self.flag=1
        
    def pathaboOneR(self):
        self.b2 += 1
        self.m2 -=1
        self.flag=1

    def pathaboMan(self):
        #x = min(self.m1,2)
        self.b1 += 2
        self.m1 -= 2
        self.flag=1

    def pathaboRakkhosh(self):
        #x = min(self.m2,2)
        self.b2 += 2
        self.m2 -= 2
        self.flag=1

    def bothpathabo(self):
        self.b1 +=1
        self.b2 += 1
        self.m1 -= 1
        self.m2 -= 1
        self.flag=1

    def ferotMan(self):
        self.b1-=1
        self.m1+=1
        self.flag=0
        
    def ferotRakkhosh(self):
        self.b2-=1
        self.m2+=1
        self.flag=0


    def ferotTMan(self):
        self.b1-=2
        self.m1+=2
        self.flag=0
        
    def ferotTRakkhosh(self):
        self.b2-=2
        self.m2+=2
        self.flag=0
        
    def ferotboth(self):
        self.b1 -= 1
        self.m1+=1
        self.b2 -= 1
        self.m2+=1
        self.flag=0


    
    def __str__(self):
        return f'(b1={self.b1},b2={self.b2},m1={self.m1},m2={self.m2},flag={self.flag})'

    def __hash__(self):
        return self.b1+self.b2

    def __eq__(self,other):
        if (other==None):
            return False
        if(self.b1==other.b1 and self.b2==other.b2 and self.m1==other.m1 and self.m2==other.m2 and self.flag==other.flag):
            return True
        else:
            return False




def goalTest(node):
    if(node.m1==0 and node.m2==0):
        return True
    return False

def test1(node):
    if(node.b1<0 or node.b2<0 or node.m1<0 or node.m2<0):
        return True
    if(node.b1<node.b2 and node.b1>0):
        return True
    if(node.m1<node.m2 and node.m1>0):
        return True
    return False


#print(result)

def bfs():
    initialNode=Node(0,0,3,3,None)
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

        #print(node)
        
        child1=copy.deepcopy(node)        
        child1.parent=node
        child1.pathaboMan()
        

        child2=copy.deepcopy(node)
        child2.parent=node
        child2.pathaboRakkhosh()
        
        child3=copy.deepcopy(node)
        child3.parent=node
        child3.ferotMan()
        

        child4=copy.deepcopy(node)
        child4.parent=node
        child4.ferotRakkhosh()

        child5=copy.deepcopy(node)
        child5.parent=node
        child5.bothpathabo()

        child6=copy.deepcopy(node)
        child6.parent=node
        child6.pathaboOneM()

        child7=copy.deepcopy(node)
        child7.parent=node
        child7.pathaboOneR()

        child8=copy.deepcopy(node)
        child8.parent=node
        child8.ferotboth()

        
        child9=copy.deepcopy(node)
        child9.parent=node
        child9.ferotTMan()

        child10=copy.deepcopy(node)
        child10.parent=node
        child10.ferotTRakkhosh()

        childList=[]
        if(node.flag==0):
            childList=[child1,child2,child5,child6,child7]
        else:
            childList=[child3,child4,child8,child9,child10]
        
        for child in childList:
            
            #if(node.flag==1):
                #print(child,2,node)
            if (child not in exploredSet and child not in frontier):
                if(test1(child)):
                   continue
                elif (goalTest(child)):
                    return child
                else:
                    #print(child,1)
                    frontier.append(child)

x=bfs()
print(x)

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
