class Position:
    '''The Positon class:
    --> Holds the x and the y coordinates for that position
    --> holds the isTraversable boolean for traversable functionality.'''
    def __init__(self, x=0, y=0, isTraversable=True):
        self.x = x
        self.y = y
        self.isTraversable = isTraversable

class Map:
    '''The Map class:
    --> Initializes the map which is a 2D array of Position objects
    --> rows and cols are variables to specify dimensions of the map.'''
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        map_obj = Position()
        map_arr = [map_obj*self.cols]*self.rows

class Rover:
    '''The Rover class:
    --> Contains the battery_life variable
    --> also contains traverse method to return the number of steps to get to end position'''
    current_pos = Position()
    def __init__(self, battery_life = 100):
        self.battery_life = battery_life
    
    def traverse(self, starting_pos, ending_pos):
        
        steps = 0
        #if either the starting position or the ending position is not traversable then 
        #automatically the rover returns -1 since it wont be able to go to these essential blocks.
        if not(starting_pos.isTraversable or ending_pos.isTraversable):
            return -1
        new_pos = Position()
        new_pos = starting_pos
        
        while not(new_pos==ending_pos):
            if new_pos.x<ending_pos.x: #either the rover moves to the right or the left depending on whether that block is traversable
                if Position(new_pos.x+1, new_pos.y).isTraversable:
                    new_pos.x+=1
                    steps+=1
                #if the right block is not traversable we check for moving up or down
                elif new_pos.y<ending_pos.y and Position(new_pos.x, new_pos.y+1).isTraversable:
                    new_pos.y+=1
                    steps+=1
                else:
                    new_pos.y-=1
                    steps+=1
                    
            else:
                if Position(new_pos.x-1, new_pos.y).isTraversable:
                    new_pos.x-=1
                    steps+=1
                elif new_pos.y<ending_pos.y and Position(new_pos.x, new_pos.y+1).isTraversable:
                    new_pos.y+=1
                    steps+=1
                else:
                    new_pos.y-=1
                    steps+=1

        self.battery_life-=steps
        return steps
  
