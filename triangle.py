# Single triangle instance in Trilemma
class Triangle:
    def __init__(self):
        # Coloured triangle; false is white, true is black (="blocked")
        self.coloured = False
        # Active means tile is part of map, this is due to rectangular map containing idle map triangles not part of puzzle
        self.active = False

    # Flip colour status        
    def flip(self):
        self.coloured = not self.coloured

    # Setters
    def setActive(self):
        self.active = True

    def setInactive(self):
        self.active = False

    def setActiveState(self, state):
        self.active = state
        
    def setColoured(self):
        self.coloured = True

    def setUncoloured(self):
        self.coloured = False

    def setColouredState(self, state):
        self.coloured = state
        
    # Getters
    def getActive(self):
        return self.active

    def getColoured(self):
        return self.coloured
    
