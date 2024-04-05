import turtle
import maze_gen_merv
import re
from maze_gen_merv import main

from time import sleep
bg_col = '#152238'
win = turtle.Screen()
win.bgcolor(bg_col)
win.title("Poliicy Iteration Maze Solver")
win.setup(700,700)

#Create Pen
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("light blue")
        self.shape("square")
        self.penup()
        self.speed(0)
        self.ht()

p = Pen()

def initialize_walls(maze):
    p.shape("square")
    p.ht()
    win.tracer(0, 0)
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            wall = maze[i][j]
            screen_x = -700/2 +30 +(j * 24)
            screen_y = 200- (i * 24)
            if wall == "w":
                p.goto(screen_x, screen_y)
                p.stamp()
    
    win.update()

def gui_policy_iteration(policy, iterations, goals):
    
    # p.shape("classic")
    # p.ht()
    win.tracer(0,0)
    for i in range(len(policy)):
        for j in range(len(policy[i])):
            arrow = policy[i][j]
            screen_x = -700/2 +30 +(j * 24)
            screen_y = 200- (i * 24)
            
            if (i,j) in goals:
                # print("HHHHEEEERRRREEE")
                p.goto(screen_x, screen_y)
                p.color(bg_col)
                p.shape('square')
                p.stamp()
                p.color('coral')
                p.shape('turtle')
                p.setheading(0)
                p.stamp()

            else:
                if arrow != 'w':
                    p.goto(screen_x, screen_y)
                    p.color(bg_col)
                    p.shape('square')
                    p.stamp()
                    p.color('pink')
                    p.shape("classic")
                
                
                if arrow == 'up':
                    p.setheading(90)
                    p.stamp()
                
                if arrow == 'down':
                    p.setheading(270)
                    p.stamp()
                
                if arrow == 'left':
                    p.setheading(180)
                    p.stamp()
                
                if arrow == 'right':
                    p.setheading(0)
                    p.stamp()        
    win.update()
def print_iteration_cost(iteration, cost_matrix):
    print(f"Iteration: {iteration}")
    for row in cost_matrix:
        print(' '.join([f'{cost:.2f}' for cost in row]))
    print()

def print_policy(policy):
    policy_str = '\n'.join([''.join(row) for row in policy])
    policy_str = re.sub('up', '↑', policy_str)
    policy_str = re.sub('down', '↓', policy_str)
    policy_str = re.sub('right', '→', policy_str)
    policy_str = re.sub('left', '←', policy_str)

    print(policy_str)

def evaluate_policy(grid, policy, gamma, goals,iterations):
    is_value_changed = True
    iteration = 0
    while is_value_changed:
        is_value_changed = False
        cost_matrix = [[0.0] * len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != 'w':
                    neighbor = getattr(grid[i][j], policy[i][j])
                    v = grid[i][j].reward + gamma * grid[neighbor[0]][neighbor[1]].value
                    if v != grid[i][j].value:
                        is_value_changed = True
                        grid[i][j].value = v
        #             cost_matrix[i][j] = v
        # print_iteration_cost(iterations, cost_matrix)
        iteration += 1
        print("iteration ", iterations, "values: ")
        values = [[round(state.value, 2)  if state != 'w' else '-' for state in row] for row in grid]
        c =0
        for row_values in values:
            print("row", c, ": ", row_values)
            c+=1
        print("\n policy")
        print_policy(policy)
        
        
        


def improve_policy(grid, policy, actions, gamma):
    is_policy_changed = False
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != 'w':
                action_values = {
                    a: grid[getattr(grid[i][j], a)[0]][getattr(grid[i][j], a)[1]].value
                    for a in actions
                }
                best_action = max(action_values, key=action_values.get)
                if best_action != policy[i][j]:
                    is_policy_changed = True
                    policy[i][j] = best_action
            else:
                policy[i][j] = 'w'
    # print_policy(policy)
        
    return is_policy_changed

def policyiteration(grid, gamma):
    initialize_walls(grid)
    policy = [['up' for i in range(len(grid[0]))] for j in range(len(grid))]
    actions = ['up', 'down', 'left', 'right']

 

    iterations = 0
    goals = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'w':
                policy[i][j] = 'w'
            elif grid[i][j].reward != -1:
                goals.append((i, j))

    gui_policy_iteration(policy, iterations, goals)
    sleep(1)

    while True:
        evaluate_policy(grid, policy, gamma, goals,iterations)
        is_policy_changed = improve_policy(grid, policy, actions, gamma)
        iterations += 1
        gui_policy_iteration(policy, iterations, goals)
        if not is_policy_changed:
            break


    print(f'Policy iteration completed in {iterations} iterations.')
    cost_mat = []

    print("\n COST")
    for i in range(len(policy)):
        row = []
        for j in range(len(policy[i])):
            if policy[i][j] == 'w':
                row.append(None)
            else:
                row.append(calculate_cost(policy, i, j, 0))
        cost_mat.append(row)
    for row in cost_mat:
        print(row)


    
    
    turtle.done()
    return policy

def calculate_cost(policy, i, j, cost):
    #print("here main")
    
    while(True):
        if i==len(policy) or j == len(policy):
            break
        if policy[i][j] == 'w':
            #print("heree")
            break
        elif policy[i][j] == 'up':
            #print("here up")
            cost+=1
            i = i-1
            # print(cost)
        elif policy[i][j] == 'down':
            #print("here down")
            cost+=1
            i = i+1
            # print(cost)
        elif policy[i][j] == 'left':
            #print("here left")
            cost+=1
            j= j+ 1
            # print(cost)
        elif policy[i][j] == 'right':
            #print("here right")
            cost+=1
            j = j-1
            # print(cost)
    return cost
    # elif policy[i][j] == 'down':
    #     cost+=1
    #     calculate_cost(policy, i+1, j, cost)
    # elif policy[i][j] == 'left':
    #     cost+=1
    #     calculate_cost(policy, i, j+1, cost)
    # elif policy[i][j] == 'right':
    #     cost+=1
    #     calculate_cost(policy, i, j-1, cost)
    


def main2(test_maze, test_mdp):
    #test_maze, test_mdp = maze_gen_merv.main()
    test_policy = policyiteration(test_mdp, 0.9)



if __name__ == '__main__':
    test_maze, test_mdp = maze_gen_merv.main(10, 10)
    test_policy = policyiteration(test_mdp, 0.9)
