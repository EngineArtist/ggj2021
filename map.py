from triangle import Triangle

# Main map in Trilemma depicting triangle logic and game state
class Map:
    # Constructors
    def __init__(self, target, xsize, ysize):
        self.linecount = 0
        self.flipcount = 0
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
        for i in range(len(startActives)):
            for j in range(len(startActives[i])):
                if(startActives[i][j]):
                    self.map[i][j].setActive()                
        # startColours is a boolean 2-dim array indicating starting colour for each map triangle
        for i in range(len(startColours)):
            for j in range(len(startColours[i])):
                if(startColours[i][j]):
                    self.map[i][j].setColoured()
                    
    # Player line-operator
    # Two 'line' type syntax can be used;
    # - Integers define as 0 as a horizontal line at given y-coord, 1 as '/' shaped diagonal line at given x-coord, 2 as '\' shaped diagonal line at given x-coord
    # - '_' symbol is a horizontal line, '/' is diagonal in corresponding direction, '\' the other diagonal
    # Notice that a single coordinate uniquely defines location when coupled with direction
    # Direction is a boolean indicating which way the arrow points (True is upwards or rightwards)
    # TODO: The coordinates still need double-checking, to make sure they work right...
    def line(self, line, coord, direction):
        if(line == 0 or line == '-'):
            self.linecount = self.linecount + 1
            if(direction):
                for j in range(0, coord):
                    for i in range(self.xsize):
                        self.map[i][j].flip()
                        self.flipcount = self.flipcount + 1
            else:                
                for j in range(coord, self.ysize):
                    for i in range(self.xsize):
                        self.map[i][j].flip()
                        self.flipcount = self.flipcount + 1
        elif(line == 1 or line == '/'):
            coord = coord * 2
            self.linecount = self.linecount + 1
            if(direction):
                for j in range(self.ysize):
                    for i in range(self.xsize):
                        if((i >= coord - j*2 - 1) and i<len(self.map) and j<len(self.map[0])):
                            self.map[i][j].flip()
                            self.flipcount = self.flipcount + 1
            else:
                for j in range(self.ysize):
                    for i in range(self.xsize) :
                        if((i < coord - j*2 - 1) and i<len(self.map) and j<len(self.map[0])):
                            self.map[i][j].flip()
                            self.flipcount = self.flipcount + 1
        elif(line == 2 or line == '\\'):
            coord = coord * 2            
            self.linecount = self.linecount + 1
            if(direction):
                for i in range(coord, self.xsize):
                    for j in range(self.ysize) :
                        if(i<len(self.map) and j<len(self.map[0])):
                            self.map[i][j].flip()
                            self.flipcount = self.flipcount + 1                        
            else:                
                for i in range(0,coord):
                    for j in range(self.ysize):
                        if(i<len(self.map) and j<len(self.map[0])):
                            self.map[i][j].flip()
                            self.flipcount = self.flipcount + 1
        

    # Test if map has been solved successfully; true if so, false if not
    def validate(self):
        return self.target == self.countColoured()

    # Get current map[xsize][ysize] of Triangle-objects
    def getMap(self):
        return self.map

    # Set active state at given coordinates for triangle
    def setActiveStateAt(self, x, y, active):
        if(x<self.xsize and y<self.ysize and x>=0 and y>=0):
            self.map[x][y].setActiveState(active)
            return True
        else:
            return False

    # Set coloured state at given coordinates for triangle
    def setColourStateAt(self, x, y, coloured):
        if(x<self.xsize and y<self.ysize and x>=0 and y>=0):
            self.map[x][y].setColouredState(coloured)
            return True
        else:
            return False

    # Reset colours to blank (False) status
    def reset(self):
        for i in range(self.xsize):
            for j in range(self.ysize):
                self.map[i][j].setUncoloured()

    # Get target count
    def getTarget(self):
        return self.target

    # Get line operation count
    def getLinecount(self):
        return self.linecount

    ## INTERNAL USE

    # Populate triangle map with instances of Triangle-objects        
    def populate(self, xsize, ysize):
        self.map = [[Triangle() for j in range(ysize)] for i in range(xsize)]

    # Count the amount of coloured triangles in current map
    def countColoured(self):
        count = 0
        for i in range(self.xsize):
            for j in range(self.ysize):
                if(self.map[i][j].getActive() and not self.map[i][j].getColoured()):
                    count = count + 1
        return count                            
    
    # Flip triangle at target location
    def flipAt(self, x, y):
        if(x<self.xsize and y<self.ysize and x>=0 and y>=0):
            self.map[x][y].flip()
            return True
        else:
            return False

    # Print custom object output
    def __str__(self):
        return ("Trilemma map of size [" +
                str(self.xsize) + "," + str(self.ysize) +
                "]\nwith target count of: " + str(self.target) +
                "\nwith current coloured count of: " + str(self.countColoured()) +
                "\nwith " + str(self.linecount) + " line operations " +
                "\nand total " + str(self.flipcount) + " triangle flips so far")
    
    # Print map status as somewhat understandable text output
    def mapASCII(self):
        string = "Map, with [ ]  being triangles, - being inactive, X coloured (active) and 0 as uncoloured (active) statuses"
        for j in range(self.ysize):
            # Line change and add a bit of buffer to the left according to x coord
            string = string + "\n" + str(" " * j) 
            for i in range(self.xsize):
                if(self.map[i][j].getActive()):
                    if(self.map[i][j].getColoured()):
                        string = string + "[X] "
                    else:
                        string = string + "[0] "
                else:
                    string = string + " -  "            
        return string    
        
