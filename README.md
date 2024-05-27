# Sudoku Solver
#### Description

#### Technology Used
    - Pygame

In this project I have created a sudoku board solver. To implement the project I first learned the back trackking algorithm to find the solution
of the given board. The algorithm works by filling each empty space with the correct number defined by the rules of sudoku at a time and then back tracking to the previous empty space if there is no correct number to fill the current position.

The second part of the project was the design of a basic user interface for the game. To accomplish this, I used pygame. Pygame is a relatively easy framework to learn but takes time to get familiar with. The UI is a simple opening screen that displays the game instructions. A new game starts after hitting the space bar and the clock starts. To enter a number into the board, you have to select the cube which disbales all the other positions and highlights the selected board. Once the cube is filled the background of the cube is filled with a color to keep track of the playable cubes. If a user wants to change a number, he should simply click the cube and enter backspace which resets the cube to 0.
 To get the solved answer, the user has to press enter, which runs the algorithm and gives the result within seconds

There are many additional things that can be implemented further, for example storing other boards in a database or generating new random boards. The next step would be to use OPENCV to detect a board and give a solution.
