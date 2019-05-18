from copy import deepcopy
import numpy as np
import random

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

ACTIONS = [UP, DOWN, LEFT, RIGHT]

DANGER = "d"
AGENT = "A"
COINS = "c"
EMPTY = "-"
TREE = "t"
END = "E"

class State:
    
    def __init__(self, map, agent_pos):
        self.map = map
        self.agent_pos = agent_pos
        
    def __eq__(self, other):
        return isinstance(other, State) and self.map == other.map and self.agent_pos == other.agent_pos
    
    def __hash__(self):
        return hash(str(self.map) + str(self.agent_pos))
    
    def __str__(self):
        return f"State(map={self.map}, agent_pos={self.agent_pos})"

# Takes the current state with an action and returns new state		
def move(state, action):
    
    def new_agent_pos(state, action):
        p = deepcopy(state.agent_pos)
        if action == UP:
            p[0] = max(0, p[0] - 1)
        elif action == DOWN:
            p[0] = min(len(state.map) - 1, p[0] + 1)
        elif action == LEFT:
            p[1] = max(0, p[1] - 1)
        elif action == RIGHT:
            p[1] = min(len(state.map[0]) - 1, p[1] + 1)
        else:
            raise ValueError(f"Unknown action {action}")
        return p
            
    p = new_agent_pos(state, action)
    map_item = state.map[p[0]][p[1]]
    
    new_map = deepcopy(state.map)
    
    if map_item == DANGER:
        reward = -100
        game_over = True
        new_map[p[0]][p[1]] += AGENT
        print("YOU ARE IN DANGER!!")
    elif map_item == COINS:
        reward = 50
        game_over = False
        old = state.agent_pos
        new_map[old[0]][old[1]] = EMPTY
        new_map[p[0]][p[1]] = AGENT
    elif map_item == EMPTY:
        reward = 0
        game_over = False
        old = state.agent_pos
        new_map[old[0]][old[1]] = EMPTY
        new_map[p[0]][p[1]] = AGENT
    elif map_item == TREE:
        reward = -10
        game_over = False
    elif map_item == AGENT:
        reward = -1
        game_over = False
    elif map_item == END:
        reward = 500
        is_done = True
        new_map[p[0]][p[1]] += AGENT
        print("You reached end of the map!!")
    else:
        raise ValueError(f"Unknown map item")
    
    return State(map=new_map, agent_pos=p), reward, game_over
