import random
import copy


class Node:

    def __init__(self,puzzleBox=None):
        self.parent=None

        # fx[] = {+1, -1, +0, +0}
        # fy[] = {+0, +0, +1, -1}
        self.fx = []
        self.fy = []

        self.fx.append(1)
        self.fx.append(-1)
        self.fx.append(0)
        self.fx.append(0)

        self.fy.append(0)
        self.fy.append(0)
        self.fy.append(1)
        self.fy.append(-1)



        self.g=0
        self.h=0
        self.f=0

        # self.puzzleBox=puzzleBox
        self.puzzleBox=[[1, 1, 3, 1, 1, 2], [1, 1, 3, 3, 1, 1], [2, 3, 2, 2, 2, 2], [2, 2, 2, 1, 3, 1], [3, 3, 3, 2, 3, 2],
         [1, 3, 3, 2, 1, 3]]


     

    def fill_color(self,x,y,now_color,target_color,vis):
        #print(x,y)
        vis[x][y] = 1
        self.puzzleBox[x][y] = target_color
        for i in range (4):
            new_x = x+self.fx[i]
            new_y = y+self.fy[i]

            #print(x,y,new_x,new_y)

            if new_x<0 or new_x>5 or new_y<0 or new_y>5:
                continue
            if vis[new_x][new_y] == 1:
                continue
            if self.puzzleBox[new_x][new_y] == now_color:
                self.fill_color(new_x,new_y,now_color,target_color,vis)

        # overriding the functions for comparison
        def __hash__(self):
            hash = 0
            count = 1
            for i in range(3):
                for j in range(3):
                    hash = hash + count * self.puzzleBox[i][j]
                    count = count + 1
            return int(hash)

        def __eq__(self, other):
            if (other == None):
                return False

            equal = True
            for i in range(3):
                for j in range(3):
                    if (self.puzzleBox[i][j] == other.puzzleBox[i][j]):
                        continue
                    else:
                        equal = False
                        break
            return equal



    def display(self):
        print('*************************')
        for i in range(6):
            for j in range(6):
                print(f'({self.puzzleBox[i][j]})', end='')
            print('')
        print('*************************')

explored = set()
priority_queue = []
def sort_pq():
    for i in range(len(priority_queue)):
        for j in range(len(priority_queue) - 1):
            t1 = priority_queue[j]
            t2 = priority_queue[j + 1]
            if((t1.f)>(t2.f)):
                temp = t1
                t1=t2
                t2=temp
                priority_queue[j] = t1
                priority_queue[j+1] = t2

# def isExist(node):
#     temp_grid = node.puzzleBox
#     klag = 0
#     for i in range (len(explored)):
#         grid = explored[i].puzzleBox
#         flag=0
#         for j in range (6):
#             f=0
#             for k in range(6):
#                 if grid[j][k] != temp_grid[j][k]:
#                     f=1
#                     flag=1
#                     break
#             if f==1:
#                 break
#         if flag==1:
#             return True
#     return False

now_h=0

def goalTest(grid):
    a=0
    b=0
    c=0
    for i in range(6):
        for j in range(6):
            if grid[i][j]==1:
                a += 1
            elif grid[i][j]==2:
                b += 1
            else:
                c +=1
    if now_h==1:
        if(a==36):
            return True
    else:
        if a==36 or b==36 or c==36:
            return True
    return False

def h1(node):
    sum = 0
    grid = node.puzzleBox
    for i in range(6):
        for j in range(6):
            if grid[i][j]!=1:
                sum+=1
    return sum

def h2(node):
    grid = node.puzzleBox
    a=0
    b=0
    c=0
    for i in range(6):
        for j in range(6):
            if grid[i][j] == 1:
                a += 1
            elif grid[i][j] == 2:
                b += 1
            else:
                c += 1
    ll =[]
    ll.append(a)
    ll.append(b)
    ll.append(c)
    ll.sort()
    return -ll[2]

# vis=[]
# for j in range(6):
#     gg = []
#     for k in range(6):
#         gg.append(0)
#     vis.append(gg)
#
# node = Node()
# node.display()
# node.fill_color(0,0,node.puzzleBox[0][0],2,vis)
# node.display()
#
# print(node.puzzleBox)



def aStarSearch(node):

    priority_queue.append(node)

    while(len(priority_queue)>0):
        sort_pq()
        temp_node = priority_queue.pop(0)
        if(goalTest(temp_node.puzzleBox)):
            print(temp_node.f)
            return temp_node
        #temp_node.display()
        child1 = copy.deepcopy(temp_node)
        child2 = copy.deepcopy(temp_node)
        child3 = copy.deepcopy(temp_node)

        vis=[]
        for j in range(6):
            gg = []
            for k in range(6):
                gg.append(0)
            vis.append(gg)
        vis1 = copy.deepcopy(vis)
        vis2 = copy.deepcopy(vis)

        child1.fill_color(0,0,child1.puzzleBox[0][0],1,vis)
        child2.fill_color(0,0,child2.puzzleBox[0][0],2,vis1)
        child3.fill_color(0,0,child3.puzzleBox[0][0],3,vis2)

        child1.g = temp_node.g + 10
        if(now_h==1):
            child1.h = h1(child1)
        if(now_h==2):
            child1.h = h2(child1)
        #child1.h = h1(child1)
        child1.parent = temp_node
        child1.f = child1.g+child1.h


        child2.g = temp_node.g + 10
        if (now_h == 1):
            child2.h = h1(child2)
        if (now_h == 2):
            child2.h = h2(child2)
        #child2.h = h1(child1)
        child2.parent = temp_node
        child2.f = child2.g + child2.h

        child3.g = temp_node.g + 10
        #child3.h = h1(child1)
        if (now_h == 1):
            child3.h = h1(child3)
        if (now_h == 2):
            child3.h = h2(child3)
        child3.parent = temp_node
        child3.f = child3.g + child3.h

        childList = []

        if(child1.puzzleBox[0][0]!=temp_node.puzzleBox[0][0]):
            childList.append(child1)
        if(child2.puzzleBox[0][0]!=temp_node.puzzleBox[0][0]):
            childList.append(child2)
        if(child3.puzzleBox[0][0]!=temp_node.puzzleBox[0][0]):
            childList.append(child3)




        for child in childList:
            #print(11111)
            #child.display()
            if((child in explored)==False):
                priority_queue.append(child)
                explored.add(child)
    return None

kiri = []
kiri.append(0)

def call(node):
    if node.parent == None:
        return
    kiri[0]+=1
    call(node.parent)
    node.display()


real_node = Node()

node1 = copy.deepcopy(real_node)
node2 = copy.deepcopy(real_node)

now_h = 1
explored.clear()
priority_queue.clear()
xx = aStarSearch(node1)
call(xx)
print("After heuristic 1 move needs : ",end=' ')
print(kiri[0]-1)
print()


now_h = 2
explored.clear()
priority_queue.clear()
xx = aStarSearch(node2)
kiri[0] = 0
call(xx)
print("After heuristic 2 move needs : ",end=' ')
print(kiri[0]-1)

