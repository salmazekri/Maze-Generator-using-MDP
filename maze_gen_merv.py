#maze generator
import random
global maze
global walls
import time
from mdpstate import MDPState
from copy import deepcopy

EMPTY = ' '
WALL = 'w'
PATH = 'p'

def maze_to_mdp(maze, exit,entrance, w , h):
    maze_mdp= deepcopy(maze)
    # maze_mdp[exit[0]][exit[1]] = WALL
    # maze_mdp[entrance[0]][entrance[1]] = WALL
    for i in range( h):
        for j in range(w):

            if(i == exit[0] and j == exit[1]):
                continue
            if(i == entrance[0] and j == entrance[1]):
                continue
    
            if maze[i][j] == WALL:
                maze_mdp[i][j] = WALL
                continue
                    
            if maze[i-1][j] == WALL:
                up = (i, j)
            else:
                up = (i-1, j)
                    
            if maze[i+1][j] == WALL:
                down = (i, j)
            else:
                down = (i+1, j)
                    
            if maze[i][j+1] == WALL:
                right = (i, j)
            else:
                right = (i, j+1)
                    
            if maze[i][j-1] == WALL:
                left = (i, j)
            else:
                left = (i, j-1)
                    
            maze_mdp[i][j] = MDPState(up, down, left, right)
        
    
    i = exit[0]
    j = exit[1]
    
    if(i == h- 1):
        maze_mdp[i][j] = MDPState((i-1, j), (i, j), (i, j),(i, j) )
    else:
        maze_mdp[i][j] = MDPState((i, j), (i, j), (i, j-1),(i, j) )
    maze_mdp[i][j].reward = 100

    i= entrance[0]
    j = entrance[1]
    if(i == 0):
        maze_mdp[i][j] = MDPState((i, j), (i+1, j), (i, j),(i, j) )
    else:
        maze_mdp[i][j] = MDPState((i, j), (i, j), (i, j),(i, j+1) )
    


                
    return(maze_mdp)

def count_paths(selected_wall, maze):
	possible_paths = 0
	if (maze[selected_wall[0]-1][selected_wall[1]] == PATH):
		possible_paths += 1
	if (maze[selected_wall[0]+1][selected_wall[1]] == PATH):
		possible_paths += 1
	if (maze[selected_wall[0]][selected_wall[1]-1] == PATH):
		possible_paths +=1
	if (maze[selected_wall[0]][selected_wall[1]+1] == PATH):
		possible_paths += 1

	return possible_paths

def remove_wall(selected_wall, walls):
     for wall in walls:
        if (wall == selected_wall):
            walls.remove(wall)
     
def modify_upper(selected_wall,walls):
    if (selected_wall[0] != 0):
        #if upper pos is not a path, make it a wall
        if (maze[selected_wall[0]-1][selected_wall[1]] != PATH):
            maze[selected_wall[0]-1][selected_wall[1]] = WALL
        # if is not already in walls array add it
        if ([selected_wall[0]-1, selected_wall[1]] not in walls):
             walls.append([selected_wall[0]-1, selected_wall[1]])

def modify_left(selected_wall, walls):
    if(selected_wall[0]!= 0 ):
        if(maze[selected_wall[0]][selected_wall[1]-1] != PATH):
            maze[selected_wall[0]][selected_wall[1]-1] = WALL
        if [selected_wall[0], selected_wall[1]-1] not in walls:
            walls.append([selected_wall[0], selected_wall[1]-1])

def modify_right(selected_wall, walls, width):
    if(selected_wall[0]!= width -1):
        if(maze[selected_wall[0]][selected_wall[1]+1] != PATH):
            maze[selected_wall[0]][selected_wall[1]+1] = WALL
        if [selected_wall[0], selected_wall[1]+1] not in walls:
            walls.append([selected_wall[0], selected_wall[1]+1])

def modify_bottom(selected_wall, walls, height):
    if (selected_wall[1] != height-1):
        #if bottom pos is not a path, make it a wall
        if (maze[selected_wall[0]+1][selected_wall[1]] != PATH):
            maze[selected_wall[0]+1][selected_wall[1]] = WALL
        # if is not already in walls array add it
        if ([selected_wall[0]+1, selected_wall[1]] not in walls):
            walls.append([selected_wall[0]+1, selected_wall[1]])

             

def init_maze(h, w):
    #width = w
   # height = h
    

    maze= []
    for i in range(h):
        row = []
        for j in range(w):
            row.append(EMPTY)
        maze.append(row)
    return maze


