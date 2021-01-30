# The pyramid example from first example game run
testmap = Map(3, 8, 4)
# Active the "pyramid" for gameplay
testmap.setActiveStateAt(7,0,True)
testmap.setActiveStateAt(5,1,True)
testmap.setActiveStateAt(6,1,True)
testmap.setActiveStateAt(7,1,True)
testmap.setActiveStateAt(3,2,True)
testmap.setActiveStateAt(4,2,True)
testmap.setActiveStateAt(5,2,True)
testmap.setActiveStateAt(6,2,True)
testmap.setActiveStateAt(7,2,True)
testmap.setActiveStateAt(1,3,True)
testmap.setActiveStateAt(2,3,True)
testmap.setActiveStateAt(3,3,True)
testmap.setActiveStateAt(4,3,True)
testmap.setActiveStateAt(5,3,True)
testmap.setActiveStateAt(6,3,True)
testmap.setActiveStateAt(7,3,True)
# See output
#print(testmap.mapASCII())
#>>> print(testmap.mapASCII())
#Map, with [ ]  being triangles, - being inactive, X coloured (active) and 0 as uncoloured (active) statuses
# -   -   -   -   -   -   -  [0] 
#  -   -   -   -   -  [0] [0] [0] 
#   -   -   -  [0] [0] [0] [0] [0] 
#    -  [0] [0] [0] [0] [0] [0] [0] 
#>>> print(testmap)
#Trilemma map of size [8,4]
#with target count of: 3
#with current coloured count of: 0
#with 0 line operations 
#and total 0 triangle flips so far
#>>> testmap.validate()
#False
## -> Map is not yet solved

#>>> testmap.setColourStateAt(5,3,True)
#True
#>>> testmap.setColourStateAt(6,3,True)
#True
#>>> testmap.setColourStateAt(7,3,True)
#True
#>>> print(testmap.mapASCII())
#Map, with [ ]  being triangles, - being inactive, X coloured (active) and 0 as uncoloured (active) statuses
# -   -   -   -   -   -   -  [0] 
#  -   -   -   -   -  [0] [0] [0] 
#   -   -   -  [0] [0] [0] [0] [0] 
#    -  [0] [0] [0] [0] [X] [X] [X] 
#>>> testmap.validate()
#True
## -> Fake solution by cheating

## Fix cheating
#>>> testmap.setColourStateAt(5,3,False)
#True
#>>> testmap.setColourStateAt(6,3,False)
#True
#>>> testmap.setColourStateAt(7,3,False)
#True

## Trying to solve using actual player operations
#>>> testmap.line(0, 2, True)
#>>> print(testmap.mapASCII())
#Map, with [ ]  being triangles, - being inactive, X coloured (active) and 0 as uncoloured (active) statuses
# -   -   -   -   -   -   -  [X] 
#  -   -   -   -   -  [X] [X] [X] 
#   -   -   -  [0] [0] [0] [0] [0] 
#    -  [0] [0] [0] [0] [0] [0] [0]
#>>> print(testmap)
#Trilemma map of size [8,4]
#with target count of: 3
#with current coloured count of: 4
#with 1 line operations 
#and total 16 triangle flips so far
#>>> testmap.validate()
#False
#>>> testmap.line(0,1,True)
#>>> print(testmap.mapASCII())
#Map, with [ ]  being triangles, - being inactive, X coloured (active) and 0 as uncoloured (active) statuses
# -   -   -   -   -   -   -  [0] 
#  -   -   -   -   -  [X] [X] [X] 
#   -   -   -  [0] [0] [0] [0] [0] 
#    -  [0] [0] [0] [0] [0] [0] [0] 
#>>> print(testmap)
#Trilemma map of size [8,4]
#with target count of: 3
#with current coloured count of: 3
#with 2 line operations 
#and total 24 triangle flips so far
#>>> testmap.validate()
#True

## The actual solution to this naive map can be obtained using just two line operations :)
# Faster way to generate maps?
moretest = Map(3, 8, 4)
testactives = [
    [ False, False, False, False],
    [ False, False, False, True],
    [ False, False, False, True],
    [ False, False, True, True],
    [ False, False, True, True],
    [ False, True, True, True],
    [ False, True, True, True],
    [ True, True, True, True]
]
testcolours = [
    [ False, False, False, False],
    [ False, False, False, False],
    [ False, False, False, False],
    [ False, False, False, False],
    [ False, False, False, False],
    [ False, False, False, False],
    [ False, False, False, False],
    [ False, False, False, False]
]
moretest.mapify(testactives, testcolours)
print(moretest.mapASCII())

#>>> print(moretest.mapASCII())
#Map, with [ ]  being triangles, - being inactive, X coloured (active) and 0 as uncoloured (active) statuses
# -   -   -   -   -   -   -  [0] 
#  -   -   -   -   -  [0] [0] [0] 
#   -   -   -  [0] [0] [0] [0] [0] 
#    -  [0] [0] [0] [0] [0] [0] [0]

    
# Do the solution similarly as in the picture
moretest.line("/", 7, False)
## TODO: Debug - it's missing corners which should be turned from [0] to [X]
#>>> print(moretest.mapASCII())
#Map, with [ ]  being triangles, - being inactive, X coloured (active) and 0 as uncoloured (active) statuses
# -   -   -   -   -   -   -  [X] 
#  -   -   -   -   -  [X] [0] [0] 
#   -   -   -  [X] [0] [0] [0] [0] 
#    -  [X] [0] [0] [0] [0] [0] [0]

moretest.line("-", 2, True)
moretest.line("\\", 4, True)

