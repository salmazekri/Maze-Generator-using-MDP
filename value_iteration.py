from maze_gen_merv import main
import re
import turtle
import gradienthelper

gradient = gradienthelper.linear_gradient('#ffffff', '#ff0000',40)
col_list = range(0, 200, 5)
gradient_dict = {col_list[i]: gradient.get('hex')[i] for i in range(len(gradient.get('hex')))}

bg_col = 'white'
win = turtle.Screen()
win.bgcolor(bg_col)
win.title("Poliicy Iteration Maze Solver")
win.setup(700,700)

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("square")
        self.color("black")
        self.speed(200)
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

    
def animate_values(grid, iterations):
    
    win.tracer(0, 0)
    for i in range(len(grid)):
        x = len(grid[i])+len(grid[i])/2
        for j in range(len(grid[i])):
            
            character = grid[i][j]
            
            screen_x = -700/2 +30 +(j * 24)
            screen_y = 200- (i * 24)
            
            p.goto(screen_x, screen_y)
            
            if character == 'w':
                p.color('#152238')
                p.stamp()
            
            else:
                p.color(gradient_dict.get(int(round(character.value/x)*5), 'red'))
                p.stamp()
                
        
    win.update()

def value_iteration(maze, gamma):
    initialize_walls(maze)
    policy = [['no_policy' for _ in range(len(maze[0]))] for _ in range(len(maze))]
    actions = ['up', 'down', 'right', 'left']

    is_value_changed = True
    iterations = 0
    while is_value_changed:
        is_value_changed = False

        for i in range(len(maze) ):
            for j in range(len(maze[i]) ):
                if maze[i][j] != 'w':
                    q = []
                    for a in actions:
                            neighbor = getattr(maze[i][j], a)
                            q.append(maze[i][j].reward + gamma * maze[neighbor[0]][neighbor[1]].value)
                    v = max(q)
                    #values[i][j].append(v)

                    if (v - maze[i][j].value > 0):
                        is_value_changed = True
                        maze[i][j].value = v

        iterations += 1
        print("iteration ", iterations, "values: ")
        values = [[round(state.value, 2)  if state != 'w' else '-' for state in row] for row in maze]
        c =0
        for row_values in values:
            print("row", c, ": ", row_values)
            c+=1
        print("\n")
    animate_values(maze, iterations)
    
    
    turtle.done()
                            
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] != 'w':
                # Dictionary comprehension to get value associated with each action
                action_values = {
                    a: maze[getattr(maze[i][j], a)[0]][getattr(maze[i][j], a)[1]].value
                    for a in actions
                }
                policy[i][j] = max(action_values, key=action_values.get)
            else:
                policy[i][j] = 'w'

    return(policy)

def main2(test_maze, grid):
    #test_maze, grid = main()
    test_policy = value_iteration(grid, .9)

    
if __name__ == '__main__':
    test_maze, grid = main(20,20)
    test_policy = value_iteration(grid, .9)
    # test_policy_str = prettify_policy(test_policy)

    #print(test_maze)
    #print(test_policy_str)
                    