def main(h,w):
    global maze
    maze = init_maze(h,w)
    random_seed = int(time.time())
    random.seed(random_seed)
    

    #random start point for maze
    start_y = int(random.random()*h)
    start_x = int(random.random()*w)

    if start_y == 0:
        start_y += 1
    elif start_y == h-1:
        start_y -=1
    if start_x == 0:
        start_x +=1
    elif start_x == w - 1:
        start_x -=1
    
    #first step in path
    maze[start_y][start_x] = PATH

    #start adding walls around starting point -- we will remove some later
    walls = []
    walls.append([start_y - 1, start_x])
    walls.append([start_y, start_x - 1])
    walls.append([start_y, start_x + 1])
    walls.append([start_y + 1, start_x])

    maze[start_y - 1][ start_x] = WALL
    maze[start_y][start_x - 1] = WALL
    maze[start_y][start_x + 1] = WALL
    maze[start_y + 1][start_x] = WALL

    while(walls):
        wall_count = len(walls)
        selected_wall = walls[int(random.random()*wall_count)-1]
        remove_wall(selected_wall, walls)
        #if its not a right wall -- 
        if (selected_wall[1] != w -1):
            if (maze[selected_wall[0]][selected_wall[1]-1] == PATH and maze[selected_wall[0]][selected_wall[1]+1] == EMPTY):
                path_count = count_paths(selected_wall, maze)
                if (path_count < 2):
                    maze[selected_wall[0]][selected_wall[1]] = PATH
                    modify_right(selected_wall, walls, w)
                    modify_bottom(selected_wall, walls, h)
                    modify_upper(selected_wall, walls)
                continue

        #if its not a left wall -- 
        if (selected_wall[1] != 0):
            if (maze[selected_wall[0]][selected_wall[1]-1] == EMPTY and maze[selected_wall[0]][selected_wall[1]+1] == PATH):
                path_count = count_paths(selected_wall, maze)
                if (path_count < 2):
                    maze[selected_wall[0]][selected_wall[1]] = PATH
                    modify_left(selected_wall, walls)
                    modify_bottom(selected_wall, walls, h)
                    modify_upper(selected_wall, walls)
                continue
        
        #if its not a bottom wall -- 
        if (selected_wall[0] != h -1):
            if (maze[selected_wall[0]-1][selected_wall[1]] == PATH and maze[selected_wall[0]+1][selected_wall[1]] == EMPTY):
                path_count = count_paths(selected_wall, maze)
                if (path_count < 2):
                    maze[selected_wall[0]][selected_wall[1]] = PATH
                    modify_right(selected_wall, walls, w)
                    modify_bottom(selected_wall, walls, h)
                    modify_left(selected_wall, walls)
                continue
        
        #if its not a upper wall -- 
        if (selected_wall[0] != 0):
            if (maze[selected_wall[0]-1][selected_wall[1]] == EMPTY and maze[selected_wall[0]+1][selected_wall[1]] == PATH):
                path_count = count_paths(selected_wall, maze)
                if (path_count < 2):
                    maze[selected_wall[0]][selected_wall[1]] = PATH
                    modify_right(selected_wall, walls, w)
                    modify_upper(selected_wall, walls)
                    modify_left(selected_wall, walls)


    random_exit = random.randint(0, 1)
    random_entrance = random.randint(0, 1)

    if random_entrance == 1: #entrance is from up
        for i in range(w):
            if maze[1][i] == PATH:
                #maze[0][i] = PATH
                entrance = [0,i]
                break

    else:
        for i in range(h):
            if maze[i][1] == PATH:
                #maze[i][0] = PATH
                entrance = [i, 0]
                
                break
    
    if random_exit == 1: #exit is from bottom
        for i in range(w-1, 0, -1):
            if maze[h-2][i] == PATH:
                maze[h-1][i] = PATH
                exit = [h-1, i]
                print(exit)
                break
    else:
        for i in range(h-1, 0, -1):
            if maze[i][w-2] == PATH:
                maze[i][w-1] = PATH
                exit = [i, w-1]
                print(exit)
                break

    for i in range(0, h):
        for j in range(0, w):
            if (maze[i][j] == EMPTY):
                maze[i][j] = WALL

    mdp = maze_to_mdp(maze, exit,entrance, w, h)
    
    return maze, mdp

#main(10,10)
#print(main(3,3))

        

                
    

                    






