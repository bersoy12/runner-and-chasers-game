# Runner and Chasers' Game
This is my term project for artificial intelligence course.

## Introduction
![Screenshot of Board](https://github.com/bersoy12/runner-and-chasers-game/blob/main/pics/board.png)

Here is a prototype of the board. There are three agents in the environment. Red square, blue squares shows Runner, Chaser 1 and Chaser 2 respectively. Initial positions of the agents can be inputted arbitrarily before starting the game. Runner and Chasers can move either vertically or horizontally. Each agent can maintain its position during their turn.



## Methods
### Minimax Algorithm
The method used to move agents is minimax algorithm. 

![Search Tree for Sudoku](https://github.com/bersoy12/runner-and-chasers-game/blob/main/pics/searchtree.png)

picture from: https://medium.com/free-code-camp/playing-strategy-games-with-minimax-4ecb83b39b4b


Above, there is a search tree for Sudoku game. Similarly, Runner and Chasers are going to simulate each possible board appereances behind the scenes. Then, agent is going to make the possible best move with respect to the Manhattan Distance.

![alt text](https://github.com/bersoy12/runner-and-chasers-game/blob/main/pics/minimax.png)

picture from: https://medium.com/analytics-vidhya/artificial-intelligence-at-play-connect-four-minimax-algorithm-explained-3b5fc32e4a4f

### Manhattan Distance
![Calculation of Manhattan Distance](https://github.com/bersoy12/runner-and-chasers-game/blob/main/pics/manhattan.png)

picture from: https://en.wikipedia.org/wiki/Taxicab_geometry#/media/File:Manhattan_distance.svg

[Definition](https://xlinux.nist.gov/dads/HTML/manhattanDistance.html): The distance between two points measured along axes at right angles. In a plane with  p_1 (x_1,y_1) and p_2 (x_2,y_2), it is  d= |x_1- x_2 |+ |y_1- y_2 |

Manhattan Distance is quiet suitable for distance measurement since agents are only able to move in horizontal or vertical direction.


## The Game

The method which is used to move agents intelligent is minimax algorithm. In every turn, each agent calculates the Manhattan Distances between Runner and both Chasers. For this purpose, evaluate function is defined which calculates distances and returns maximum and minimum distances for the move. In minimax.py there is an simulate_move() method is defined. This method simulates every possible moves for the agent given as parameter. This method returns a board and list of boards of simulated moves are stored in get_all_moves() method. When we get all the boards from this function, minimax algorithm works on these boards. With respect to the type of the agent, minimax algorithm returns maximum distanced board and maximum distance if it is Runner, or minimum distanced board and minimum distance if it is a Chaser.


## Results and Recommendations
![Move](https://github.com/bersoy12/runner-and-chasers-game/blob/main/pics/play1.png)
![Move](https://github.com/bersoy12/runner-and-chasers-game/blob/main/pics/play2.png)

After several rounds:

![Move](https://github.com/bersoy12/runner-and-chasers-game/blob/main/pics/play3.png)


Positive Results:

-	Runner and Chaser 1 are moving in the logical direction according to their positions. 
-	Runner picks the furthest point from both chasers. 
-	Chaser 1 moves through Runner. 

Must be enhanced:
-	After several rounds of play, since runner always picks furthest point to move, Runner stucks at the corners even tough Runner and Chaser 1 are placed at the same row or column. Possibly it is because of the Chaser 2’s position.


## Inspired by 
[https://www.youtube.com/watch?v=RjdrFHEgV2o&t]
