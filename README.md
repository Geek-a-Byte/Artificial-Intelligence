# AI-Sessional

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
