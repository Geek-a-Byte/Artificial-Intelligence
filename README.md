## Additional Resources

- https://www.youtube.com/watch?v=pDxbtrVDwSU
- https://www.youtube.com/watch?v=aWEKe7lQxNw

# AI-Sessional
## A* Search algo
```py
# g = the movement cost to move from the starting point to a given square on the grid, following the path generated to get there. 
# h = the estimated movement cost to move from that given square on the grid to the final destination. This is often referred to as the heuristic, which is nothing but a kind of smart guess. We really don’t know the actual distance until we find the path, because all sorts of things can be in the way (walls, water, etc.). There can be many ways to calculate this ‘h’ which are discussed in the later sections.

1. Get the square on the open list which has the lowest score. Let’s call
this square S.
2. Remove S from the open list and add S to the closed list.
3. For each square T in S’s walkable adjacent tiles:
a) If T is in the closed list: Ignore it.
b) If T is not in the open list: Add it and compute its score.
c) If T is already in the open list: Check if the F score is lower. If it is, update its score and update its parent as well.

def aStarSearch():
  take the initial node 
  do a goaltest
     if the initial node is the goal then return the initial node 
     else take a frontier queue and append the node # here frontier is the open list  
     
  initialize a set named explored # which is our closed list 
  while loop starts
     if frontier is empty 
        return failure/None
        
     sort the frontier queue based on f value = h+g of any node in the queue, so that we can find out the minimum node based on that f value
     
     take the front node from frontier, pop that frontnode from the frontier
     
     do a goaltest again, if it is goal then return this node
     
     add the node to explored set
     
     generate all the possible child nodes of that node 
     calculate the g of each child node
     assign the front node as parent of each child node
     
     assign all the childs to a child list
     
     for loop starts across child list
         # if a child is in frontier, not in explored then it will be explored later, 
         # if a child is explored but not in frontier, we will ignore it, 
         # if a child is explored and is in frontier -> not a valid possible case
         if child is in explored 
            continue
         if child in the childlist is not in frontier and not in explored
            insert the child into frontier
            
         elif child in frontier
            find out the index of the child in the frontier
            find out the child from that index through frontier[index]
            let infrontiernode = frontier[index]
            if h(child)+g(child)<h(infrontiernode)+g(infrontiernode)
               frontier[index]=child
     for loop ends   
```
## Mini-Max Algorithm in Artificial Intelligence
- Mini-max algorithm is a recursive or backtracking algorithm which is used in decision-making and game theory. It provides an optimal move for the player assuming that opponent is also playing optimally.
- Mini-Max algorithm uses recursion to search through the game-tree.
- Min-Max algorithm is mostly used for game playing in AI. Such as Chess, Checkers, tic-tac-toe, go, and various tow-players game. This Algorithm computes the minimax decision for the current state.
- In this algorithm two players play the game, one is called MAX and other is called MIN.
- Both the players fight it as the opponent player gets the minimum benefit while they get the maximum benefit.
- Both Players of the game are opponent of each other, where MAX will select the maximized value and MIN will select the minimized value.
- The minimax algorithm performs a depth-first search algorithm for the exploration of the complete game tree.
- The minimax algorithm proceeds all the way down to the terminal node of the tree, then backtrack the tree as the recursion.

## Pseudo-code for MinMax Algorithm

```
function minimax(node, depth, maximizingPlayer) is  
if depth ==0 or node is a terminal node then  
 return static evaluation of node  
  
if MaximizingPlayer then      // for Maximizer Player  
 maxEva= -infinity            
 for each child of node do  
    eva= minimax(child, depth-1, false)  
 maxEva= max(maxEva,eva)        //gives Maximum of the values  
 return maxEva  
  
else                         // for Minimizer player  
 minEva= +infinity   
 for each child of node do  
    eva= minimax(child, depth-1, true)  
 minEva= min(minEva, eva)         //gives minimum of the values  
 return minEva  
```

## Example

In this example, there are two players one is called Maximizer and other is called Minimizer.
Maximizer will try to get the Maximum possible score, and Minimizer will try to get the minimum possible score.
This algorithm applies DFS, so in this game-tree, we have to go all the way through the leaves to reach the terminal nodes.
At the terminal node, the terminal values are given so we will compare those value and backtrack the tree until the initial state occurs. 
Following are the main steps involved in solving the two-player game tree:

Step-1: In the first step, the algorithm generates the entire game-tree and apply the utility function to get the utility values for the terminal states. In the below tree diagram, let's take A is the initial state of the tree. Suppose maximizer takes first turn which has worst-case initial value =- infinity, and minimizer will take next turn which has worst-case initial value = +infinity.

