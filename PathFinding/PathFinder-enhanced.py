import math

# Generate the labyrinth
print ("Generating labyrinth")
positions = [
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 1, 1, 1, 0, 0, 1, 0, 1],
    [0, 0, 1, 0, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 0, 1, 0, 0, 1, 0, 1],
    [0, 0, 1, 1, 1, 1, 0, 1, 0, 1],
    [0, 0, 1, 1, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
]
print ("Done")

# Print the labyrinth
print ()
print ("Printing labyrinth")
print ()

def printLabyrinth ():
    for x in positions:
        row = ""
        for y in x:
            row += str(y)
        print (row)
printLabyrinth()

#
# Enhanced Path Finder - based on A* algorithm
#
print ()
print ("Starting analysis of the labyrinth")
endFound = False

pos = None
lastPos = {}
init = None
end = None
options = []
analyzed = []

gscore = {"default" : 9999999}
fscore = {"default" : 9999999}

# Function that will calculate the fscore based on the module of the position to the goal.
def calculateCost (ptt, goal):
    return math.fabs( math.sqrt( math.pow(goal[0]-ptt[0], 2) + math.pow(goal[1]-ptt[1], 2) ) )
# Function that will reconstruct the path once arrived to the exit
def findPath (lp, p):
    total_path = [p,]
    while str(p) in lp:
        p = lp[str(p)]
        total_path.append(p)
    for x in total_path:
        positions[x[0]][x[1]] = 2
    moves = len(total_path)
    printLabyrinth()
    print ("---")
    print ("Exit found successfully in " + str(moves) + " moves.") 
            
# Starts finding the initial position that must be at the first file and the end position
for x in positions[0]:
    if (x == 1):
        init = [0, positions[0].index(x)]
        options.append(init)
        pos = init

        for x in positions[len(positions)-1]:
            if (x == 1):
                end = [len(positions)-1, positions[len(positions)-1].index(x)]                                      
        if end == None:
            print ("Error: no end found.")
        
        gscore[str(init)] = 0
        fscore[str(init)] = calculateCost (init, end)
        
        print ("Start position: " + str(pos) + "\tEnd position: " + str(end))
        print ()
        
if pos == None:
    print ("Error: no initial position found.")

# Application of the A* algorithm
while len(options) > 0:
    pos = None
    # Looks for the option with better fscore
    for x in options:
        if pos == None:
            pos = x
        else:
            if fscore[str(x)] < fscore[str(pos)]:
                pos = x
                
    if pos == end:
        findPath(lastPos, pos)
        break
    
    options.pop(options.index(pos))
    analyzed.append(pos)

    # Look for the neighbors
    adjacent = []
    try:
        if positions[pos[0]+1][pos[1]] == 1:
            adjacent.append([pos[0]+1,pos[1]])
    except:
        pass
    try:
        if positions[pos[0]][pos[1]+1] == 1:
            adjacent.append([pos[0],pos[1]+1])
    except:
        pass
    try:
        if positions[pos[0]][pos[1]-1] == 1:
            adjacent.append([pos[0],pos[1]-1])
    except:
        pass
    try:
        if positions[pos[0]-1][pos[1]] == 1:
            adjacent.append([pos[0]-1,pos[1]])
    except:
        pass
    
    # Analysis of the neighbors
    for opt in adjacent:
        if opt in analyzed:
            continue
        if opt not in options:
            options.append(opt)

        potential_gscore = gscore[str(pos)] + 1
##        if potential_gscore >= gscore[str(opt)]:
##            continue
        lastPos[str(opt)] = pos
        gscore[str(opt)] = potential_gscore
        fscore[str(opt)] = gscore[str(opt)] + calculateCost(opt, end)
        
