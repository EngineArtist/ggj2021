from map import Map

class levels:
    # When creating the levels class, presumably we start at the first level
    def __init__(self):
        self.current_level = 0
        # Level 1
        level1 = Map(3, 8, 4) # target 3, 8 x-width, 4 y-height
        level1actives = [
            [ False, False, False, False],
            [ False, False, False, True],
            [ False, False, False, True],
            [ False, False, True, True],
            [ False, False, True, True],
            [ False, True, True, True],
            [ False, True, True, True],
            [ True, True, True, True]
        ]
        level1colours = [
            [ False, False, False, False],
            [ False, False, False, False],
            [ False, False, False, False],
            [ False, False, False, False],
            [ False, False, False, False],
            [ False, False, False, False],
            [ False, False, False, False],
            [ False, False, False, False]
        ]
        level1.mapify(level1actives, level1colours)
        # Level 2
        level2 = Map(5, 10, 5) # target 5, 10 x-width, 5 y-height
        level2actives = [
            [ False, False, False, False, False],
            [ False, False, False, False, True],
            [ False, False, False, False, True],
            [ False, False, False, True, False],
            [ False, False, False, True, False],
            [ False, False, True, True, False],
            [ False, True, True, True, True],
            [ True, True, True, True, True],
            [ False, True, False, False, False],
            [ True, False, False, False, False],
        ]
        level2colours = [
            [ False, False, False, False, False],
            [ False, False, False, False, False],
            [ False, False, False, False, False],
            [ False, False, False, False, False],
            [ False, False, False, False, False],
            [ False, False, False, False, False],
            [ False, False, False, False, False],
            [ False, True, False, False, False],
            [ False, False, False, False, False],
            [ False, False, False, False, False]
        ]
        level2.mapify(level2actives, level2colours)
        
        self.levellist = [level1, level2]
        
    # Get current level
    def getCurrentLevel(self):
        return self.levellist[self.current_level]

    # Get definition for the next level and progress level indicator by one
    def getNextLevel(self):
        if(self.current_level == len(self.levellist)-1):
            self.current_level = 0
        else:
            self.current_level = self.current_level + 1
        return self.levellist[self.current_level]

