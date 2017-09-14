# Generate the labyrinth
print ("Generating labyrinth")
positions = [
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
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
# 1st Recursive PathFinding section
#
print ()
print ("Starting simple path finding")
endFound = False
moves = 0

startPosition = None

# Recursive function
def recursiveFinding (pos):
    global moves
    moves+=1
    positions[pos[0]][pos[1]] = 2
    print (str(pos))
    if pos[0] == len(positions)-1:
        return True
    else:
        if positions[pos[0]+1][pos[1]] == 1:
            return recursiveFinding ([pos[0]+1,pos[1]])
        if positions[pos[0]][pos[1]-1] == 1:
            return recursiveFinding ([pos[0],pos[1]-1])
        if positions[pos[0]][pos[1]+1] == 1:
            return recursiveFinding ([pos[0],pos[1]+1])
        if positions[pos[0]-1][pos[1]] == 1:
            return recursiveFinding ([pos[0]-1,pos[1]])
            
while endFound == False:
    # Starts finding the initial position
    if startPosition == None:
        for x in positions[0]:
            if (x == 1):
                startPosition = [0, positions[0].index(x)]
                print ("Start position: " + str(startPosition))
                continue
        if startPosition == None:
            print ("Error: no initial position found.")
            break
        
    # Once found, the algorithm continues to normal
    else:
        print ()
        print ("Printing movements: ")
        print ()
        endFound = recursiveFinding (startPosition)
        if (endFound):
            print ()
            print ("Exit found in " + str(moves) + " moves.")
            print ()
            printLabyrinth()
        else:
            print ()
            print ("Exit not found. " + str(moves) + " moves done.")
            print ()
            printLabyrinth()
            break
            
