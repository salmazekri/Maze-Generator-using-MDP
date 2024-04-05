# Maze-Generator-using-MDP
# Maze Generator

MDPs, or Markov Decision Processes, are mathematical frameworks used in the field of reinforcement learning to model decision-making processes. They consist of states, actions, transition probabilities, and rewards. In an MDP, an agent takes actions in states and receives rewards based on those actions, with the goal of maximizing cumulative rewards over time.

This code generates a maze using policy iteration and value iteration algorithms. It utilizes a `main` function to generate the maze and policy, as well as a `maze_to_mdp` function to convert the maze to a Markov Decision Process. The code also includes functions to count paths and modify the maze.

## Policy Iteration

The `policyiteration` function performs policy iteration on the generated maze. It initializes the walls and policies of the maze, and then iteratively evaluates and improves the policy until convergence. At each iteration, it prints the values and policies of the states. The `evaluate_policy` function calculates the value of each state using the policy, and the `improve_policy` function updates the policy based on the values.

## Value Iteration

The `value_iteration` function performs value iteration on the generated maze. It initializes the walls and policies of the maze, and then iteratively updates the values of the states until convergence. At each iteration, it prints the values of the states. The `animate_values` function visualizes the maze with the updated values.

## Counting Paths and Modifying the Maze

The code also includes functions to count the number of possible paths from a given wall (`count_paths`), remove a selected wall from the list of walls (`remove_wall`), and modify the adjacent states of a selected wall based on their position (`modify_upper`, `modify_left`, `modify_right`, `modify_bottom`). These functions are used in the main algorithms to generate and manipulate the maze.

To use this code, simply run the `main2` function with the desired maze and grid.
This readme provides instructions on how to run the Maze Solver code.

##Prerequisites

Before running the Maze Solver code, ensure that the following prerequisites are met:

    Python: Install Python on your machine. You can download Python from the official website at python.org and follow the installation instructions.

    Required Libraries: Make sure the necessary libraries are installed. The code utilizes the turtle library for graphical visualization. If not installed, use the following command in your command prompt or terminal:
    
```
    bash

    pip install PythonTurtle
    
```

## Running the Code

Follow these steps to run the Maze Solver code:

    **Download the code:** Download the code files for the Maze Solver.

    **Import the Required Modules:** Import the necessary modules in your main code file. Add the following import statements at the beginning of your code:

    python
```
import turtle

import maze_gen_merv

from time import sleep
```

**Use the Functions:** The code provides various functions for different purposes. Call the required functions in your main code based on your specific needs. For example, to run the Policy Iteration algorithm on a maze, use:

python
```
main2(test_maze, test_mdp)
```
**Replace** test_maze and test_mdp with your actual maze and Markov Decision Process (MDP) data.

**Run the Code:** use the editor

    Visualize the Maze Solver: Once the code is running, a turtle graphics window will display the maze-solving process. Observe the turtle's movement as it solves the maze based on the chosen algorithm.

## Additional Notes

    Adjusting the Maze and MDP Data: Customize the maze and MDP data by modifying the variables test_maze and test_mdp within your code.


If you have any questions or need assistance, feel free to reach out. Enjoy learning MDP's!
![image](https://github.com/salmazekri/Maze-Generator-using-MDP/assets/76392907/4efbcc4a-91ad-4835-90d2-633a9277506b)
![image](https://github.com/salmazekri/Maze-Generator-using-MDP/assets/76392907/ac4225fe-2797-424f-b230-1c9ca581bd22)
