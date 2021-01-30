# Main map in Trilemma depicting triangle logic and game state
class Map:
    # Constructors
    def __init__(self, target, xsize, ysize):
        self.target = target
        self.xsize = xsize
        self.ysize = ysize
        self.populate(xsize, ysize)

    ## EXTERNAL USE

    # Define level map with set active/colour status
    # startActives : boolean 2-dim list indicating which triangles ought to exist in level
    # startColours : boolean 2-dim list indicating starting colours (typically False for uncoloured)
    def mapify(self, startActives, startColours):
        # startActives is a boolean 2-dim array indicating if the triangle should be part of active game map
        for i in len(startActives):
            for j in len(startActives[i]):
                # TODO? Sanity checkers to see if dimensions match
                if(startActives[i,j]):
                    self.map[i,j].setActive()                
        # startColours is a boolean 2-dim array indicating starting colour for each map triangle
        for i in len(startColours):
            for j in len(startColours[i]):
                # TODO? Sanity checkers to see if dimensions match
                if(startColours[i,j]):
                    self.map[i,j].setColoured()
                    
    # Player line-operator
    # Two 'line' type syntax can be used;
    # - Integers define as 0 as a horizontal line at given coord, 1 as '/' shaped diagonal line, 2 as '\' shaped diagonal line
    # - '_' symbol is a horizontal line, '/' is diagonal in corresponding direction, '\' the other diagonal
    # Notice that a single coordinate uniquely defines location when coupled with direction
    # Direction is a boolean indicating which way the arrow points (True is upwards or rightwards)
    # TODO: The coordinates still need double-checking, to make sure they work right...
    def line(self, line, coord, direction):
        if(line == 0 | line == '_'):
            if(direction):
                for j in range(0, coord):
                    for i in range(xsize):
                        self.map[i,j].flip()
                        ## TODO: Send message to graphics device to draw animation for flip(s)?
            else:                
                for j in range(coord+1, ysize):
                    for i in range(xsize):
                        self.map[i,j].flip()
                        ## TODO: Send message to graphics device to draw animation for flip(s)?
        elif(line == 1 | line == '/'):
            if(direction):
                for j in range(ysize):
                    for i in range(xsize):
                        if(i > coord - j*2):
                            self.map[i,j].flip()                            
                            ## TODO: Send message to graphics device to draw animation for flip(s)?
            else:
                for j in range(ysize):
                    for i in range(xsize) :
                        if(i <= coord - j*2):
                            self.map[i,j].flip()                            
                            ## TODO: Send message to graphics device to draw animation for flip(s)?
        elif(line == 2 | line == '\\'):
            if(direction):
                for i in range(coord+1, xsize):
                    for j in range(ysize) :
                        self.map[i,j].flip()
                        ## TODO: Send message to graphics device to draw animation for flip(s)?
            else:                
                for i in range(0,coord):
                    for j in range(ysize):
                        self.map[i,j].flip()
                        ## TODO: Send message to graphics device to draw animation for flip(s)?
        

    # Test if map has been solved successfully; true if so, false if not
    def validate(self):
        if(self.target == self.countColoured()):
            return True
        else:
            return False

    # Get current map[xsize][ysize] of Triangle-objects
    def getMap(self):
        return self.map

    ## INTERNAL USE

    # Populate triangle map with instances of Triangle-objects        
    def populate(self, xsize, ysize):
        self.map = [[Triangle() for j in range(ysize)] for i in range(xsize)]

    # Count the amount of coloured triangles in current map
    def countColoured(self):
        count = 0
        for i in range(self.xsize):
            for j in range(self.ysize):
                if(self.map[i][j].getActive() & self.map[i][j].getColoured()):
                    count = count + 1
        return count                            
    
    # Flip triangle at target location
    def flipAt(self, x, y):
        if(x<self.xsize & y<self.ysize & x>=0 & y>=0):
            self.map[x][y].flip()

    # Print custom object output
    def __str__(self):
        return ("Trilemma map of size [" +
                str(self.xsize) + "," + str(self.ysize) +
                "]\nwith target count of: " + str(self.target) +
                "\nwith current coloured count of: " + str(self.countColoured()))
    
    
    
        