![image](https://user-images.githubusercontent.com/59027621/179638056-74148ab2-5537-4dd3-a12e-5f2c7be17dbb.png)

Step 2: Now, first we find the utilities value for the Maximizer, its initial value is -∞, so we will compare each value in terminal state with initial value of Maximizer and determines the higher nodes values. It will find the maximum among the all.

```
For node D         max(-1, -∞) => max(-1, 4) = 4
For Node E         max(2, -∞)  => max(2, 6) = 6
For Node F         max(-3, -∞) => max(-3, -5) = -3
For node G         max(0, -∞)  => max(0, 7) = 7
```

![image](https://user-images.githubusercontent.com/59027621/179638268-dd93ce09-f5b1-4efa-ad09-72066f9beb29.png)

Step 3: In the next step, it's a turn for minimizer, so it will compare all nodes value with +∞, and will find the 3rd layer node values.

```
For node B = min(+∞,4) = min(4,6) = 4
For node C = min(+∞,-3) = min (-3, 7) = -3
```

![image](https://user-images.githubusercontent.com/59027621/179638511-b6872b4f-e3d4-4362-8c9e-551ed015077b.png)

Step 4: Now it's a turn for Maximizer, and it will again choose the maximum of all nodes value and find the maximum value for the root node. In this game tree, there are only 4 layers, hence we reach immediately to the root node, but in real games, there will be more than 4 layers.

```
For node A max(4, -3)= 4
```

![image](https://user-images.githubusercontent.com/59027621/179638605-f64c3513-2f51-4d8a-a864-d692681a2d0b.png)

That was the complete workflow of the minimax two player game.

## Properties of Mini-Max algorithm:
```
1. Complete- Min-Max algorithm is Complete. It will definitely find a solution (if exist), in the finite search tree.
2. Optimal- Min-Max algorithm is optimal if both opponents are playing optimally.
3. Time complexity- As it performs DFS for the game-tree, so the time complexity of Min-Max algorithm is O(bm), where b is branching factor of the game-tree, and m is the maximum depth of the tree.
4. Space Complexity- Space complexity of Mini-max algorithm is also similar to DFS which is O(bm).
```

## Limitation of the minimax Algorithm:
```
The main drawback of the minimax algorithm is that it gets really slow for complex games such as Chess, go, etc. 
This type of games has a huge branching factor, and the player has lots of choices to decide. 
This limitation of the minimax algorithm can be improved from alpha-beta pruning which we have discussed in the next topic.
```

## Alpha-Beta Pruning

- Alpha-beta pruning is a modified version of the minimax algorithm. It is an optimization technique for the minimax algorithm.
- As we have seen in the minimax search algorithm that the number of game states it has to examine are exponential in depth of the tree. Since we cannot eliminate the exponent, but we can cut it to half. 
- Hence there is a technique by which without checking each node of the game tree we can compute the correct minimax decision, and this technique is called pruning. 
- This involves two threshold parameter Alpha and beta for future expansion, so it is called alpha-beta pruning. It is also called as Alpha-Beta Algorithm.
- Alpha-beta pruning can be applied at any depth of a tree, and sometimes it not only prune the tree leaves but also entire sub-tree.

The two-parameter can be defined as:
- Alpha: The best (highest-value) choice we have found so far at any point along the path of Maximizer. The initial value of alpha is -∞.
- Beta: The best (lowest-value) choice we have found so far at any point along the path of Minimizer. The initial value of beta is +∞.

- The Alpha-beta pruning to a standard minimax algorithm returns the same move as the standard algorithm does, but it removes all the nodes which are not really affecting the final decision but making algorithm slow. Hence by pruning these nodes, it makes the algorithm fast.

![image](https://user-images.githubusercontent.com/59027621/179639526-ba8fc0c6-7e05-43d6-a4b4-2ad0479d8ee0.png)

### key points
``
The Max player will only update the value of alpha.
The Min player will only update the value of beta.
While backtracking the tree, the node values will be passed to upper nodes instead of values of alpha and beta.
We will only pass the alpha, beta values to the child nodes.
``
## Pseudocode

```
function minimax(node, depth, alpha, beta, maximizingPlayer) is  
if depth==0 or node is a terminal node then  
   return static evaluation of node  
  
if MaximizingPlayer then      // for Maximizer Player  
   maxEva= -infinity            
   for each child of node do  
     eva= minimax(child, depth-1, alpha, beta, False)  
     maxEva= max(maxEva, eva)   
     alpha= max(alpha, maxEva)      
     if beta<=alpha break  
   return maxEva  
    
else                         // for Minimizer player  
   minEva= +infinity   
   for each child of node do  
     eva= minimax(child, depth-1, alpha, beta, true)  
     minEva= min(minEva, eva)   
     beta= min(beta, minEva)  
     if beta<=alpha break          
   return minEva  
```

![293303012_1387177095105397_4748890868051727585_n](https://user-images.githubusercontent.com/59027621/179647783-4cf65bcc-fc92-4e38-8ddb-9a495857faa3.jpg)

# BFS / DFS

### last path comparison
bfs
![image](https://user-images.githubusercontent.com/59027621/179658629-ac4509a9-2ec5-4770-8329-acf72fdb1288.png)

dfs
![image](https://user-images.githubusercontent.com/59027621/179658994-cd28052e-4ccd-4649-bacc-29588a0c7a03.png)

### expansion comparison

bfs
![image](https://user-images.githubusercontent.com/59027621/179659108-3c3a03f7-aef7-492a-bbb1-37e0f43fb5a7.png)

dfs
![image](https://user-images.githubusercontent.com/59027621/179659157-6375eb12-7655-4528-852f-68c16968cd5f.png)
