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
print(testmap.mapASCII())
#Map, with [ ]  being triangles, - being inactive, X coloured (active) and 0 as uncoloured (active) statuses
# -   -   -   -  
#  -   -   -  [0] 
#   -   -   -  [0] 
#    -   -  [0] [0] 
#     -   -  [0] [0] 
#      -  [0] [0] [0] 
#       -  [0] [0] [0] 
#       [0] [0] [0] [0]
#>>> testmap.validate()
#False
#>>> print(testmap)
#Trilemma map of size [8,4]
#with target count of: 3
#with current coloured count of: 1
#>>> testmap.validate()
#False
#>>> testmap.setColourStateAt(6,3,True)
#True
#>>> testmap.setColourStateAt(7,3,True)
#True
#>>> testmap.validate()
#True
#>>> print(testmap.mapASCII())
#Map, with [ ]  being triangles, - being inactive, X coloured (active) and 0 as uncoloured (active) statuses
# -   -   -   -  
#  -   -   -  [0] 
#   -   -   -  [0] 
#    -   -  [0] [0] 
#     -   -  [0] [0] 
#      -  [0] [0] [X] 
#       -  [0] [0] [X] 
#       [0] [0] [0] [X]
