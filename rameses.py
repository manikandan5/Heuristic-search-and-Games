"""Program to play Rameses"""

"""Program follows Iterative deepening algorithm and assigns MinMax values to each state while it traverses through the levels

The Evaluative function used in this program is 
    if(Diagonal or Row or Column) violates the game rules
        then we assign -1 to that state.
    if the next move results in a terminal state which results in the human player losing,
        we assign +1
    for all the other states,
        we assign 0

Sample input to the program is :
    python rameses.py 3 ..x..x... 3
    
    ramese.py   - program name
    
    3           - Dimensions of the grid N
    
    ..x..x...   - Initial State of the board
    
    3           - Time limit
    
Sample Output would be:
    .xx..x...   which represents the move of the player
    
    
"""
import time
import random
import sys


class stateclass:
    state=[]
    value=0
    children=[]

    def __init__(self,state,value,children):
        self.state=state
        self.value=value
        self.children=children

#Functions

"""Function to process input from the User and handle exceptions in Inputs"""
def get_input():
    #input=raw_input("Enter the input\t:")
    #input=input.split()
    if len(sys.argv)!=4:                   #Input should be of 3 parameters
        print "Invalid inputs"
        return "Error"
    else:
        N=int(sys.argv[1])
        if len(sys.argv[2])!=N*N:
            print "Invalid State"
            return "Error"
        #a="."*12+"x"+"."*3+"x"
        #input=["3","x.x.x....","5"]
        #input=["3","xxx.x...x","5"]
    return sys.argv

"""makeArray function changes the given string into a two dimensional array which
is easier to loop through and check for the terminal states and assign scores"""
def makeArray(n,state):
    k=0
    array=[[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            array[i][j]=state[k]
            k=k+1
    return array

"""Terminal Status Check- Returns Fail if the state matches any of the condition
else returns Pass"""
def calcGoal(state,n):
    rCheck=rowCheck(state,n)
    cCheck=colCheck(state,n)
    dCheck=diagCheck(state,n)
    if rCheck=="yes" or dCheck=="yes" or cCheck=="yes":
        return "Fail"
    return "Pass"

"""Row Check for each state"""
def rowCheck(state,n):
    count = 0
    fail="no"
    for i in range(n):
        for j in range(n):
            if state[i][j]=="x":
                count+=1
        if count==n:
            fail="yes"
            return fail
        #print count
        count=0
    return fail

"""Column Check for each state"""
def colCheck(state,n):
    count = 0
    fail="no"
    for j in range(n):
        for i in range(n):
            if state[i][j]=="x":
                count+=1
        if count==n:
            fail="yes"
            return fail
        count=0
    return fail

"""Diagonal Check for each state"""
def diagCheck(state,n):
    count = 0
    count1=0
    fail="no"
    for i in range(n):
        if state[i][i]=="x":
            count+=1
        if state[n-1-i][i]=="x":
            count1+=1
    if count==n or count1==n:
        fail="yes"
        return fail
    return fail

"""Traverses one level and finds the children of the particular state which are
not terminal"""
def findChild(list,n):
    #print list.state
    for i in range(list.state.count(".")):
        temp=list.state
        temp=temp.replace(".","y",i+1)
        temp=temp.replace("y",".",(i))
        temp=temp.replace("y","x",1)
        array=makeArray(n,temp)
        #print list
        if (calcGoal(array,n)=="Pass"):
            list.children.append(temp)
            list.value=0
    if list.children == []:
        list.value=-1
    return list

"""Iterates through each children and assigns the MinMax value to the state
till the Timer ends="""
def iteration(level):
    while ((time.clock()-programStart)<timelimit-0.15):
        if(level<=11):
            for child in states.children:
                level+=1
                #print child
                childr = stateclass(child,1,[])
                childofchilds=findChild(childr,n)
                if childofchilds.children==[]:
                    childr.value=1
                    bestmove.append(childr.state)
                else:
                    for schild in childofchilds.children:
                        level+=1
                        schildr = stateclass(schild,1,[])
                        schildofchilds=findChild(schildr,n)
                        if schildofchilds.children!=[]:
                            iteration(level,)
                            childr.value=0
                            secondbestmove.append(childr.state)

"""Finding a non terminal state as a Backup incase the terminal state is not
reached"""
def findNonTerminalState(list):
    for i in range(list.state.count(".")):
        temp=list.state
        temp=temp.replace(".","y",i+1)
        temp=temp.replace("y",".",(i))
        temp=temp.replace("y","x",1)
        array=makeArray(n,temp)
        if (calcGoal(array,n)=="Pass"):
            thirdbestmove.append(temp)

#Main

#Receives Input
input=get_input()

#Starts the clock
programStart=time.clock()

if input =="Error" :
    sys.exit()

#Initialization
bestmove=[]
secondbestmove=[]
thirdbestmove=[]
level=0

#Processing the Input and assigning it to values
n=int(input[1])
state=input[2]
timelimit=int(input[3])
Initstate = stateclass(state,0,[])

#Finding the Child for Initial State
states= findChild(Initstate,n)

#Calling the function to get non terminal states as backup
findNonTerminalState(Initstate)

#Iteration Starts
iteration(0)

#Printing the Solution
if(bestmove!=[]):
    #print "BestMove\t:"
    print bestmove[0]
else:
    try:
        #print "Second Best Move"
        print secondbestmove[random.randrange(0,len(secondbestmove))]
    except:
        try:
            print thirdbestmove[random.randrange(0,len(thirdbestmove))]
        except:
            print "I lose"

#Timer Start
programEnd=time.clock()





